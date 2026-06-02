> [!info] Enlaces Relacionados
> 🗂️ **Índice central:** [[Indice_Proyecto]]
> ⚙️ **Especificación Funcional:** [[proeycto1]]

Especificación Estructural
Proyecto Semestral 2026-I
Miguel Ángel Jimenez Suspes (20231020027)
Matthew Stev Toro Mondragon (20231020077)
Fundamentos de Ingeniería de Software
Henry Alberto Diosa

Tabla de contenidos
1. Diagrama de clases ............................................................................................................ 3
2. Diccionario de clases ......................................................................................................... 4
3. Modelado de persistencia ..................................................................................................... 38
3.1 Patrones de fuente de datos ............................................................................................ 38
3.2 Estrategia de mapeo ......................................................................................................... 4
3.3 Modelo Relacional ......................................................................................................... 43
4. Diseño básico de interfaz gráfica de usuario ....................................................................... 48
4.1 Mapas de navegación y bocetos visuales IGU ............................................................... 48
5. Bibliografia .......................................................................................................................... 62

|     |     |     |
| --- | --- | --- |

1. Diagrama de clases

|     |     |     |
| --- | --- | --- |

|     |     |     |     |     |
| --- | --- | --- | --- | --- |

2. Diccionario de clases

Clase: «abstract» Persona
DESCRIPCIÓN: Clase abstracta raíz del modelo de personas. Define los atributos y operaciones
comunes a todo tipo de persona registrada en el sistema (adulto mayor, responsable y personal
del hogar). No puede instanciarse directamente.
Capa de atributos
Dominio de
| Visibilidad  | Nombre  | Tipo  | Multiplicidad  |     |
| ------------ | ------- | ----- | -------------- | --- |
valores
Numérico > 0,
| Privado  | idPersona  | Integer  | 1   |     |
| -------- | ---------- | -------- | --- | --- |
único
2-30 caracteres, sin
| Privado  | primerNombre  | String  | 1   |     |
| -------- | ------------- | ------- | --- | --- |
números
2-30 caracteres, sin
| Privado  | segundoNombre  | String  | 0..1  |     |
| -------- | -------------- | ------- | ----- | --- |
números
2-30 caracteres, sin
| Privado  | primerApellido  | String  | 1   |     |
| -------- | --------------- | ------- | --- | --- |
números
2-30 caracteres, sin
| Privado  | segundoApellido  | String  | 0..1  |     |
| -------- | ---------------- | ------- | ----- | --- |
números
10-12 caracteres
| Privado  | identificacion  | String  | 1   |     |
| -------- | --------------- | ------- | --- | --- |
numéricos, único
Formato email
| Privado  | correoElectronico  | String  | 1   |     |
| -------- | ------------------ | ------- | --- | --- |
válido, único
7-15 caracteres
| Privado  | telefono  | String  | 1   |     |
| -------- | --------- | ------- | --- | --- |
numéricos
Formato YYYY-
| Privado  | fechaRegistro  | LocalDate  | 1   |     |
| -------- | -------------- | ---------- | --- | --- |
MM-DD, no futura
|     |     |     |     |     |
| --- | --- | --- | --- | --- |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Referencia al
| Privado  | tokenAccess  | TokenUsuario  | 1   | objeto  |     |
| -------- | ------------ | ------------- | --- | ------- | --- |
TokenUsuario
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
Concatena
nombres y
Público  obtenerNombreCompleto  Sin parámetros  String  apellidos en un solo
String ordenado
para presentación.
Verifica que todos
los atributos
obligatorios
| Público  | esValido  | Sin parámetros  | Boolean  |     |     |
| -------- | --------- | --------------- | -------- | --- | --- |
cumplan las
restricciones de
dominio.

Clase: AdultoMayor
DESCRIPCIÓN: Representa a un adulto mayor residente o aspirante del hogar gerontológico.
Hereda los datos básicos de Persona y agrega los atributos específicos del servicio geriátrico
(edad, fecha de ingreso, categoría de servicio, hoja de vida asociada).
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
Atributos heredados
| —   |     | —   | —   | —   |     |
| --- | --- | --- | --- | --- | --- |
de Persona
Numérico, entre 60 y
| Privado  | edad  | Integer  | 1   |     |     |
| -------- | ----- | -------- | --- | --- | --- |
120
Formato YYYY-MM-
| Privado  | fechaIngreso  | LocalDate  | 1   |     |     |
| -------- | ------------- | ---------- | --- | --- | --- |
DD, no futura
Enum
{A_INDIVIDUAL,
| Privado  | categoriaServicio  | CategoriaServicio  | 1   |     |     |
| -------- | ------------------ | ------------------ | --- | --- | --- |
B_COMPARTIDA,
C_DIURNA}
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

True (residente
| Privado  | activo  | Boolean  | 1   | actual) / False  |     |
| -------- | ------- | -------- | --- | ---------------- | --- |
(egresado)
Referencia al objeto
| Privado  | responsable  | Responsable  | 1   |     |     |
| -------- | ------------ | ------------ | --- | --- | --- |
Responsable
Referencia al
| Privado  | enfermero  | Enfermero  | 1   |     |     |
| -------- | ---------- | ---------- | --- | --- | --- |
enfermero asignado
Referencia al objeto
| Privado  | hojaDeVida  | HojaDeVida  | 1   | HojaDeVida  |     |
| -------- | ----------- | ----------- | --- | ----------- | --- |
(composición)
Bitácoras diarias
| Privado  | bitacorasDiarias  | BitacoraDiaria  | 1..*  | asociadas  |     |
| -------- | ----------------- | --------------- | ----- | ---------- | --- |
(composición)
Lista de reportes
| Privado  | reportes  | List<Reporte>  | 0..*  |     |     |
| -------- | --------- | -------------- | ----- | --- | --- |
generados
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
Retorna la edad
Público  obtenerEdad  Sin parámetros  Integer  actual del adulto
mayor.
Indica si el adulto
mayor está
| Público  | estaActivo  | Sin parámetros  | Boolean  |     |     |
| -------- | ----------- | --------------- | -------- | --- | --- |
actualmente en el
hogar.
Agrega un nuevo
Público  agregarReporte  reporte: Reporte  void  reporte a la lista de
reportes.
Elimina un reporte de
| Público  | eliminarReporte  | Sin parámetros  | void  |     |     |
| -------- | ---------------- | --------------- | ----- | --- | --- |
la lista.

Clase: Responsable
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

DESCRIPCIÓN: Representa a la persona que responde legal y económicamente por uno o varios
adultos mayores. Es quien puede registrar preinscripciones, consultar el seguimiento y ser
contactado por la coordinación.
Capa de atributos
Dominio de
Visibilidad Nombre Tipo Multiplicidad
valores
Atributos heredados de
— — — —
Persona
Texto corto (hijo,
Privado parentesco String 1 hija, cónyuge,
sobrino, etc.)
Lista de adultos
Privado adultosACargo List<AdultoMayor> 1..* mayores bajo
responsabilidad
Capa de métodos
Tipo de
Visibilidad Nombre Parámetros Intencionalidad
retorno
Retorna el número
de adultos mayores
Público cantidadAdultosACargo Sin parámetros Integer
bajo
responsabilidad.
Agrega un adulto
Público agregarAdultoMayor am: AdultoMayor void mayor a la lista de
responsabilidades.
Elimina un adulto
Público eliminarAdultoMayor Sin parámetros void mayor de la lista de
responsabilidades.
Clase: «abstract» Personal
DESCRIPCIÓN: Clase abstracta que representa a cualquier miembro del personal contratado por
la entidad. Agrupa los atributos y operaciones comunes a todos los cargos del hogar. Sus
subclases concretas son las que pueden instanciarse.
Capa de atributos

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
Atributos heredados
| —   |     | —   | —   | —   |     |
| --- | --- | --- | --- | --- | --- |
de Persona
Formato YYYY-MM-
| Privado  | fechaContratacion  | LocalDate  | 1   |     |     |
| -------- | ------------------ | ---------- | --- | --- | --- |
DD, no futura
True (contrato
| Privado  | activo  | Boolean  | 1   | vigente) / False (ex- |     |
| -------- | ------- | -------- | --- | --------------------- | --- |
empleado)
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
Indica si el empleado
Público  estaActivo  Sin parámetros  Boolean  tiene contrato vigente
con la entidad.

Clase: Enfermero
DESCRIPCIÓN: Miembro del personal encargado del cuidado directo y diario del adulto mayor.
Registra bitácoras, controla asistencia de estancia diurna y aplica los planes de medicamentos
definidos por el médico.
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
Atributos heredados
| —   |     | —   | —   | —   |     |
| --- | --- | --- | --- | --- | --- |
de Personal
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —

Clase: Medico
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

DESCRIPCIÓN: Profesional médico que realiza el diagnóstico clínico inicial, prescribe el plan de
medicamentos y emite recomendaciones específicas de atención para cada adulto mayor del
hogar.
Capa de atributos
Visibilidad Nombre Tipo Multiplicidad Dominio de valores
Atributos heredados
— — — —
de Personal
Capa de métodos
Tipo de
Visibilidad Nombre Parámetros Intencionalidad
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —
Clase: TrabajadorSocial
DESCRIPCIÓN: Profesional encargado del diagnóstico psicosocial del adulto mayor al ingreso y
del seguimiento de su entorno familiar y red de apoyo.
Capa de atributos
Visibilidad Nombre Tipo Multiplicidad Dominio de valores
Atributos heredados
— — — —
de Personal
Capa de métodos
Tipo de
Visibilidad Nombre Parámetros Intencionalidad
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —
Clase: Psicologo
DESCRIPCIÓN: Profesional de salud mental que acompaña a los adultos mayores en aspectos
cognitivos y emocionales durante su estadía en el hogar.

Capa de atributos
Visibilidad Nombre Tipo Multiplicidad Dominio de valores
Atributos heredados
— — — —
de Personal
Capa de métodos
Tipo de
Visibilidad Nombre Parámetros Intencionalidad
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —
Clase: Recreacionista
DESCRIPCIÓN: Miembro del personal encargado de las actividades lúdicas, físicas y de
integración social dentro del hogar.
Capa de atributos
Visibilidad Nombre Tipo Multiplicidad Dominio de valores
Atributos heredados
— — — —
de Personal
Capa de métodos
Tipo de
Visibilidad Nombre Parámetros Intencionalidad
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —
Clase: Cocinero
DESCRIPCIÓN: Miembro del personal responsable de la preparación de alimentos en el hogar
gerontológico, atendiendo las dietas especiales definidas por el equipo médico.
Capa de atributos
Visibilidad Nombre Tipo Multiplicidad Dominio de valores

Atributos heredados
— — — —
de Personal
Capa de métodos
Tipo de
Visibilidad Nombre Parámetros Intencionalidad
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —
Clase: ServiciosGenerales
DESCRIPCIÓN: Personal de apoyo encargado de aseo, lavandería y mantenimiento general de
las instalaciones del hogar.
Capa de atributos
Visibilidad Nombre Tipo Multiplicidad Dominio de valores
Atributos heredados
— — — —
de Personal
Capa de métodos
Tipo de
Visibilidad Nombre Parámetros Intencionalidad
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —
Clase: CoordinadorHogar
DESCRIPCIÓN: Responsable operativo de un hogar específico. Gestiona las preinscripciones, las
citaciones, la asignación de personal y la hoja de vida del adulto mayor dentro de su hogar.
Capa de atributos
Visibilidad Nombre Tipo Multiplicidad Dominio de valores
Atributos heredados
— — — —
de Personal
Capa de métodos

Tipo de
Visibilidad Nombre Parámetros Intencionalidad
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —
Clase: CoordinadorLogistico
DESCRIPCIÓN: Miembro del personal encargado de la logística general del hogar: insumos,
transporte, programación de visitas externas y gestión de proveedores.
Capa de atributos
Visibilidad Nombre Tipo Multiplicidad Dominio de valores
Atributos heredados
— — — —
de Personal
Capa de métodos
Tipo de
Visibilidad Nombre Parámetros Intencionalidad
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —
Clase: CoordinadorEntidad
DESCRIPCIÓN: Administrador general de la entidad pública. Gestiona la creación de hogares
gerontológicos, administra los usuarios del sistema y supervisa la operación global de la
organización.
Capa de atributos
Visibilidad Nombre Tipo Multiplicidad Dominio de valores
Atributos heredados
— — — —
de Personal
Capa de métodos
Tipo de
Visibilidad Nombre Parámetros Intencionalidad
retorno

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

— Solo operaciones de acceso (getters/setters), no se detallan —

Clase: HogarGerontologico
DESCRIPCIÓN: Representa un hogar gerontológico físico administrado por la entidad pública.
Cada hogar contiene su infraestructura propia (habitaciones y espacios comunes), aloja adultos
mayores y emplea personal.
Capa de atributos
Dominio de
| Visibilidad  | Nombre  | Tipo  | Multiplicidad  |     |     |
| ------------ | ------- | ----- | -------------- | --- | --- |
valores
Numérico > 0,
| Privado  | idHogar  | Integer  | 1   |     |     |
| -------- | -------- | -------- | --- | --- | --- |
único
| Privado  | nombre  | String  | 1   | 5-100 caracteres  |     |
| -------- | ------- | ------- | --- | ----------------- | --- |
10-200
| Privado  | direccion  | String  | 1   |     |     |
| -------- | ---------- | ------- | --- | --- | --- |
caracteres
| Privado  | capacidadTotal  | Integer  | 1   | Numérico > 0  |     |
| -------- | --------------- | -------- | --- | ------------- | --- |
True (operativo) /
| Privado  | activo  | Boolean  | 1   |     |     |
| -------- | ------- | -------- | --- | --- | --- |
False (inactivo)
Formato YYYY-
| Privado  | fechaCreacion  | LocalDate  | 1   |     |     |
| -------- | -------------- | ---------- | --- | --- | --- |
MM-DD
Lista de
habitaciones del
| Privado  | habitaciones  | List<Habitacion>  | 1..*  |     |     |
| -------- | ------------- | ----------------- | ----- | --- | --- |
hogar
(composición)
Lista de
espacios
Privado  espaciosComunes  List<EspacioComun>  1..*  comunes del
hogar
(composición)
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Calcula los
cupos
cat: disponibles para
Público cuposDisponibles Integer
CategoriaServicio la categoría
indicada (A, B o
C).
Cuenta los
adultos mayores
de categoría
Público cuposDiurnosOcupados Sin parámetros Integer
C_DIURNA
registrados
(máx. 10).
Agrega una
Público agregarHabitacion h: Habitacion void nueva habitación
al hogar.
Elimina una
Público eliminarHabitacion Sin parámetros void habitación del
hogar.
Agrega un nuevo
Público agregarEspacioComun e: EspacioComun void espacio común
al hogar.
Elimina un
Público eliminarEspacioComun Sin parámetros void espacio común
del hogar.
Clase: Habitacion
DESCRIPCIÓN: Habitación individual o doble del hogar. Forma parte inseparable del hogar
(composición) y puede alojar uno o dos adultos mayores según su tipo. Registra su estado de
ocupación.
Capa de atributos
Visibilidad Nombre Tipo Multiplicidad Dominio de valores
Código único dentro del
Privado codigo String 1
hogar, 3-10 caracteres
Enum {INDIVIDUAL,
Privado tipo TipoHabitacion 1
DOBLE}

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Enum {DISPONIBLE,
| Privado  | estado  | EstadoHabitacion  | 1   | OCUPADA,  |     |
| -------- | ------- | ----------------- | --- | --------- | --- |
EN_MANTENIMIENTO}
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
Indica si la habitación
Público  estaDisponible  Sin parámetros  Boolean  puede recibir un nuevo
adulto mayor.

Clase: EspacioComun
DESCRIPCIÓN: Espacio compartido del hogar (sala de juegos, biblioteca, comedor, espacio
deportivo, zona verde) disponible para todos los residentes y para uso del personal.
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
| Privado  | idEspacioComun  | Integer  | 1   | Numérico > 0     |     |
| -------- | --------------- | -------- | --- | ---------------- | --- |
| Privado  | nombre          | String   | 1   | 3-80 caracteres  |     |
Enum {SALA_JUEGOS,
BIBLIOTECA,
| Privado  | tipo  | TipoEspacio  | 1   | COMEDOR,  |     |
| -------- | ----- | ------------ | --- | --------- | --- |
ESPACIO_DEPORTIVO,
ZONA_VERDE}
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —

Clase: TokenUsuario
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

DESCRIPCIÓN: Cuenta de acceso al sistema asociada a una persona. Contiene las credenciales
y el token de sesión emitido tras una autenticación exitosa. Una Persona tiene exactamente una
cuenta de TokenUsuario.
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
| Privado  | idUsuario  | Integer  | 1   | Numérico > 0, único  |     |
| -------- | ---------- | -------- | --- | -------------------- | --- |
3-50 caracteres,
| Privado  | nombreUsuario  | String  | 1   |     |     |
| -------- | -------------- | ------- | --- | --- | --- |
único
Formato email válido,
| Privado  | correo  | String  | 1   |     |     |
| -------- | ------- | ------- | --- | --- | --- |
único
Hash BCrypt de 60
| Privado  | contrasenaHash  | String  | 1   |     |     |
| -------- | --------------- | ------- | --- | --- | --- |
caracteres
True (activa) / False
| Privado  | activo  | Boolean  | 1   |     |     |
| -------- | ------- | -------- | --- | --- | --- |
(dada de baja)
Formato YYYY-MM-
| Privado  | fechaCreacion  | LocalDate  | 1   |     |     |
| -------- | -------------- | ---------- | --- | --- | --- |
DD
Referencia al rol
| Privado  | rol  | Roles  | 1   |     |     |
| -------- | ---- | ------ | --- | --- | --- |
asignado al usuario
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
Indica si la cuenta
Público  esActivo  Sin parámetros  Boolean  permite iniciar sesión
en el sistema.

Clase: Roles
DESCRIPCIÓN: Representa un rol asignable a un usuario del sistema. Cada rol agrupa un
conjunto de permisos que determinan qué funcionalidades puede utilizar el usuario.
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

| Privado  | idRol  | Integer  | 1   |     | Numérico > 0, único  |     |     |
| -------- | ------ | -------- | --- | --- | -------------------- | --- | --- |
3-50 caracteres, único
| Privado  | nombre  | String  | 1   |     | (COORDINADOR_HOGAR,  |     |     |
| -------- | ------- | ------- | --- | --- | -------------------- | --- | --- |
MEDICO, etc.)
| Privado  | valor  | Integer  | 1   |     | Nivel jerárquico del rol  |     |     |
| -------- | ------ | -------- | --- | --- | ------------------------- | --- | --- |
Lista de permisos que tiene
| Privado  | permisos  | List<Permiso>  | 1..*  |     |     |     |     |
| -------- | --------- | -------------- | ----- | --- | --- | --- | --- |
el rol
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     |     |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | --- | --- | ---------------- | --- |
retorno
Agrega un permiso al
permiso:
Público  agregarPermiso  Boolean  conjunto del rol, validando
Permiso
que no esté duplicado.
|          |               | permiso:  |          |     | Verifica si el rol cuenta con  |     |     |
| -------- | ------------- | --------- | -------- | --- | ------------------------------ | --- | --- |
| Público  | tienePermiso  |           | Boolean  |     |                                |     |     |
|          |               | Permiso   |          |     | un permiso específico.         |     |     |

Clase: Permiso
DESCRIPCIÓN: Unidad mínima de autorización del sistema. Representa una acción específica
que puede ser realizada por un usuario según el rol que le fue asignado.
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
| Privado  | idPermiso    | Integer  |     | 1   |     | Numérico > 0, único  |     |
| -------- | ------------ | -------- | --- | --- | --- | -------------------- | --- |
| Privado  | nombre       | String   |     | 1   |     | 3-50 caracteres      |     |
| Privado  | descripcion  | String   |     | 1   |     | 10-200 caracteres    |     |
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     |     |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | --- | --- | ---------------- | --- |
retorno
|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

Verifica que el
Público esValido Sin parámetros Boolean permiso tiene nombre
y descripción válidos.
Clase: Preinscripcion
DESCRIPCIÓN: Solicitud inicial registrada por un responsable para inscribir a uno o más adultos
mayores en el hogar. Mantiene el estado del proceso (pendiente, aprobada, rechazada) hasta que
termina el flujo de admisión.
Capa de atributos
Dominio de
Visibilidad Nombre Tipo Multiplicidad
valores
Numérico > 0,
Privado idPreinscripcion Integer 1
único
Formato YYYY-
Privado fechaEnvio LocalDate 1
MM-DD
Enum
{PENDIENTE,
Privado estado EstadoPreinscripcion 1
APROBADA,
RECHAZADA}
Responsable que
Privado responsable Responsable 1 realiza la
preinscripción
Lista de
Privado adultosMayores List<AdultoMayor> 1..* aspirantes a
inscribir
Capa de métodos
Tipo de
Visibilidad Nombre Parámetros Intencionalidad
retorno
Retorna
verdadero si la
Público estaPendiente Sin parámetros Boolean preinscripción aún
no ha sido
atendida.

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Cambia el estado
de la
| Público  | aceptarPreinscripcion  | Sin parámetros  | Boolean  |     |     |
| -------- | ---------------------- | --------------- | -------- | --- | --- |
preinscripción a
APROBADA.
Cambia el estado
de la
| Público  | rechazarPreinscripcion  | Sin parámetros  | Boolean  |     |     |
| -------- | ----------------------- | --------------- | -------- | --- | --- |
preinscripción a
RECHAZADA.
Agrega un
Público  agregarAdultoMayor  am: AdultoMayor  void  aspirante a la
preinscripción.
Elimina un
Público  eliminarAdultoMayor  Sin parámetros  void  aspirante de la
preinscripción.

Clase: CitacionAdmision
DESCRIPCIÓN: Cita agendada por la coordinación para la entrevista y visita diagnóstica del
adulto mayor aspirante. El trabajador social y el médico son los encargados de atenderla.
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
| Privado  | idCitacion  | Integer  | 1   | Numérico > 0  |     |
| -------- | ----------- | -------- | --- | ------------- | --- |
Formato YYYY-MM-
| Privado  | fecha  | LocalDate  | 1   |     |     |
| -------- | ------ | ---------- | --- | --- | --- |
DD, futura
| Privado  | hora   | LocalTime  | 1   | Formato HH:MM      |     |
| -------- | ------ | ---------- | --- | ------------------ | --- |
| Privado  | lugar  | String     | 1   | 10-150 caracteres  |     |
Enum
{PROGRAMADA,
| Privado  | estado  | EstadoCitacion  | 1   |     |     |
| -------- | ------- | --------------- | --- | --- | --- |
REALIZADA,
CANCELADA}
| Privado  | observaciones  | String  | 1   | Texto libre  |     |
| -------- | -------------- | ------- | --- | ------------ | --- |
|          |                |         |     |              |     |

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Responsable
| Privado  | responsable  |     | Responsable  |     | 1   |     | convocado a la  |     |     |
| -------- | ------------ | --- | ------------ | --- | --- | --- | --------------- | --- | --- |
citación
Notificación
| Privado  | notificacion  |     | Notificacion  |     | 1   |     |     |     |     |
| -------- | ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
generada al convocar
Capa de métodos
Tipo de
| Visibilidad  |     | Nombre  | Parámetros  |     |     |     | Intencionalidad  |     |     |
| ------------ | --- | ------- | ----------- | --- | --- | --- | ---------------- | --- | --- |
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —

Clase: HojaDeVida
DESCRIPCIÓN: Documento clínico y psicosocial del adulto mayor. Consolida el estado de salud,
alergias y capacidades de aprendizaje al momento del ingreso, y se va actualizando a lo largo de
su estancia.
Capa de atributos
| Visibilida |               |         |          |       |     | Multiplicida |     | Dominio de    |     |
| ---------- | ------------- | ------- | -------- | ----- | --- | ------------ | --- | ------------- | --- |
|            |               | Nombre  |          | Tipo  |     |              |     |               |     |
| d          |               |         |          |       |     |              | d   | valores       |     |
| Privado    | idHojaDeVida  |         | Integer  |       |     | 1            |     | Numérico > 0  |     |
Texto libre
describiendo
| Privado  | estadoSalud  |     | String  |     |     | 1   |     |     |     |
| -------- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- |
condición
general
Listado de
| Privado  | alergias  |     | String  |     |     | 1   |     | alergias  |     |
| -------- | --------- | --- | ------- | --- | --- | --- | --- | --------- | --- |
conocidas
|          | capacidadesAprendizaj |     |         |     |     |     |     | Descripción  |     |
| -------- | --------------------- | --- | ------- | --- | --- | --- | --- | ------------ | --- |
| Privado  |                       |     | String  |     |     | 1   |     |              |     |
|          | e                     |     |         |     |     |     |     | cualitativa  |     |
Formato YYYY-
| Privado  | fechaCreacion  |     | LocalDate  |     |     | 1   |     |     |     |
| -------- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
MM-DD
|          | fechaUltimaActualizacio |     |            |     |     |     |     | Formato YYYY- |     |
| -------- | ----------------------- | --- | ---------- | --- | --- | --- | --- | ------------- | --- |
| Privado  |                         |     | LocalDate  |     |     | 1   |     |               |     |
|          | n                       |     |            |     |     |     |     | MM-DD         |     |
|          |                         |     |            |     |     |     |     |               |     |

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Recomendació
|          | recomendacionAtencio |     | RecomendacionAtencio |     |     |     |                  |     |     |
| -------- | -------------------- | --- | -------------------- | --- | --- | --- | ---------------- | --- | --- |
| Privado  |                      |     |                      |     |     | 1   | n asociada a la  |     |     |
|          | n                    |     | n                    |     |     |     |                  |     |     |
hoja de vida
Diagnóstico
(clínico o
| Privado  | diagnostico  |     | Diagnostico  |     |     | 1   |     |     |     |
| -------- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- |
psicosocial)
vinculado
Capa de métodos
| Visibilida |     |         |     |             |     | Tipo de  | Intencionalida |     |     |
| ---------- | --- | ------- | --- | ----------- | --- | -------- | -------------- | --- | --- |
|            |     | Nombre  |     | Parámetros  |     |          |                |     |     |
| d          |     |         |     |             |     | retorno  |                | d   |     |
— Solo operaciones de acceso (getters/setters), no se detallan —

Clase: «abstract» Diagnostico
DESCRIPCIÓN: Clase abstracta que representa un diagnóstico del adulto mayor realizado al
ingreso. Se especializa en diagnóstico psicosocial (trabajador social) y diagnóstico clínico
(médico).
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
| Privado  | idDiagnostico  |     | Integer  |     | 1   |     | Numérico > 0  |     |     |
| -------- | -------------- | --- | -------- | --- | --- | --- | ------------- | --- | --- |
Formato YYYY-MM-
| Privado  | fecha  |     | LocalDate  |     | 1   |     |     |     |     |
| -------- | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- |
DD
| Privado  | antecedentes     |     | String  |     | 1   |     | Texto libre  |     |     |
| -------- | ---------------- | --- | ------- | --- | --- | --- | ------------ | --- | --- |
| Privado  | condicionActual  |     | String  |     | 1   |     | Texto libre  |     |     |
| Privado  | observaciones    |     | String  |     | 1   |     | Texto libre  |     |     |
Capa de métodos
Tipo de
| Visibilidad  |     | Nombre  | Parámetros  |     |     |     | Intencionalidad  |     |     |
| ------------ | --- | ------- | ----------- | --- | --- | --- | ---------------- | --- | --- |
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Clase: DiagnosticoPsicosocial
DESCRIPCIÓN: Diagnóstico psicosocial del adulto mayor al ingreso, realizado por el trabajador
social. Documenta el entorno familiar y la red de apoyo con que cuenta el paciente.
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
Atributos heredados
| —   |     | —   | —   | —   |     |
| --- | --- | --- | --- | --- | --- |
de Diagnostico
| Privado  | entornoFamiliar  | String  | 1   | Texto libre  |     |
| -------- | ---------------- | ------- | --- | ------------ | --- |
| Privado  | redApoyo         | String  | 1   | Texto libre  |     |
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —

Clase: DiagnosticoClinico
DESCRIPCIÓN: Diagnóstico clínico del adulto mayor al ingreso, realizado por el médico. Registra
signos vitales y diagnóstico principal.
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
Atributos heredados
| —   |     | —   | —   | —   |     |
| --- | --- | --- | --- | --- | --- |
de Diagnostico
Presión arterial,
| Privado  | signosVitales  | String  | 1   | pulso, saturación,  |     |
| -------- | -------------- | ------- | --- | ------------------- | --- |
etc.
Texto libre con
| Privado  | diagnosticoPrincipal  | String  | 1   |     |     |
| -------- | --------------------- | ------- | --- | --- | --- |
patología principal
Capa de métodos
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —

Clase: PlanAtencion
DESCRIPCIÓN: Plan individualizado de atención para un adulto mayor, definido por el equipo
profesional (médico y trabajador social). Contiene las directrices de cuidado y un texto de
seguimiento.
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
| Privado  | idPlan  | Integer  | 1   | Numérico > 0  |     |
| -------- | ------- | -------- | --- | ------------- | --- |
Formato YYYY-MM-
| Privado  | fechaInicio  | LocalDate  | 1   |     |     |
| -------- | ------------ | ---------- | --- | --- | --- |
DD
Formato YYYY-MM-
| Privado  | fechaFin  | LocalDate  | 0..1  |     |     |
| -------- | --------- | ---------- | ----- | --- | --- |
DD, posterior a inicio
Texto libre con las
| Privado  | seguimiento  | String  | 1   | directrices de  |     |
| -------- | ------------ | ------- | --- | --------------- | --- |
cuidado
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —

Clase: PlanMedicamento
DESCRIPCIÓN: Plan de administración de medicamentos para un adulto mayor, prescrito por el
médico. Agrupa uno o varios medicamentos con sus dosis y frecuencias.
Capa de atributos
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Dominio de
| Visibilidad  | Nombre  | Tipo  | Multiplicidad  |     |     |
| ------------ | ------- | ----- | -------------- | --- | --- |
valores
| Privado  | idPlan  | Integer  | 1   | Numérico > 0  |     |
| -------- | ------- | -------- | --- | ------------- | --- |
Formato YYYY-
| Privado  | fechaInicio  | LocalDate  | 1   |     |     |
| -------- | ------------ | ---------- | --- | --- | --- |
MM-DD
Formato YYYY-
| Privado  | fechaFin  | LocalDate  | 0..1  |     |     |
| -------- | --------- | ---------- | ----- | --- | --- |
MM-DD
| Privado  | observaciones  | String  | 1   | Texto libre  |     |
| -------- | -------------- | ------- | --- | ------------ | --- |
Lista de
Privado  medicamentos  List<Medicamento>  1..*  medicamentos del
plan
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
Agrega un
Público  agregarMedicamentos  m: Medicamento  void  medicamento al
plan.
Elimina un
Público  eliminarMedicamento  Sin parámetros  void  medicamento del
plan.

Clase: Medicamento
DESCRIPCIÓN: Representa un medicamento específico incluido en un plan de medicamentos,
con su nombre, dosis y frecuencia de administración.
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
| Privado  | nombre  | String  | 1   | 3-100 caracteres  |     |
| -------- | ------- | ------- | --- | ----------------- | --- |
Texto libre (ej.
| Privado  | dosis  | String  | 1   |     |     |
| -------- | ------ | ------- | --- | --- | --- |
500mg)
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Texto libre (ej. cada 8
| Privado  | frecuencia  | String  | 1   |     |     |
| -------- | ----------- | ------- | --- | --- | --- |
horas)
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —

Clase: RecomendacionAtencion
DESCRIPCIÓN: Recomendación particular emitida por un médico o trabajador social, vinculada a
un plan de atención y/o de medicamentos, visible para el personal autorizado.
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
| Privado  | idRecomendacion  | Integer  | 1   | Numérico > 0       |     |
| -------- | ---------------- | -------- | --- | ------------------ | --- |
| Privado  | descripcion      | String   | 1   | 10-500 caracteres  |     |
Formato YYYY-MM-
| Privado  | fecha  | LocalDate  | 1   |     |     |
| -------- | ------ | ---------- | --- | --- | --- |
DD
Plan de atención
| Privado  | planAtencion  | PlanAtencion  | 1   |     |     |
| -------- | ------------- | ------------- | --- | --- | --- |
referenciado
Plan de
| Privado  | planMedicamento  | PlanMedicamento  | 1   | medicamentos  |     |
| -------- | ---------------- | ---------------- | --- | ------------- | --- |
referenciado
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —

Clase: BitacoraDiaria
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

DESCRIPCIÓN: Registro diario de eventos relevantes para un adulto mayor, llevado por el
enfermero asignado. Puede ser de tipo COMPARTIDA (grupo) o INDIVIDUAL.
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
| Privado  | idBitacora  | Integer  | 1   | Numérico > 0  |     |
| -------- | ----------- | -------- | --- | ------------- | --- |
Formato YYYY-MM-
| Privado  | fecha  | LocalDate  | 1   |     |     |
| -------- | ------ | ---------- | --- | --- | --- |
DD
| Privado  | evento         | String  | 1   | 10-500 caracteres  |     |
| -------- | -------------- | ------- | --- | ------------------ | --- |
| Privado  | observaciones  | String  | 1   | Texto libre        |     |
Enum
| Privado  | tipo  | TipoBitacora  | 1   | {COMPARTIDA,  |     |
| -------- | ----- | ------------- | --- | ------------- | --- |
INDIVIDUAL}
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —

Clase: RegistroAsistencia
DESCRIPCIÓN: Registro de entrada y salida diaria de un adulto mayor de categoría C (estancia
diurna). Permite llevar el control horario de permanencia en el hogar.
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
| Privado  | idRegistro  | Integer  | 1   | Numérico > 0  |     |
| -------- | ----------- | -------- | --- | ------------- | --- |
Formato YYYY-MM-
| Privado  | fecha  | LocalDate  | 1   |     |     |
| -------- | ------ | ---------- | --- | --- | --- |
DD
| Privado  | horaEntrada  | LocalTime  | 1   | Formato HH:MM  |     |
| -------- | ------------ | ---------- | --- | -------------- | --- |
|          |              |            |     |                |     |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Formato HH:MM,
| Privado  | horaSalida  | LocalTime  | 0..1  |     |     |
| -------- | ----------- | ---------- | ----- | --- | --- |
posterior a entrada
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —

Clase: AsignacionEnfermero
DESCRIPCIÓN: Clase asociación entre Enfermero y AdultoMayor que registra qué enfermero
tiene asignado qué adulto mayor durante un período determinado.
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
Formato YYYY-MM-
| Privado  | fechaInicio  | LocalDate  | 1   |     |     |
| -------- | ------------ | ---------- | --- | --- | --- |
DD
Formato YYYY-MM-
| Privado  | fechaFin  | LocalDate  | 0..1  |     |     |
| -------- | --------- | ---------- | ----- | --- | --- |
DD, posterior a inicio
True (vigente) / False
| Privado  | activa  | Boolean  | 1   |     |     |
| -------- | ------- | -------- | --- | --- | --- |
(reasignada)
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —

Clase: AsignacionHabitacion
DESCRIPCIÓN: Clase asociación entre AdultoMayor y Habitación que registra la ocupación de
una habitación por un adulto mayor durante un período determinado.
Capa de atributos
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
Formato YYYY-MM-
| Privado  | fechaAsignacion  | LocalDate  | 1   |     |     |
| -------- | ---------------- | ---------- | --- | --- | --- |
DD
Formato YYYY-MM-
| Privado  | fechaFin  | LocalDate  | 0..1  | DD, posterior a  |     |
| -------- | --------- | ---------- | ----- | ---------------- | --- |
asignación
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —

Clase: CitacionReunion
DESCRIPCIÓN: Convocatoria creada por el coordinador del hogar para reuniones con el personal
o con los responsables de los adultos mayores. Puede ser masiva (todo el personal) o selectiva
(grupo específico).
Capa de atributos
Dominio de
| Visibilidad  | Nombre  | Tipo  | Multiplicidad  |     |     |
| ------------ | ------- | ----- | -------------- | --- | --- |
valores
| Privado  | idCitacion  | Integer  | 1   | Numérico > 0  |     |
| -------- | ----------- | -------- | --- | ------------- | --- |
Formato YYYY-MM-
| Privado  | fecha  | LocalDate  | 1   |     |     |
| -------- | ------ | ---------- | --- | --- | --- |
DD, futura
| Privado  | hora    | LocalTime  | 1   | Formato HH:MM      |     |
| -------- | ------- | ---------- | --- | ------------------ | --- |
| Privado  | lugar   | String     | 1   | 10-150 caracteres  |     |
| Privado  | asunto  | String     | 1   | 10-200 caracteres  |     |
Enum {MASIVA,
| Privado  | tipo  | TipoCitacion  | 1   |     |     |
| -------- | ----- | ------------- | --- | --- | --- |
SELECTIVA}
Lista de
Privado  responsables  List<Responsable>  0..*  responsables
convocados
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Notificaciones
| Privado  | notificaciones  | List<Notificacion>  | 1..*  |     |     |
| -------- | --------------- | ------------------- | ----- | --- | --- |
generadas
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
Agrega un
Público  agregarResponsable  r: Responsable  void  responsable a la
lista de convocados.
Elimina un
Público  eliminarResponsable  Sin parámetros  void  responsable de la
lista de convocados.
Agrega una
Público  agregarNotificacion  n: Notificacion  void  notificación a la
citación.
Elimina una
Público  eliminarNotificacion  Sin parámetros  void  notificación de la
citación.

Clase: Notificacion
DESCRIPCIÓN: Mensaje enviado por el sistema a una persona específica. Es generada por los
servicios cuando ocurre un evento relevante (preinscripción, citación, reunión, etc.).
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
| Privado  | idNotificacion  | Integer  | 1   | Numérico > 0       |     |
| -------- | --------------- | -------- | --- | ------------------ | --- |
| Privado  | asunto          | String   | 1   | 10-200 caracteres  |     |
| Privado  | mensaje         | String   | 1   | Texto libre        |     |
Formato YYYY-MM-
| Privado  | fechaEnvio  | LocalDate  | 1   |     |     |
| -------- | ----------- | ---------- | --- | --- | --- |
DD
True (leída) / False
| Privado  | leida  | Boolean  | 1   |     |     |
| -------- | ------ | -------- | --- | --- | --- |
(sin leer)
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | --- | ---------------- | --- |
retorno
— Solo operaciones de acceso (getters/setters), no se detallan —

Clase: Reporte
DESCRIPCIÓN: Reporte en formato PDF generado por el sistema. Puede ser un listado por
categoría, un reporte de seguimiento individual o una hoja de vida consolidada.
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
| Privado  | idReporte        | Integer    | 1   | Numérico > 0        |     |     |
| -------- | ---------------- | ---------- | --- | ------------------- | --- | --- |
| Privado  | titulo           | String     | 1   | 5-150 caracteres    |     |     |
| Privado  | fechaGeneracion  | LocalDate  | 1   | Formato YYYY-MM-DD  |     |     |
Enum
{LISTADO_POR_CATEGORIA,
| Privado  | tipo  | TipoReporte  | 1   |     |     |     |
| -------- | ----- | ------------ | --- | --- | --- | --- |
SEGUIMIENTO_INDIVIDUAL,
HOJA_VIDA_CONSOLIDADA}
Miembro del personal que
| Privado  | personal  | Personal  | 1   |     |     |     |
| -------- | --------- | --------- | --- | --- | --- | --- |
generó el reporte
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- | --- |
retorno
|          |                 | Sin         |       | Genera y persiste el contenido  |     |     |
| -------- | --------------- | ----------- | ----- | ------------------------------- | --- | --- |
| Público  | generarReporte  |             | void  |                                 |     |     |
|          |                 | parámetros  |       | del reporte en formato PDF.     |     |     |

Clase: AutenticacionService
DESCRIPCIÓN: Servicio que encapsula la lógica de autenticación de usuarios: inicio de sesión,
validación de tokens, cierre de sesión y restauración de contraseña.
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
— Los atributos son heredados de la superclase —
Capa de métodos
Tipo de
| Visibilidad  | Nombre  | Parámetros  |     | Intencionalidad  |     |
| ------------ | ------- | ----------- | --- | ---------------- | --- |
retorno
Valida credenciales
|          |                | correo: String,  |               | y, si son correctas,  |     |
| -------- | -------------- | ---------------- | ------------- | --------------------- | --- |
| Público  | iniciarSesion  |                  | TokenUsuario  |                       |     |
|          |                | pwd: String      |               | emite un token de     |     |
sesión.
Revoca el token de
token:
| Público  | cerrarSesion  |     | Boolean  | sesión activo del  |     |
| -------- | ------------- | --- | -------- | ------------------ | --- |
TokenUsuario
usuario.
Genera una nueva
contraseña temporal
| Público  | restaurarContrasena  | correo: String  | Boolean  |     |     |
| -------- | -------------------- | --------------- | -------- | --- | --- |
y la envía al correo
del usuario.
Verifica si un token
| Público  | validarToken  | token: String  | Boolean  |     |     |
| -------- | ------------- | -------------- | -------- | --- | --- |
está activo y vigente.

Clase: UsuariosService
DESCRIPCIÓN: Servicio de gestión del ciclo de vida de los usuarios del sistema. Permite crear,
modificar, eliminar y consultar cuentas de acceso.
Capa de atributos
Dominio de
| Visibilidad  | Nombre  | Tipo  | Multiplicidad  |     |     |
| ------------ | ------- | ----- | -------------- | --- | --- |
valores
— Los atributos son heredados de la superclase —
Capa de métodos
Visibilidad  Nombre  Parámetros  Tipo de retorno  Intencionalidad
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Crea una nueva
datos:
cuenta de usuario
Público crearUsuario TokenUsuario, TokenUsuario
con contraseña
rol: Roles
temporal.
Actualiza los datos
Público modificarUsuario u: TokenUsuario TokenUsuario del usuario
existente.
idUsuario: Da de baja lógica
Público eliminarUsuario Boolean
Integer al usuario.
Lista los usuarios
Público consultarUsuarios Sin parámetros List<TokenUsuario> registrados en el
sistema.
Clase: PreinscripcionService
DESCRIPCIÓN: Servicio que encapsula el proceso completo de preinscripción y admisión:
registro, notificación a coordinación, programación de citaciones y decisión final.
Capa de atributos
Dominio de
Visibilidad Nombre Tipo Multiplicidad
valores
— Los atributos son heredados de la superclase —
Capa de métodos
Visibilidad Nombre Parámetros Tipo de retorno Intencionalidad
Registra una
nueva
r: Responsable,
Público registrarPreinscripcion Preinscripcion preinscripción en
am: AdultoMayor
estado
PENDIENTE.
Genera una
notificación
Público notificarCoordinacion p: Preinscripcion Notificacion automática a la
coordinación del
hogar.

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

Crea una citación
|          |                    | p: Preinscripcion,  |     |                   | de admisión    |     |
| -------- | ------------------ | ------------------- | --- | ----------------- | -------------- | --- |
| Público  | programarCitacion  |                     |     | CitacionAdmision  |                |     |
|          |                    | fecha: LocalDate    |     |                   | asociada a la  |     |
preinscripción.
|          |                   | p: Preinscripcion,  |     |              | Cambia el estado  |     |
| -------- | ----------------- | ------------------- | --- | ------------ | ----------------- | --- |
|          |                   | cat:                |     |              | a APROBADA y      |     |
| Público  | aprobarAspirante  |                     |     | AdultoMayor  |                   |     |
|          |                   | CategoriaServicio,  |     |              | asigna categoría  |     |
|          |                   | hab: Habitacion     |     |              | y habitación.     |     |
Cambia el estado
p: Preinscripcion,
| Público  | rechazarAspirante  |     |     | Preinscripcion  | a RECHAZADA y  |     |
| -------- | ------------------ | --- | --- | --------------- | -------------- | --- |
motivo: String
registra el motivo.

Clase: HogaresService
DESCRIPCIÓN: Servicio de gestión de hogares gerontológicos. Permite crear, consultar,
modificar y eliminar hogares, configurando automáticamente su infraestructura estándar.
Capa de atributos
| Visibilida |         |       |     |                | Dominio de  |     |
| ---------- | ------- | ----- | --- | -------------- | ----------- | --- |
|            | Nombre  | Tipo  |     | Multiplicidad  |             |     |
| d          |         |       |     |                | valores     |     |
— Los atributos son heredados de la superclase —
Capa de métodos
| Visibilida |         |             |     |                  | Intencionalid |     |
| ---------- | ------- | ----------- | --- | ---------------- | ------------- | --- |
|            | Nombre  | Parámetros  |     | Tipo de retorno  |               |     |
| d          |         |             |     |                  | ad            |     |
Crea un
nuevo hogar
con
|          |             | nombre: String,     |     |                     | infraestructura  |     |
| -------- | ----------- | ------------------- | --- | ------------------- | ---------------- | --- |
|          |             | direccion: String,  |     |                     | estándar (10     |     |
| Público  | crearHogar  |                     |     | HogarGerontologico  |                  |     |
|          |             | capacidad:          |     |                     | hab.             |     |
|          |             | Integer             |     |                     | individuales,    |     |
10 dobles,
espacios
comunes).
Ajusta la
h:
|          | configurarInfraestruct |                  |     |          | infraestructura  |     |
| -------- | ---------------------- | ---------------- | --- | -------- | ---------------- | --- |
| Público  |                        | HogarGerontologi |     | Boolean  |                  |     |
|          | ura                    |                  |     |          | de un hogar      |     |
co
existente.
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

Lista los
hogares
List<HogarGerontologi
| Público  | consultarHogares  | Sin parámetros  |     |     | registrados  |     |
| -------- | ----------------- | --------------- | --- | --- | ------------ | --- |
co>
con su estado
actual.
Da de baja
lógica al
hogar,
| Público  | eliminarHogar  | idHogar: Integer  |     | Boolean  |     |     |
| -------- | -------------- | ----------------- | --- | -------- | --- | --- |
preservando
los registros
históricos.

Clase: SeguimientoService
DESCRIPCIÓN: Servicio de seguimiento clínico y psicosocial del adulto mayor. Centraliza el
registro de diagnósticos, planes, bitácoras, asistencia diurna y hoja de vida.
Capa de atributos
| Visibilida |         |     |       |                | Dominio de  |     |
| ---------- | ------- | --- | ----- | -------------- | ----------- | --- |
|            | Nombre  |     | Tipo  | Multiplicidad  |             |     |
| d          |         |     |       |                | valores     |     |
— Los atributos son heredados de la superclase —
Capa de métodos
| Visibilida |         |     |             |                  | Intencionalida |     |
| ---------- | ------- | --- | ----------- | ---------------- | -------------- | --- |
|            | Nombre  |     | Parámetros  | Tipo de retorno  |                |     |
| d          |         |     |             |                  | d              |     |
Registra un
|     |     | am:  |     |     | nuevo  |     |
| --- | --- | ---- | --- | --- | ------ | --- |
Público  registrarDiagnostico  AdultoMayor, d:  Diagnostico  diagnóstico
|     |     | Diagnostico  |     |     | para el adulto  |     |
| --- | --- | ------------ | --- | --- | --------------- | --- |
mayor.
|     |     | am:  |     |     | Crea un plan  |     |
| --- | --- | ---- | --- | --- | ------------- | --- |
Público  registrarPlanAtencion  AdultoMayor, p:  PlanAtencion  de atención
|     |     | PlanAtencion  |     |     | individualizado.  |     |
| --- | --- | ------------- | --- | --- | ----------------- | --- |
am:
Registra la
|          | registrarPlanMedicament | AdultoMayor, p:  |     | PlanMedicament |                  |     |
| -------- | ----------------------- | ---------------- | --- | -------------- | ---------------- | --- |
| Público  |                         |                  |     |                | prescripción de  |     |
|          | os                      | PlanMedicament   |     | o              |                  |     |
medicamentos.
o
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

|          |                    | e: Enfermero,   |     |                 | Registra un    |     |
| -------- | ------------------ | --------------- | --- | --------------- | -------------- | --- |
|          |                    | am:             |     |                 | evento en la   |     |
| Público  | registrarBitacora  |                 |     | BitacoraDiaria  |                |     |
|          |                    | AdultoMayor,    |     |                 | bitácora del   |     |
|          |                    | evento: String  |     |                 | adulto mayor.  |     |
Registra la
am:
entrada diaria
|          |                            | AdultoMayor,  |     | RegistroAsistenci |               |     |
| -------- | -------------------------- | ------------- | --- | ----------------- | ------------- | --- |
| Público  | registrarAsistenciaDiurna  |               |     |                   | de un adulto  |     |
|          |                            | entrada:      |     | a                 |               |     |
mayor de
LocalTime
categoría C.
|          |                       | am:           |     |             | Actualiza los   |     |
| -------- | --------------------- | ------------- | --- | ----------- | --------------- | --- |
|          |                       | AdultoMayor,  |     |             | datos de salud  |     |
| Público  | actualizarHojaDeVida  |               |     | HojaDeVida  |                 |     |
|          |                       | datos:        |     |             | del adulto      |     |
|          |                       | HojaDeVida    |     |             | mayor.          |     |

Clase: AsignacionPersonalService
DESCRIPCIÓN: Servicio que gestiona la asignación de enfermeros a adultos mayores por
categoría de servicio.
Capa de atributos
| Visibilida |         |       |     |                | Dominio de  |     |
| ---------- | ------- | ----- | --- | -------------- | ----------- | --- |
|            | Nombre  | Tipo  |     | Multiplicidad  |             |     |
| d          |         |       |     |                | valores     |     |
— Los atributos son heredados de la superclase —
Capa de métodos
| Visibilida |         |             |     |                  | Intencionalid |     |
| ---------- | ------- | ----------- | --- | ---------------- | ------------- | --- |
|            | Nombre  | Parámetros  |     | Tipo de retorno  |               |     |
| d          |         |             |     |                  | ad            |     |
Crea una
nueva
|          |                   | e: Enfermero, am:  |                      |     | asignación de  |     |
| -------- | ----------------- | ------------------ | -------------------- | --- | -------------- | --- |
| Público  | asignarEnfermero  |                    | AsignacionEnfermero  |     |                |     |
|          |                   | AdultoMayor        |                      |     | enfermero      |     |
con fecha de
vigencia.
Lista las
asignaciones
|          | consultarAsignacio | cat:               | List<AsignacionEnferm |     |          |     |
| -------- | ------------------ | ------------------ | --------------------- | --- | -------- | --- |
| Público  |                    |                    |                       |     | activas  |     |
|          | nes                | CategoriaServicio  | ero>                  |     |          |     |
filtradas por
categoría.
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

Cierra la
asignación
a:
actual y crea
reasignarEnfermer AsignacionEnferm
Público AsignacionEnfermero una nueva
o ero, nuevo:
con el
Enfermero
enfermero
indicado.
Clase: CitacionService
DESCRIPCIÓN: Servicio que gestiona las citaciones a reuniones (masivas o selectivas) y la
generación de notificaciones asociadas a cada destinatario.
Capa de atributos
Dominio de
Visibilidad Nombre Tipo Multiplicidad
valores
— Los atributos son heredados de la superclase —
Capa de métodos
Visibilidad Nombre Parámetros Tipo de retorno Intencionalidad
coord:
Crea una citación
CoordinadorHogar,
a reunión y la
Público crearCitacionReunion destinatarios: CitacionReunion
asocia a los
List<Persona>,
destinatarios.
asunto: String
Genera las
notificaciones
Público notificarDestinatarios c: CitacionReunion List<Notificacion> para cada
persona
convocada.
Clase: ReporteService
DESCRIPCIÓN: Servicio de generación de reportes en formato PDF. Produce listados, reportes
de seguimiento individual y hojas de vida consolidadas.
Capa de atributos

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

| Visibilida |     |     | Multiplicida | Dominio de  |     |
| ---------- | --- | --- | ------------ | ----------- | --- |
Nombre  Tipo
| d   |     |     | d   | valores  |     |
| --- | --- | --- | --- | -------- | --- |
— Los atributos son heredados de la superclase —
Capa de métodos
| Visibilida |     |     | Tipo de  | Intencionalida |     |
| ---------- | --- | --- | -------- | -------------- | --- |
Nombre  Parámetros
| d   |     |     | retorno  | d   |     |
| --- | --- | --- | -------- | --- | --- |
Genera el
|          |                           | h:                 |          | listado de      |     |
| -------- | ------------------------- | ------------------ | -------- | --------------- | --- |
|          | generarListadoPorCategori | HogarGerontologic  |          | adultos         |     |
| Público  |                           |                    | Reporte  |                 |     |
|          | a                         | o, cat:            |          | mayores del     |     |
|          |                           | CategoriaServicio  |          | hogar filtrado  |     |
por categoría.
Genera un
reporte
generarReporteSeguimient
| Público  |     | am: AdultoMayor  | Reporte  | consolidado del  |     |
| -------- | --- | ---------------- | -------- | ---------------- | --- |
o
seguimiento del
adulto mayor.
Genera el PDF
con la hoja de
generarHojaVidaConsolidad
| Público  |     | am: AdultoMayor  | Reporte  | vida completa  |     |
| -------- | --- | ---------------- | -------- | -------------- | --- |
a
del adulto
mayor.
Exporta el
reporte a
| Público  | exportarPDF  | r: Reporte  | String  |     |     |
| -------- | ------------ | ----------- | ------- | --- | --- |
archivo PDF y
retorna la ruta.

Clase: NotificacionService
DESCRIPCIÓN: Servicio que gestiona el envío de notificaciones a los usuarios del sistema por
distintos canales (correo, SMS, sistema interno).
Capa de atributos
Visibilidad  Nombre  Tipo  Multiplicidad  Dominio de valores
— Los atributos son heredados de la superclase —
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

Capa de métodos
Tipo de
Visibilidad Nombre Parámetros Intencionalidad
retorno
destinatario:
Envía una
Persona, asunto:
notificación al
Público enviarNotificacion String, msg: String, Notificacion
destinatario por el
canal:
canal especificado.
CanalNotificacion
Marca la notificación
Público marcarComoLeida n: Notificacion Boolean como leída por el
destinatario.
3. Modelado de persistencia
3.1 Patrones de fuente de datos
La capa de persistencia del sistema de gestión de hogares gerontológicos se implementa
utilizando SQLAlchemy como herramienta de Mapeo Objeto-Relacional (ORM) para el
lenguaje Python. SQLAlchemy actúa como una capa de abstracción sobre la base de datos
relacional PostgreSQL, permitiendo que las operaciones sobre las entidades del dominio se
traduzcan automáticamente a sentencias SQL. Esta abstracción evita que el código de la
aplicación deba preocuparse por los detalles específicos del motor de base de datos,
promoviendo un desarrollo más limpio y mantenible.
La elección de SQLAlchemy se fundamenta en su madurez, su flexibilidad para modelar
relaciones complejas y su perfecta integración con el ecosistema Python. Su enfoque
declarativo permite definir el esquema de la base de datos directamente desde las clases de
Python, lo que garantiza un desarrollo eficiente y un alto rendimiento en las consultas
necesarias para el seguimiento diario de los adultos mayores.

2.2 Patrón de Fuente de Datos: Data Mapper
El sistema se adhiere estrictamente al patrón arquitectónico Data Mapper, una decisión de
diseño fundamental para asegurar la mantenibilidad, testabilidad y escalabilidad del software.
Este patrón, formalizado por Martin Fowler en su catálogo de patrones de arquitectura
empresarial, establece una separación total entre el modelo de dominio (las entidades de
negocio) y la capa de persistencia (la base de datos).
Principio del Data Mapper: A diferencia de patrones como Active Record, donde las
propias entidades contienen métodos para persistirse (save(), delete()), el patrón Data Mapper
externaliza por completo la lógica de persistencia a una clase especializada denominada
Mapper o Repository. De esta forma, las entidades del dominio permanecen como objetos
Python puros (POPO - Plain Old Python Objects), sin ninguna dependencia de frameworks de
persistencia ni conocimiento del esquema de la base de datos.
En nuestra arquitectura, los Repositorios actúan como los mapeadores externos, con las
siguientes responsabilidades:
Transformar objetos del dominio en registros de la base de datos: Toman una instancia
de una entidad (ej. AdultoMayor) y ejecutan las operaciones INSERT o UPDATE necesarias
en las tablas correspondientes.
Reconstruir objetos del dominio a partir de datos persistidos: Ejecutan consultas
SELECT e hidratan los resultados en instancias de las clases del dominio, listas para ser
utilizadas por la lógica de negocio.
Ejecutar operaciones CRUD de manera transparente, aislando a las capas superiores de los
detalles de conexión y sintaxis SQL.
Desacoplamiento mediante Repositorios:
La implementación del patrón Data Mapper mediante repositorios en SQLAlchemy ofrece
ventajas críticas para el proyecto:
Entidades Puras: Las clases como HogarGerontologico, AdultoMayor o BitacoraDiaria
contienen únicamente atributos, métodos de comportamiento del dominio y validaciones
básicas. No incluyen ninguna lógica de persistencia, lo que las hace más fáciles de entender,
probar y modificar.
Capa de Persistencia Intercambiable: Si en el futuro se decidiera migrar de PostgreSQL a
otro sistema gestor de base de datos, o incluso a un origen de datos no relacional, solo sería
necesario modificar la implementación de los repositorios. Las entidades del dominio y la
lógica de negocio permanecerían inalteradas.
Facilidad de Pruebas Unitarias: Las entidades pueden ser instanciadas y probadas de forma
aislada, sin necesidad de una conexión real a la base de datos. Para probar la lógica de

negocio en los servicios, se pueden utilizar repositorios "mock" que simulen el
comportamiento de la capa de persistencia.
Responsabilidad Única: Se respeta el Principio de Responsabilidad Única (SRP). Las
entidades modelan el negocio; los repositorios gestionan la persistencia; los servicios
orquestan la lógica de aplicación. Cada clase tiene una única razón para cambiar.
Componentes del Patrón en el Sistema:
Entidades (Capa de Dominio): Clases Python puras que representan los conceptos del
negocio: AdultoMayor, Personal, HogarGerontologico, Habitacion, BitacoraDiaria, etc.
Contienen atributos, relaciones (ej. AdultoMayor tiene una relación con Habitacion) y lógica
de dominio.
Repositorios (Mapeadores Externos): Clases de Python que utilizan la API de Sesión de
SQLAlchemy para interactuar con PostgreSQL. Cada agregado o entidad principal del
dominio tendrá su propio repositorio (ej. AdultoMayorRepository, HogarRepository). Estos
repositorios ofrecen métodos como obtener_por_id(), listar_por_hogar(), guardar(),
actualizar_diagnostico(), etc.
Servicios (Capa de Aplicación): Clases que contienen la lógica de negocio. Inyectan y
utilizan las interfaces de los repositorios para obtener y persistir datos, pero nunca acceden
directamente a la base de datos. Por ejemplo, ServicioAdmision usará HogarRepository para
verificar cupos y AdultoMayorRepository para registrar al nuevo residente.
DTOs (Data Transfer Objects): Objetos planos utilizados para la comunicación entre la
capa de presentación (interfaz Streamlit) y los servicios, así como para las respuestas de la
API. Desacoplan la estructura de las entidades de dominio de los datos que se envían al
frontend, ocultando campos internos y optimizando la transferencia de información.
2.3 Estrategias de Mapeo
Para modelar la jerarquía de usuarios del sistema, en la que una clase base abstracta Usuario
es extendida por clases concretas como Coordiandor,Enfermero,Medico o Acudiente, se ha
seleccionado la estrategia de mapeo HERENCIA POR CLASE CONCRETA.
2.3.1 Mapeo de Entidades y Relaciones
El modelo de dominio para el hogar gerontológico se caracteriza por un conjunto de
entidades bien diferenciadas que se relacionan mediante asociaciones y composiciones claras.
SQLAlchemy permite mapear estas relaciones de forma declarativa y eficiente, garantizando
la integridad referencial y la consistencia de los datos.

A continuación, se detallan las estrategias de mapeo aplicadas a las relaciones más
significativas del sistema:
Relaciones Uno a Muchos (1:N): Se utilizan para modelar dependencias jerárquicas donde
una entidad "padre" puede estar asociada con múltiples entidades "hijas". Ejemplos:
HogarGerontologico → Habitacion: Un hogar contiene muchas habitaciones. En la
base de datos, la tabla habitacion incluye una clave foránea hogar_id que referencia la
clave primaria de hogar_gerontologico.
AdultoMayor → BitacoraDiaria: Un adulto mayor puede tener múltiples registros en
su bitácora a lo largo del tiempo. La tabla bitacora_diaria contiene una columna
adulto_mayor_id que apunta al registro correspondiente.
HogarGerontologico → Personal: Un hogar emplea a muchos miembros del personal.
La tabla personal incluye la clave foránea hogar_id.
SQLAlchemy gestiona estas relaciones mediante el objeto relationship y la definición
de ForeignKey en la tabla del lado "muchos". La carga de los objetos relacionados
puede ser lazy (perezosa) para optimizar el rendimiento, recuperándolos de la base de
datos solo cuando se accede a ellos.
Relaciones Uno a Uno (1:1): Se aplican cuando una entidad está asociada exclusivamente
con otra. El ejemplo principal en el sistema es la asignación de un AdultoMayor a una
Habitacion. Una habitación puede estar ocupada por un único adulto mayor a la vez, y un
adulto mayor (de categoría A o B) reside en una sola habitación. En SQLAlchemy, esto se
modela con una ForeignKey (ej. habitacion_id en adulto_mayor) y la opción uselist=False en
el relationship. Esta configuración asegura que la relación devuelva un único objeto en lugar
de una lista.
Relaciones Muchos a Muchos (N:M): Aunque no son predominantes en el diseño inicial,
podrían surgir en contextos como la asignación flexible de múltiples enfermeros a múltiples
adultos mayores. Para implementar esta asociación, SQLAlchemy utiliza una tabla de
asociación (o tabla pivote) que contiene pares de claves foráneas. Por ejemplo, una tabla
enfermero_adulto_mayor con columnas enfermero_id y adulto_mayor_id. El ORM se
encarga de gestionar automáticamente las inserciones y consultas en esta tabla intermedia,
simplificando la lógica de negocio.
Integridad Referencial y Restricciones: La base de datos PostgreSQL se configura con
restricciones de clave foránea apropiadas para garantizar la integridad de los datos:
ON DELETE RESTRICT: Impide eliminar un registro padre (ej. un HogarGerontologico) si
existen registros hijos que dependen de él (ej. Habitacion o Personal asociados). Esto
previene la creación de registros huérfanos.

ON UPDATE CASCADE: Si la clave primaria de un registro padre cambiara (un escenario
poco común con identificadores estables), la actualización se propagaría automáticamente a
las claves foráneas de las tablas hijas.
NOT NULL: Se aplica a todas las columnas que representan datos obligatorios, como
nombres, identificaciones o claves foráneas que definen relaciones de pertenencia
imprescindibles.
Además, las operaciones que involucran múltiples entidades y modifican el estado del
sistema (como el proceso de admisión de un adulto mayor) se ejecutarán dentro de
transacciones ACID. Esto asegura que, ante cualquier fallo durante el proceso, la base de
datos revierta a su estado anterior consistente, evitando registros parciales o datos corruptos.
Campo Identidad
Para la identificación única de los registros en cada tabla del sistema, se ha optado por utilizar
identificadores numéricos enteros autoincrementales (INTEGER con la propiedad SERIAL
en PostgreSQL) como claves primarias.
Justificación del uso de Identificadores Enteros Autoincrementales:
Simplicidad y Legibilidad: Los identificadores numéricos secuenciales son intuitivos y
fáciles de leer, recordar y comunicar para los usuarios administrativos y el personal de
soporte. Un ID como 125 es más manejable en comunicaciones verbales o escritas que una
cadena UUID larga y compleja.
Rendimiento Optimizado: En bases de datos relacionales como PostgreSQL, los índices
sobre columnas INTEGER son más compactos y su mantenimiento es más rápido que los
índices sobre columnas de tipo UUID. Esto se traduce en un mejor rendimiento para las
operaciones de búsqueda por clave primaria y para las consultas que involucran JOIN entre
tablas, un aspecto crítico para un sistema que gestionará un volumen creciente de bitácoras y
registros de seguimiento.
Eficiencia en Almacenamiento: Una clave primaria de tipo INTEGER ocupa 4 bytes,
mientras que un UUID ocupa 16 bytes. Esta diferencia de espacio, aunque aparentemente
pequeña por registro, se vuelve significativa al considerar las claves foráneas en múltiples
tablas relacionadas y el historial acumulado a lo largo del tiempo. El uso de INTEGER
reduce el espacio total de almacenamiento y mejora la eficiencia de la memoria caché de la
base de datos.
Adecuación al Volumen de Datos Esperado: Dado que el sistema está diseñado para
gestionar un número limitado de hogares gerontológicos (inicialmente dos, con potencial de
expansión controlada) y un flujo de residentes y personal acotado, el rango de valores

proporcionado por un INTEGER (más de 2 mil millones de registros únicos) es más que
suficiente para toda la vida útil del sistema sin riesgo de desbordamiento.
Estabilidad de la Clave Primaria: Al igual que un UUID, un identificador entero
autoincremental, una vez asignado, nunca debe cambiar durante la vida del registro. Esto
proporciona una clave primaria simple y estable para garantizar la correcta trazabilidad y
consistencia de las relaciones en todo el sistema.
La generación de estos identificadores se delega completamente al motor de la base de datos
mediante el tipo SERIAL de PostgreSQL, lo que garantiza la atomicidad y unicidad de los
valores en entornos concurrentes sin requerir lógica adicional en la aplicación. Las entidades
en Python simplemente tendrán un atributo id de tipo int que será asignado por SQLAlchemy
después de que el registro se inserte por primera vez en la base de datos.
3.3 Modelo Relacional

|     |     |     |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |

4. Diseño básico de interfaz gráfica de usuario
4.1 Mapas de navegación y bocetos visuales IGU
❖  Inicio de sesión
|     |     |     |
| --- | --- | --- |

❖ Recuperar contraseña
❖ Crear Usuario

❖ Eliminar Usuario

|     |     |     |
| --- | --- | --- |

❖  Lista de usuarios

❖  Gestionar Citación
|     |     |     |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |

❖  Registrar Preinscripción

❖  Asignar Categoría De Servicio
|     |     |     |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |

❖  Crear Hogares Gerontológico

❖  Hogar Gerontológico
|     |     |     |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |

❖  Eliminar Hogar Gerontológico

❖  Diagnóstico Inicial
|     |     |     |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |

❖  Recomendaciones de atención

❖  Bitácora diaria
|     |     |     |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |

❖  Hoja de vida

❖  Citación a reunión
|     |     |     |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |

❖  Consultar Seguimiento

❖  Asignar enfermero a adulto mayor
|     |     |     |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |

❖  Consultar asignaciones de enfermeros

❖  Listado Por Categoría
|     |     |     |
| --- | --- | --- |

❖ Reporte De Seguimiento

❖ Lista Adultos Mayores

❖

5. Bibliografia
• Sparx Systems. EA tool setup. [En línea]. Disponible en:
https://sparxsystems.com/enterprise_architect_user_guide/17.1/guide_books/ea_tool_
setup.html. Fecha de consulta: 11 de marzo de 2026.
• Lucidchart. Tutorial — Diagrama de actividades UML. [En línea]. Disponible en:
https://www.lucidchart.com/pages/es/tutorial-diagrama-de-actividades-uml. Fecha de
consulta: 11 de marzo de 2026.
• Northware. Técnicas efectivas para la toma de requerimientos. [En línea]. Disponible
en: https://www.northware.mx/blog/tecnicas-efectivas-para-la-toma-de-
requerimientos/. Fecha de consulta: 11 de marzo de 2026.
• Object Management Group. About UML — UML 2.5.1 Specification. [En línea].
Disponible en: https://www.omg.org/spec/UML/2.5.1/About-UML. Fecha de
consulta: 11 de marzo de 2026.
• GeeksforGeeks. Use Case Diagram — System Design. [En línea]. Disponible en:
https://www.geeksforgeeks.org/system-design/use-case-diagram/. Fecha de consulta:
11 de marzo de 2026.