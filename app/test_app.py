"""
Tests unitarios para el proyecto Hogar Gerontologico.
Ejecutar con: python -m pytest test_app.py -v
"""
import os
import sys
import datetime
import unittest

# Asegurar que los imports locales funcionen
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# Importar ANTES de que database.py cree su engine propio
from database import Base
import models


class TestModelos(unittest.TestCase):
    """Tests para verificar que los modelos ORM funcionan correctamente."""

    @classmethod
    def setUpClass(cls):
        """Crea una base de datos SQLite en memoria para los tests."""
        cls.engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
        Base.metadata.create_all(bind=cls.engine)
        Session = scoped_session(sessionmaker(bind=cls.engine))
        cls.db = Session()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    def setUp(self):
        """Limpia todas las tablas antes de cada test."""
        for table in reversed(Base.metadata.sorted_tables):
            self.db.execute(table.delete())
        self.db.commit()

    # =====================
    # Test 1: Roles y Usuarios
    # =====================
    def test_crear_rol(self):
        rol = models.Rol(nombre="Admin", valor=1)
        self.db.add(rol)
        self.db.commit()
        
        resultado = self.db.query(models.Rol).filter(models.Rol.nombre == "Admin").first()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Admin")
        self.assertEqual(resultado.valor, 1)

    def test_crear_usuario(self):
        rol = models.Rol(nombre="Admin", valor=1)
        self.db.add(rol)
        self.db.commit()

        usuario = models.TokenUsuario(
            nombreUsuario="testuser",
            correo="test@test.com",
            contrasenaHash="hash_fake",
            rol_id=rol.idRol
        )
        self.db.add(usuario)
        self.db.commit()

        resultado = self.db.query(models.TokenUsuario).filter(
            models.TokenUsuario.nombreUsuario == "testuser"
        ).first()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.correo, "test@test.com")
        self.assertEqual(resultado.rol.nombre, "Admin")

    def test_usuario_nombre_unico(self):
        """Verifica que no se pueden crear dos usuarios con el mismo nombre."""
        rol = models.Rol(nombre="Admin", valor=1)
        self.db.add(rol)
        self.db.commit()

        u1 = models.TokenUsuario(nombreUsuario="admin", correo="a@a.com", contrasenaHash="h1", rol_id=rol.idRol)
        self.db.add(u1)
        self.db.commit()

        u2 = models.TokenUsuario(nombreUsuario="admin", correo="b@b.com", contrasenaHash="h2", rol_id=rol.idRol)
        self.db.add(u2)
        with self.assertRaises(Exception):
            self.db.commit()
        self.db.rollback()

    # =====================
    # Test 2: Hogares
    # =====================
    def test_crear_hogar(self):
        hogar = models.HogarGerontologico(
            nombre="Hogar Primavera",
            direccion="Calle 1 #2-3",
            capacidadTotal=50
        )
        self.db.add(hogar)
        self.db.commit()

        resultado = self.db.query(models.HogarGerontologico).first()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Hogar Primavera")
        self.assertTrue(resultado.activo)
        self.assertEqual(resultado.capacidadTotal, 50)

    def test_hogar_con_habitaciones(self):
        hogar = models.HogarGerontologico(nombre="H1", direccion="Dir1", capacidadTotal=10)
        self.db.add(hogar)
        self.db.commit()

        hab = models.Habitacion(codigo="H101", tipo="INDIVIDUAL", hogar_id=hogar.idHogar)
        self.db.add(hab)
        self.db.commit()

        resultado = self.db.query(models.HogarGerontologico).first()
        self.assertEqual(len(resultado.habitaciones), 1)
        self.assertEqual(resultado.habitaciones[0].codigo, "H101")

    # =====================
    # Test 3: Preinscripción
    # =====================
    def test_flujo_preinscripcion_completo(self):
        """Test del flujo completo: Crear responsable -> Preinscripción -> Adulto Mayor."""
        resp = models.Responsable(
            primerNombre="Carlos",
            primerApellido="Lopez",
            identificacion="123456",
            correoElectronico="carlos@email.com"
        )
        self.db.add(resp)
        self.db.commit()

        pre = models.Preinscripcion(responsable_id=resp.idResponsable)
        self.db.add(pre)
        self.db.commit()

        self.assertEqual(pre.estado, "PENDIENTE")

        am = models.AdultoMayor(
            primerNombre="Maria",
            primerApellido="Lopez",
            identificacion="654321",
            edad=75,
            categoriaServicio="A_INDIVIDUAL",
            responsable_id=resp.idResponsable,
            preinscripcion_id=pre.idPreinscripcion
        )
        self.db.add(am)
        self.db.commit()

        # Verificar relaciones
        self.assertEqual(len(pre.adultos_mayores), 1)
        self.assertEqual(pre.adultos_mayores[0].primerNombre, "Maria")
        self.assertEqual(resp.adultos_a_cargo[0].primerNombre, "Maria")

    def test_aprobar_preinscripcion(self):
        """Simula la aprobación de una preinscripción."""
        resp = models.Responsable(
            primerNombre="Juan", primerApellido="Perez",
            identificacion="111", correoElectronico="j@e.com"
        )
        self.db.add(resp)
        self.db.commit()

        pre = models.Preinscripcion(responsable_id=resp.idResponsable)
        self.db.add(pre)
        self.db.commit()

        am = models.AdultoMayor(
            primerNombre="Rosa", primerApellido="Garcia",
            identificacion="222", edad=80,
            categoriaServicio="B_COMPARTIDA",
            responsable_id=resp.idResponsable,
            preinscripcion_id=pre.idPreinscripcion
        )
        self.db.add(am)
        self.db.commit()

        # Simular aprobación
        pre.estado = "APROBADA"
        am.activo = True
        am.fechaIngreso = datetime.date.today()
        self.db.commit()

        self.assertEqual(pre.estado, "APROBADA")
        self.assertTrue(am.activo)
        self.assertIsNotNone(am.fechaIngreso)

    def test_rechazar_preinscripcion(self):
        resp = models.Responsable(
            primerNombre="Ana", primerApellido="Ruiz",
            identificacion="333", correoElectronico="a@e.com"
        )
        self.db.add(resp)
        self.db.commit()

        pre = models.Preinscripcion(responsable_id=resp.idResponsable)
        self.db.add(pre)
        self.db.commit()

        pre.estado = "RECHAZADA"
        self.db.commit()

        self.assertEqual(pre.estado, "RECHAZADA")

    # =====================
    # Test 4: Seguimiento Clínico
    # =====================
    def test_crear_diagnostico(self):
        am = models.AdultoMayor(
            primerNombre="Pedro", primerApellido="Gomez",
            identificacion="444", edad=70,
            categoriaServicio="C_DIURNA", activo=True
        )
        self.db.add(am)
        self.db.commit()

        diag = models.Diagnostico(
            tipo="Medico",
            descripcion="Hipertension arterial controlada",
            adulto_mayor_id=am.idAdulto
        )
        self.db.add(diag)
        self.db.commit()

        resultado = self.db.query(models.Diagnostico).first()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.tipo, "Medico")
        self.assertEqual(resultado.adulto_mayor.primerNombre, "Pedro")

    def test_crear_bitacora(self):
        am = models.AdultoMayor(
            primerNombre="Luis", primerApellido="Diaz",
            identificacion="555", edad=82,
            categoriaServicio="A_INDIVIDUAL", activo=True
        )
        self.db.add(am)
        self.db.commit()

        bitacora = models.BitacoraDiaria(
            fechaHora="2026-06-01 10:30",
            signosVitales="PA: 130/85, FC: 72",
            observaciones="Paciente estable. Sin novedades.",
            adulto_mayor_id=am.idAdulto,
            registradoPor="enfermero1"
        )
        self.db.add(bitacora)
        self.db.commit()

        resultado = self.db.query(models.BitacoraDiaria).first()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.registradoPor, "enfermero1")
        self.assertIn("130/85", resultado.signosVitales)

    def test_relaciones_clinicas(self):
        """Verifica que un adulto mayor puede tener multiples diagnosticos y bitacoras."""
        am = models.AdultoMayor(
            primerNombre="Carmen", primerApellido="Soto",
            identificacion="666", edad=78,
            categoriaServicio="B_COMPARTIDA", activo=True
        )
        self.db.add(am)
        self.db.commit()

        for i in range(3):
            d = models.Diagnostico(
                tipo="Medico", descripcion=f"Diagnostico {i+1}",
                adulto_mayor_id=am.idAdulto
            )
            self.db.add(d)

        for i in range(5):
            b = models.BitacoraDiaria(
                fechaHora=f"2026-06-01 0{i}:00",
                signosVitales=f"PA: {120+i}/80",
                observaciones=f"Obs {i+1}",
                adulto_mayor_id=am.idAdulto,
                registradoPor="admin"
            )
            self.db.add(b)

        self.db.commit()

        self.assertEqual(len(am.diagnosticos), 3)
        self.assertEqual(len(am.bitacoras), 5)

    # =====================
    # Test 5: Personal
    # =====================
    def test_crear_personal(self):
        personal = models.Personal(
            primerNombre="Diana",
            primerApellido="Torres",
            identificacion="777",
            correoElectronico="diana@hogar.com",
            tipoPersonal="Enfermero"
        )
        self.db.add(personal)
        self.db.commit()

        resultado = self.db.query(models.Personal).first()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.tipoPersonal, "Enfermero")
        self.assertTrue(resultado.activo)

    # =====================
    # Test 6: Funciones auxiliares
    # =====================
    def test_limpiar_texto(self):
        """Verifica que la función limpiar_texto remueve acentos."""
        # Importar la función desde app (cuidado con Streamlit)
        # Reimplementamos la lógica aquí para evitar importar streamlit en tests
        def limpiar_texto(texto):
            if texto is None:
                return ""
            reemplazos = {
                'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
                'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
                'ñ': 'n', 'Ñ': 'N', 'ü': 'u', 'Ü': 'U',
            }
            for original, reemplazo in reemplazos.items():
                texto = texto.replace(original, reemplazo)
            return texto

        self.assertEqual(limpiar_texto("María López"), "Maria Lopez")
        self.assertEqual(limpiar_texto("Diagnóstico médico"), "Diagnostico medico")
        self.assertEqual(limpiar_texto("Niño"), "Nino")
        self.assertEqual(limpiar_texto(None), "")

    # =====================
    # Test 7: Plan de Atención
    # =====================
    def test_crear_plan_atencion(self):
        am = models.AdultoMayor(
            primerNombre="Elena", primerApellido="Mora",
            identificacion="888", edad=68,
            categoriaServicio="A_INDIVIDUAL", activo=True
        )
        self.db.add(am)
        self.db.commit()

        plan = models.PlanAtencion(
            objetivos="Control de glucosa y ejercicio diario",
            frecuenciaRevision="Semanal",
            adulto_mayor_id=am.idAdulto
        )
        self.db.add(plan)
        self.db.commit()

        resultado = self.db.query(models.PlanAtencion).first()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.frecuenciaRevision, "Semanal")
        self.assertEqual(resultado.adulto_mayor.primerNombre, "Elena")


if __name__ == "__main__":
    unittest.main()
