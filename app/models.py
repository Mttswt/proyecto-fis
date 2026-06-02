import datetime
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Rol(Base):
    __tablename__ = "roles"

    idRol = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, index=True)
    valor = Column(Integer)

    usuarios = relationship("TokenUsuario", back_populates="rol")

class TokenUsuario(Base):
    __tablename__ = "usuarios"

    idUsuario = Column(Integer, primary_key=True, index=True)
    nombreUsuario = Column(String(50), unique=True, index=True)
    correo = Column(String(100), unique=True, index=True)
    contrasenaHash = Column(String(100)) # bcrypt hash
    activo = Column(Boolean, default=True)
    fechaCreacion = Column(Date, default=datetime.date.today)
    
    rol_id = Column(Integer, ForeignKey("roles.idRol"))
    rol = relationship("Rol", back_populates="usuarios")

class HogarGerontologico(Base):
    __tablename__ = "hogares"

    idHogar = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    direccion = Column(String(200))
    capacidadTotal = Column(Integer)
    activo = Column(Boolean, default=True)
    fechaCreacion = Column(Date, default=datetime.date.today)

    habitaciones = relationship("Habitacion", back_populates="hogar")
    espacios = relationship("EspacioComun", back_populates="hogar")

class Habitacion(Base):
    __tablename__ = "habitaciones"

    idHabitacion = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(10))
    tipo = Column(String(20)) # INDIVIDUAL, DOBLE
    estado = Column(String(20), default="DISPONIBLE")
    
    hogar_id = Column(Integer, ForeignKey("hogares.idHogar"))
    hogar = relationship("HogarGerontologico", back_populates="habitaciones")

class EspacioComun(Base):
    __tablename__ = "espacios_comunes"

    idEspacio = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(80))
    tipo = Column(String(50))

    hogar_id = Column(Integer, ForeignKey("hogares.idHogar"))
    hogar = relationship("HogarGerontologico", back_populates="espacios")

class Personal(Base):
    __tablename__ = "personal"

    idPersonal = Column(Integer, primary_key=True, index=True)
    primerNombre = Column(String(30))
    primerApellido = Column(String(30))
    identificacion = Column(String(20), unique=True)
    correoElectronico = Column(String(100), unique=True)
    fechaContratacion = Column(Date, default=datetime.date.today)
    activo = Column(Boolean, default=True)
    tipoPersonal = Column(String(50)) # Coordinador, Enfermero, Medico...

class Responsable(Base):
    __tablename__ = "responsables"

    idResponsable = Column(Integer, primary_key=True, index=True)
    primerNombre = Column(String(30))
    primerApellido = Column(String(30))
    identificacion = Column(String(20), unique=True)
    correoElectronico = Column(String(100))
    telefono = Column(String(20))
    parentesco = Column(String(50))

    adultos_a_cargo = relationship("AdultoMayor", back_populates="responsable")
    preinscripciones = relationship("Preinscripcion", back_populates="responsable")

class Preinscripcion(Base):
    __tablename__ = "preinscripciones"

    idPreinscripcion = Column(Integer, primary_key=True, index=True)
    fechaEnvio = Column(Date, default=datetime.date.today)
    estado = Column(String(20), default="PENDIENTE") # PENDIENTE, APROBADA, RECHAZADA

    responsable_id = Column(Integer, ForeignKey("responsables.idResponsable"))
    responsable = relationship("Responsable", back_populates="preinscripciones")

    adultos_mayores = relationship("AdultoMayor", back_populates="preinscripcion")

class AdultoMayor(Base):
    __tablename__ = "adultos_mayores"

    idAdulto = Column(Integer, primary_key=True, index=True)
    primerNombre = Column(String(30))
    primerApellido = Column(String(30))
    identificacion = Column(String(20), unique=True)
    edad = Column(Integer)
    categoriaServicio = Column(String(20)) # A_INDIVIDUAL, B_COMPARTIDA, C_DIURNA
    activo = Column(Boolean, default=False)
    fechaIngreso = Column(Date, nullable=True)

    responsable_id = Column(Integer, ForeignKey("responsables.idResponsable"))
    responsable = relationship("Responsable", back_populates="adultos_a_cargo")
    
    preinscripcion_id = Column(Integer, ForeignKey("preinscripciones.idPreinscripcion"))
    preinscripcion = relationship("Preinscripcion", back_populates="adultos_mayores")
    
    diagnosticos = relationship("Diagnostico", back_populates="adulto_mayor")
    planes_atencion = relationship("PlanAtencion", back_populates="adulto_mayor")
    bitacoras = relationship("BitacoraDiaria", back_populates="adulto_mayor")

class Diagnostico(Base):
    __tablename__ = "diagnosticos"

    idDiagnostico = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, default=datetime.date.today)
    descripcion = Column(String(500))
    tipo = Column(String(50)) # MEDICO, PSICOLOGICO, etc.

    adulto_mayor_id = Column(Integer, ForeignKey("adultos_mayores.idAdulto"))
    adulto_mayor = relationship("AdultoMayor", back_populates="diagnosticos")

class PlanAtencion(Base):
    __tablename__ = "planes_atencion"

    idPlan = Column(Integer, primary_key=True, index=True)
    fechaInicio = Column(Date, default=datetime.date.today)
    objetivos = Column(String(500))
    frecuenciaRevision = Column(String(50))

    adulto_mayor_id = Column(Integer, ForeignKey("adultos_mayores.idAdulto"))
    adulto_mayor = relationship("AdultoMayor", back_populates="planes_atencion")

class BitacoraDiaria(Base):
    __tablename__ = "bitacoras_diarias"

    idBitacora = Column(Integer, primary_key=True, index=True)
    fechaHora = Column(String(50))
    observaciones = Column(String(1000))
    signosVitales = Column(String(100)) # e.g. "PA: 120/80, FC: 75"

    adulto_mayor_id = Column(Integer, ForeignKey("adultos_mayores.idAdulto"))
    adulto_mayor = relationship("AdultoMayor", back_populates="bitacoras")
    
    # En un sistema completo esto apuntaría al ID del personal (Enfermero/Medico)
    registradoPor = Column(String(100))
