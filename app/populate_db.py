import os
import sys
import datetime
import random
from database import get_db, engine
import models
from app import hash_password

def populate():
    db = get_db()
    
    print("Iniciando carga profunda de datos de prueba...")

    # Limpiar base de datos para recargar limpio (Opcional, pero recomendado para resetear todo)
    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)
    
    # 1. Crear roles
    roles_dict = {}
    roles_data = [
        ("Admin", 1), ("Coordinador", 2), ("Enfermero", 3), 
        ("Medico", 4), ("Psicologo", 5), ("Trabajador Social", 6),
        ("Recreacionista", 7)
    ]
    for nombre, valor in roles_data:
        r = models.Rol(nombre=nombre, valor=valor)
        db.add(r)
        db.commit()
        roles_dict[nombre] = r

    # Admin Master User
    admin_user = models.TokenUsuario(
        nombreUsuario="admin",
        correo="admin@hogar.com",
        contrasenaHash=hash_password("admin123"),
        rol_id=roles_dict["Admin"].idRol
    )
    db.add(admin_user)
    db.commit()

    # 2. Crear Hogar
    hogar = models.HogarGerontologico(
        nombre="Hogar Geriátrico La Esperanza",
        direccion="Av. Principal 456, Ciudad",
        capacidadTotal=40
    )
    db.add(hogar)
    db.commit()
    print("Hogar creado.")

    # 3. Crear Personal masivo según especificaciones (vault)
    # - 1 Coordinador
    # - 15 Enfermeras
    # - 3 Médicos Generales
    # - 2 Trabajadores Sociales
    # - 2 Psicólogos
    # - 5 Recreacionistas
    # - 1 Coordinador Logístico
    personal_specs = [
        ("Coordinador", 1),
        ("Enfermero", 15),
        ("Medico", 3),
        ("Trabajador Social", 2),
        ("Psicologo", 2),
        ("Recreacionista", 5),
        ("Coordinador Logistico", 1)
    ]
    
    nombres_pool = ["Ana", "Carlos", "María", "José", "Laura", "Diego", "Carmen", "Luis", "Elena", "Pedro", "Sofia", "Jorge", "Lucia", "Miguel", "Paula"]
    apellidos_pool = ["García", "Rodríguez", "López", "Martínez", "González", "Pérez", "Sánchez", "Romero", "Fernández", "Díaz", "Torres"]
    
    contador = 1
    personal_list = []
    for tipo, cantidad in personal_specs:
        for _ in range(cantidad):
            nombre = random.choice(nombres_pool)
            apellido = random.choice(apellidos_pool)
            ident = f"{tipo[:3].upper()}{contador:03d}"
            
            p = models.Personal(
                primerNombre=nombre,
                primerApellido=apellido,
                identificacion=ident,
                correoElectronico=f"{nombre.lower()}.{apellido.lower()}{contador}@hogar.com",
                tipoPersonal=tipo
            )
            db.add(p)
            personal_list.append(p)
            contador += 1
            
            # Crear usuario si el rol existe (para poder loguearse a probar)
            if tipo in roles_dict and tipo in ["Enfermero", "Medico"]:
                u = models.TokenUsuario(
                    nombreUsuario=ident.lower(),
                    correo=p.correoElectronico,
                    contrasenaHash=hash_password("123"), # contraseña simple para pruebas
                    rol_id=roles_dict[tipo].idRol
                )
                db.add(u)
    
    db.commit()
    print(f"Personal creado: {len(personal_list)} empleados registrados.")

    # 4. Crear Responsables (unos 20 para asociar a los adultos mayores)
    responsables = []
    for i in range(1, 21):
        r = models.Responsable(
            primerNombre=random.choice(nombres_pool),
            primerApellido=random.choice(apellidos_pool),
            identificacion=f"RES{i:03d}",
            correoElectronico=f"responsable{i}@email.com",
            parentesco=random.choice(["Hijo/a", "Nieto/a", "Sobrino/a", "Hermano/a"])
        )
        db.add(r)
        responsables.append(r)
    db.commit()

    # 5. Crear Adultos Mayores (20 pacientes)
    # Categoría A (Independiente), B (Compartida), C (Diurna)
    categorias = ["A_INDIVIDUAL", "B_COMPARTIDA", "C_DIURNA"]
    
    pacientes = []
    for i in range(1, 21):
        resp = responsables[i-1]
        
        # Preinscripcion
        pre = models.Preinscripcion(responsable_id=resp.idResponsable, estado="APROBADA")
        db.add(pre)
        db.commit()
        
        cat = random.choice(categorias)
        am = models.AdultoMayor(
            primerNombre=random.choice(["Don", "Doña"]) + " " + random.choice(nombres_pool),
            primerApellido=random.choice(apellidos_pool),
            identificacion=f"PAC{i:03d}",
            edad=random.randint(65, 95),
            categoriaServicio=cat,
            responsable_id=resp.idResponsable,
            preinscripcion_id=pre.idPreinscripcion,
            activo=True,
            fechaIngreso=datetime.date.today() - datetime.timedelta(days=random.randint(10, 300))
        )
        db.add(am)
        pacientes.append(am)
    db.commit()
    print(f"Adultos Mayores creados: {len(pacientes)} pacientes activos registrados.")

    # 6. Crear Seguimiento Clínico masivo (Diagnósticos y Bitácoras)
    enfermeros = [p for p in personal_list if p.tipoPersonal == "Enfermero"]
    medicos = [p for p in personal_list if p.tipoPersonal == "Medico"]
    
    diagnosticos_medicos = ["Hipertensión arterial", "Diabetes Mellitus Tipo II", "Artrosis de rodilla", "Artritis reumatoide", "EPOC leve"]
    diagnosticos_psic = ["Ansiedad leve", "Depresión estacionaria", "Demencia senil incipiente", "Buen estado cognitivo"]
    
    for am in pacientes:
        # 1 a 3 diagnósticos por paciente
        for _ in range(random.randint(1, 3)):
            tipo = random.choice(["Medico", "Psicologico", "Nutricional"])
            if tipo == "Medico":
                desc = random.choice(diagnosticos_medicos)
            elif tipo == "Psicologico":
                desc = random.choice(diagnosticos_psic)
            else:
                desc = "Dieta hiposódica y control de carbohidratos."
                
            d = models.Diagnostico(tipo=tipo, descripcion=desc, adulto_mayor_id=am.idAdulto)
            db.add(d)
        
        # 3 a 5 bitácoras por paciente simulando días pasados
        for j in range(random.randint(3, 5)):
            fecha_pasada = datetime.datetime.now() - datetime.timedelta(days=j, hours=random.randint(1, 12))
            enf = random.choice(enfermeros).identificacion.lower()
            
            b = models.BitacoraDiaria(
                fechaHora=fecha_pasada.strftime("%Y-%m-%d %H:%M"),
                signosVitales=f"PA: {random.randint(110, 140)}/{random.randint(70, 90)}, FC: {random.randint(60, 85)}",
                observaciones="Paciente estable. " + random.choice(["Durmió bien.", "Comió todo su alimento.", "Participó en actividades.", "Se quejó de dolor leve."]),
                adulto_mayor_id=am.idAdulto,
                registradoPor=enf
            )
            db.add(b)
            
    db.commit()
    print("Historial clínico generado (Diagnósticos y Bitácoras).")
    print("¡Base de datos POBLADA MASIVAMENTE con éxito!")

if __name__ == "__main__":
    populate()
