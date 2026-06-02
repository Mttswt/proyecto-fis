> [!info] Enlaces Relacionados
> 🗂️ **Índice central:** [[Indice_Proyecto]]
> 📝 **Definición del Problema:** [[definicion]]
> 🏗️ **Especificación Estructural:** [[proyecto2]]

Especificación Funcional

Proyecto Semestral 2026-I

Miguel Ángel Jimenez Suspes (20231020027)

Matthew Stev Toro Mondragon (20231020077)

Fundamentos de Ingeniería de Software

Henry Alberto Diosa

Tabla de contenidos

1.

Introducción ....................................................................................................................... 2

2.  Producto a obtener ............................................................................................................. 3

3. Requerimientos específicos de interfaces .............................................................................. 4

3.1 Interfaces de usuario......................................................................................................... 4

3.2 Interfaces de hardware ..................................................................................................... 4

3.3 Interfaces de software....................................................................................................... 4

3.4 Protocolos de comunicación............................................................................................. 4

3.5 Requerimientos de persistencia ........................................................................................ 5

4. Caracterización del producto de software .............................................................................. 5

4.1 Requerimientos funcionales ............................................................................................. 6

4.1.1. Módulo Gestión de acceso ........................................................................................ 7

4.1.2. Módulo Usuarios y autenticación ............................................................................. 7

4.1.3. Módulo Preinscripción y admisiones ....................................................................... 8

4.1.4. Módulo Reportes y consultas ................................................................................... 8

4.1.5. Módulo Gestión hogares ........................................................................................... 9

4.1.6. Módulo seguimiento y bitácoras............................................................................... 9

4.1.7. Módulo asignación personal ................................................................................... 10

4.1.8. Módulo Promoción y contenidos ............................................................................ 11

5. Casos de uso y diagramas de actividad ................................................................................ 11

5.1. Módulo Gestión de acceso ......................................................................................... 11

5.2. Módulo de Gestión de Hogares ..................................................................................... 16

5.3 Módulo Preinscripción y admisiones ............................................................................. 21

5.4. Módulo de Seguimiento y Bitácoras ............................................................................. 27

5.5. Módulo de Reportes y consultas ................................................................................... 28

5.6. Módulo de Asignación de Personal ............................................................................... 28

5.7. Módulo de Usuarios y Autenticación ............................................................................ 28

6. Matriz de cobertura .............................................................................................................. 28

8. Mockups y mapa de navegación .......................................................................................... 28

8.1. Menu de ingreso: ........................................................................................................... 28

8.2. Inicio de sesión: ............................................................................................................. 28

8.3. Registrar preinscripción: ............................................................................................... 28

8.4. Coordinador de la entidad: ............................................................................................ 28

8.5. Coordinador del hogar:.................................................................................................. 28

9. Requerimientos no funcionales a implementar .................................................................... 28

10. Propuesta de negociación ................................................................................................... 28

11. Bibliografia ........................................................................................................................ 28

1. Introducción

El  propósito  de  este  documento  de  Especificación  Funcional  es  definir  de  manera  clara  y
detallada los requisitos del sistema de información destinado a la gestión integral de hogares
gerontológicos  administrados  por  una  entidad  pública.  La  necesidad  de  sistematizar  esta
operación  surge  de  la  complejidad  inherente  a  la  prestación  de  servicios  especializados  de
cuidado para adultos mayores, considerando que la entidad administra actualmente un hogar
en funcionamiento y tiene proyectada la inauguración de un segundo en el corto plazo. Cada
hogar  ofrece  tres  categorías  de  servicio:  personas  que  requieren  habitación  independiente,
personas que pueden compartir habitación con otro adulto mayor, y personas que únicamente
asisten  durante  el  día,  con  una  capacidad  máxima  de  diez  usuarios  simultáneos  en  esta
modalidad.

El  documento  se  encuentra  organizado  de  tal  manera  que  en  los  apartados  posteriores  se
presentan  los  requerimientos  específicos  de  interfaces  y  la  caracterización  del  producto  de
software, profundizando en la sección dedicada a los requerimientos funcionales, los casos de
uso y los diagramas de actividades, pues allí se explica con mayor detalle cómo se espera que
se lleven a cabo cada una de las tareas del sistema. Gracias a esta estructura, se puede visualizar
paso a paso cómo se planea desarrollar las funcionalidades solicitadas en el enunciado inicial
y  cómo  se  dará  respuesta  a  cada  una  de  ellas.  Además,  con  esta  especificación  se  busca
garantizar  que  el  desarrollo  e  implementación  se  realicen  de  forma  ordenada  y  coherente,
evitando  confusiones  y  asegurando  que  la  aplicación  final  cumpla  con  las  expectativas  y
necesidades de la entidad.

2. Producto a obtener

 El  producto  a  obtener  es  un  prototipo  de  aplicación  de  gestión  integral  para  hogares
gerontológicos,  desarrollado  como  aplicación  web.  Su  objetivo  central  es  digitalizar  y
centralizar  los  procesos  operativos,  clínicos  y  administrativos  de  la  entidad  pública
administradora, comenzando con los dos hogares actualmente identificados y proyectado para
escalar a nuevos hogares conforme la entidad los habilite.

Desde el punto de vista de la infraestructura gestionada, el sistema deberá modelar cada hogar
con su dotación mínima: diez habitaciones para una sola persona, diez habitaciones para dos
personas,  salas  de  juegos,  biblioteca,  comedor,  espacios  deportivos  y  zonas  verdes.  Esta
configuración constituye  la plantilla base que se replicará automáticamente cada vez que se
registre un nuevo hogar en el sistema.

En cuanto a la gestión de personas, el sistema administrará dos grandes grupos de usuarios: el
personal del hogar y los adultos mayores junto  con sus responsables. El personal  incluye al
coordinador  del  hogar,  quince  enfermeros,  dos  cocineros,  tres  médicos  generales,  dos
trabajadores sociales, dos psicólogos, cinco recreacionistas, personal de servicios generales y
un coordinador logístico. Los adultos mayores podrán pertenecer a alguna de las tres categorías
de  servicio  ya  enunciadas,  y  sus  responsables  podrán  consultar  el  estado  de  seguimiento  a
través del sistema.

Las  funcionalidades  principales  del  producto  contemplarán:  el  formulario  de  preinscripción
con  notificación  automática  a  coordinación,  la  gestión  del  proceso  de  admisión  mediante
entrevista y diagnóstico inicial, la asignación de habitaciones o cupos según disponibilidad y
categoría, el módulo de seguimiento clínico y psicosocial con bitácora diaria, la generación de
reportes  consolidados  en  PDF,  el  control  de  asistencia  para  usuarios  de  estancia  diurna,  la
gestión de citaciones, el módulo de hoja de vida del adulto mayor y el control de acceso por
roles.  Al  ser  un  prototipo  académico,  algunas  funcionalidades  de  alta  complejidad  técnica
podrán ser negociadas según se describe en la sección correspondiente.

 3. Requerimientos específicos de interfaces

3.1 Interfaces de usuario

La aplicación contará con una interfaz web desarrollada con la librería Streamlit de Python, la
cual  permite  construir  interfaces  interactivas  accesibles  desde  cualquier  navegador  web
moderno sin requerir instalación adicional por parte del usuario. La navegación del sistema se
realizará mediante un menú lateral que desplegará las opciones correspondientes según el rol
del usuario autenticado. Se priorizará la simplicidad de uso y la facilidad de interacción para
los  usuarios  finales,  quienes  realizarán  todas  las  operaciones  a  través  de  formularios,  tablas
interactivas  y  botones  de  acción  organizados  en  páginas  independientes  por  módulo.  Los
mensajes de error se mostrarán en color rojo y los mensajes de confirmación en color verde,
garantizando retroalimentación visual consistente en toda la aplicación.

3.2 Interfaces de hardware

La aplicación requiere únicamente un equipo personal con acceso a un navegador web moderno
(Google Chrome, Mozilla Firefox o Microsoft Edge en sus versiones actuales) y conexión a la
red  local  donde  se  encuentre  desplegada  la  aplicación.  No  se  requiere  integración  con
dispositivos externos adicionales.

3.3 Interfaces de software

•  Lenguaje de programación: Python 3.10 o superior.
•  Librería principal de interfaz: Streamlit.
•  Base de datos: PostgreSQL versión 14 o superior.
•  Dependencias  adicionales:  psycopg2  o  SQLAlchemy  como  controlador  para  la

comunicación entre Python y PostgreSQL.

•

3.4 Protocolos de comunicación

La aplicación Streamlit se ejecutará en un servidor local y será accesible desde el navegador
mediante  el  protocolo  HTTP,  usando  por  defecto  el  puerto  8501.  La  comunicación  entre  la
interfaz web y el servidor de la aplicación se gestiona internamente por Streamlit sin requerir
configuración adicional. La interacción con la base de datos PostgreSQL se realizará mediante
conexión directa a través de socket TCP/IP usando el puerto 5432 por defecto, gestionada por
el controlador psycopg2 o SQLAlchemy desde el backend de la aplicación.

3.5 Requerimientos de persistencia

La información persistente se almacenará en PostgreSQL 14 o superior mediante el controlador
psycopg2  o  SQLAlchemy.  Se  registrarán  las  entidades  principales:  Hogar  Gerontológico,
Adulto Mayor (incluida su hoja de vida), Responsable, Aspirante, Personal (con su respectivo
rol), Categoría de Servicio, Habitación, Asignación de Habitación, Diagnóstico Psicosocial y
Clínico, Plan de Atención, Plan de Medicamentos y Terapias, Recomendaciones de Atención,
Bitácora Diaria y Registro de Asistencia Diurna.

Se  garantizará  la  integridad  referencial  mediante  claves  primarias,  claves  foráneas  y
restricciones  NOT  NULL  en  todos  los  campos  obligatorios.  Se  aplicarán  restricciones  de
unicidad  en  campos  críticos  como  el  número  de  identificación  del  adulto  mayor,  el  correo
electrónico de usuarios y responsables, y el código  de habitación dentro de  cada hogar. Las
operaciones  compuestas  críticas,  como  el  registro  de  admisión  de  un  adulto  mayor,  se
ejecutarán  dentro  de  transacciones  para  asegurar  consistencia.  Por  defecto  no  se  eliminarán
registros  históricos  como  bitácoras  diarias  ni  diagnósticos,  únicamente  se  marcarán  como
inactivos cuando corresponda.

4. Caracterización del producto de software

4.1 Requerimientos funcionales

Los requerimientos funcionales se organizaron en distintos módulos según funcionalidades que
tendrá el sistema, cada uno con sus respectivos requerimientos, se obtuvieron un total de  40
requerimientos funcionales.

4.1.1. Módulo Gestión de acceso

Código

Título

Descripción

Prioridad

RF-GA-
01

Iniciar aplicación

Iniciar el sistema al ejecutar el programa.

Alta

RF-GA-
02

Inicio de sesión con
credenciales únicas

Se permite a los usuarios iniciar sesión validando
su usuario y contraseña y asociarlos con un rol
definido en el sistema.

RF-GA-
03

RF-GA-
04

RF-GA-
05

Controlar permisos
de rol

Habilitar únicamente las funcionalidades
correspondientes al rol del usuario autenticado.

Cerrar sesión

Permitir al usuario cerrar sesión finalizando su
acceso en la aplicación.

Restaurar
contraseña

Se crea una nueva contraseña para reemplazar la
anterior contraseña del usuario que la olvidó.

Alta

Alta

Alta

Alta

4.1.2. Módulo Usuarios y autenticación

Código

Título

Descripción

Prioridad

RF-UA-
01

Crear usuario del
sistema

La dirección crea nuevos usuarios definiendo
nombre, correo, contraseña temporal y rol (lista
predefinida). El sistema envía las credenciales al
nuevo usuario por correo.

Alta

RF-UA-
02

Modificar usuario
del sistema

La dirección modifica datos y/o rol de un usuario
existente en el sistema.

Alta

RF-UA-
03

Eliminar usuario
del sistema

La dirección da de baja (eliminación lógica) a un
usuario, revocando su acceso al sistema sin
eliminar sus registros históricos.

RF-UA-
04

Consultar usuarios
del sistema

La dirección consulta la lista de usuarios
registrados con sus datos y roles asignados.

RF-UA-
05

Autenticar usuario
por rol

El sistema autentica a cada usuario con correo y
contraseña, habilitando únicamente las opciones
correspondientes a su rol.

Alta

Alta

Alta

4.1.3. Módulo Preinscripción y admisiones

Código

Título

Descripción

Prioridad

RF-PA-
01

Registrar
preinscripción de
adultos mayores

RF-PA-
02

Notificar a la
coordinación sobre
aspirantes nuevos

RF-PA-
03

Gestionar
citaciones de
admisión

RF-PA-
04

Asignar adulto
mayor a categoría
de servicio

Formulario web con datos del responsable
(nombres, apellidos, contacto) y perfil básico del
adulto mayor (nombres, apellidos, edad,
categoría de servicio solicitada). Al enviar
genera notificación automática a coordinación.

El sistema notifica automáticamente a la
coordinación de la entidad (vía SMS y/o correo
electrónico) sobre nuevas preinscripciones
recibidas.

La coordinación programa y registra citaciones
para entrevista con los responsables y visita
diagnóstica por parte del trabajador social y
médico. El sistema notifica al responsable la
fecha y hora de la cita.

Tras entrevista y diagnóstico, permite asignar al
adulto mayor aceptado a una categoría (A, B o
C) y habitación disponible. El sistema actualiza
los cupos disponibles.

Alta

Alta

Alta

Alta

4.1.4. Módulo Reportes y consultas

Código

Título

Descripción

Prioridad

RF-RC-
01

Generar listado de
adulto mayor por
categoría (PDF)

RF-RC-
02

Consultar registros
de seguimiento

Genera un listado de adultos mayores
clasificados por categoría de servicio (A, B, C)
con su ubicación dentro del hogar. Permite
descarga en formato PDF.

El personal profesional y el coordinador del
hogar consultan los registros de seguimiento de
los adultos mayores bajo su responsabilidad.

RF-RC-
03

Generar reporte
imprimible de
seguimiento (PDF)

Genera un reporte consolidado de los registros de
seguimiento de un adulto mayor en formato PDF
imprimible.

Alta

Alta

Alta

RF-RC-
04

RF-RC-
05

RF-RC-
06

Consulta de
seguimiento por
responsable del
adulto mayor

El responsable del adulto mayor puede consultar,
con credenciales de acceso externo, los datos de
seguimiento del adulto mayor a su cargo.

Generar PDF
descargable para el
responsable

El responsable del AM puede descargar un PDF
con los datos de seguimiento del adulto mayor
bajo su responsabilidad.

Alta

Alta

Generar reporte
consolidado de hoja
de vida en PDF

Genera el reporte consolidado de la hoja de vida
del AM, integrando datos de ingreso y
seguimiento acumulado, en formato PDF.

Media

4.1.5. Módulo Gestión hogares

Código

Título

Descripción

Prioridad

RF-GH-
01

Crear hogar
gerontológico

RF-GH-
02

Configurar
infraestructura del
hogar

RF-GH-
03

Consultar hogares
gerontológicos

Permite registrar un nuevo hogar gerontológico
con nombre, dirección y capacidad, configurando
su infraestructura estándar (10 hab. individuales,
10 hab. dobles, salas, comedor, espacios
deportivos y verdes).

Permite ajustar la infraestructura de un hogar
existente y habilitar las categorías de servicio A
(individual), B (compartida) y C (adulto mayor
de día, máx. 10).

Permite consultar la lista de hogares
gerontológicos a nombre de la entidad, así como
su estado actual (cantidad de adultos mayores en
la ubicación).

Alta

Alta

Alta

RF-GH-
04

Eliminar hogar
gerontológico

Permite eliminar hogares gerontológicos.

Alta

4.1.6. Módulo seguimiento y bitácoras

Código

Título

Descripción

Prioridad

RF-SB-
01

Registrar
diagnóstico
psicosocial y clínico
inicial

El trabajador social y/o médico registra el
diagnóstico psicosocial y clínico inicial del
adulto mayor al momento de su ingreso al hogar.

Alta

Alta

Alta

Alta

Alta

Alta

RF-SB-
02

Registrar plan de
atención

Permite crear y actualizar el plan de atención
individualizado para cada adulto mayor con las
directrices de cuidado establecidas por el equipo
profesional.

RF-SB-
03

RF-SB-
04

Registrar plan de
medicamentos y
terapias

Permite registrar y actualizar el plan de
administración de medicamentos y terapias
(dosis, frecuencia, observaciones) para cada
adulto mayor.

Registrar
recomendaciones
de atención

Permite registrar recomendaciones particulares
de atención para un adulto mayor específico,
visibles al personal de cuidado autorizado.

Media

RF-SB-
05

Registrar bitácora
diaria de eventos

Permite al personal registrar eventos relevantes
del día para uno o varios adultos mayores en la
bitácora compartida del hogar gerontológico.

RF-SB-
06

Gestionar bitácora
individual por
enfermero

RF-SB-
07

Gestionar hoja de
vida del adulto
mayor

RF-SB-
08

Chequeo de
asistencia
Categoría C
(adultos de día)

RF-SB-
09

Gestionar
citaciones a
reuniones

Cada enfermero(a) puede crear, consultar y
actualizar su propia bitácora diaria para cada
adulto mayor que tiene asignado bajo su
responsabilidad.

La coordinación registra y actualiza la hoja de
vida del AM: estado de salud, alergias y
capacidades de aprendizaje al ingreso. Se
consolida con los datos de seguimiento
posteriores.

El personal de enfermería registra la entrada y
salida diaria de los adultos mayores de la
categoría C (sólo durante el día).

Media

La coordinación del hogar crea convocatorias
masivas (todo el personal) o selectivas (usuarios
específicos) para reuniones, indicando fecha,
hora, lugar y asunto. El sistema notifica a los
destinatarios.

Media

4.1.7. Módulo asignación personal

Código

Título

Descripción

Prioridad

RF-AP-
01

Asignar enfermeros
a adultos mayores

RF-AP-
02

Consultar
asignación de
enfermeros

El coordinador del hogar asigna uno o más
enfermeros a grupos de adultos mayores por
categoría de servicio, registrando la asignación
con fecha de vigencia.

El coordinador del hogar consulta la asignación
actual de enfermeros a adultos mayores,
visualizando la distribución por categoría de
servicio.

Media

Media

RF-AP-
03

Modificar
asignación de
enfermeros

El coordinador del hogar es capaz de reasignar a
los enfermeros.

Media

4.1.8. Módulo Promoción y contenidos

Código

Título

Descripción

RF-PC-
01

Gestionar
contenidos
institucionales web

Gestor de contenidos para que la coordinación
publique información institucional (misión,
servicios, noticias) en el sitio web del hogar
gerontológico.

Prioridad

Media

RF-PC-
02

Promocionar en
redes sociales

Permite publicar y compartir contenidos del
hogar en redes sociales (Facebook, Instagram, X)
directamente desde la plataforma web.

Media

5. Casos de uso y diagramas de actividad

5.1. Módulo Gestión de acceso

CU-1.1 Iniciar aplicación

Actores

Tipo

Usuario

Primario

Precondiciones

La aplicación está instalada y es ejecutada por el usuario.

Postcondiciones

El sistema despliega la interfaz gráfica principal con las opciones
disponibles.

Referencias Cruzadas,
Req.

RF-GA-01

Descripción

El sistema inicia y muestra la interfaz principal al usuario, permitiéndole
acceder a las opciones de inicio de sesión o preinscripción.

CU-1.2 Iniciar sesión

Actores

Tipo

Precondiciones

Postcondiciones

Referencias Cruzadas,
Req.

Descripción

Usuario

Primario

El usuario ha ejecutado la aplicación y dispone de credenciales registradas
en el sistema.

El usuario accede al sistema con las funcionalidades habilitadas según su
rol.

CU-1.1 Iniciar aplicación, CU-7.1 Autenticar usuario RF-GA-02

El usuario ingresa su correo electrónico y contraseña. El sistema valida las
credenciales y, si son correctas, habilita las opciones correspondientes al
rol asignado.

CU-1.3 Recuperar contraseña

Actores

Tipo

Precondiciones

Postcondiciones

Usuario

Opcional

El usuario ha iniciado la aplicación y selecciona la opción de recuperar
contraseña en la pantalla de inicio de sesión.

Se genera una nueva contraseña y se envía al correo electrónico del
usuario.

Referencias Cruzadas,
Req.

RF-GA-05

Descripción

El usuario ingresa el correo asociado a su cuenta. El sistema genera una
nueva contraseña aleatoria, la registra en la base de datos y la envía por
correo al usuario.

CU-1.4 Cerrar sesión

Actores

Tipo

Usuario

Opcional

Precondiciones

El usuario ha iniciado sesión en el sistema.

Postcondiciones

La sesión del usuario es finalizada y el sistema regresa a la pantalla de
inicio.

Referencias Cruzadas,
Req.

RF-GA-04

Descripción

El usuario selecciona la opción de cerrar sesión. El sistema invalida la
sesión activa y redirige al usuario a la pantalla principal de inicio.

5.2. Módulo de Gestión de Hogares

CU-2.1 Crear hogar gerontológico

Actores

Tipo

Coord. entidad

Primario

Precondiciones

El coordinador de la entidad ha iniciado sesión con su rol correspondiente.

Postcondiciones

El nuevo hogar gerontológico queda registrado en el sistema con su
infraestructura estándar configurada.

Referencias Cruzadas,
Req.

RF-GH-01

Descripción

El coordinador de la entidad ingresa los datos del nuevo hogar (nombre,
dirección, capacidad). El sistema registra el hogar y configura
automáticamente su infraestructura estándar: 10 habitaciones individuales,
10 habitaciones dobles, salas de juego, biblioteca, comedor y espacios
deportivos y verdes.

CU-2.2 Consultar hogares gerontológicos

Actores

Tipo

Coord. entidad, Coord. hogar

Primario

Precondiciones

El usuario ha iniciado sesión y accede al módulo de gestión de hogares.

Postcondiciones

Se visualiza la lista de hogares gerontológicos con su estado actual.

Referencias Cruzadas,
Req.

RF-GH-03

Descripción

El sistema muestra la lista de hogares gerontológicos registrados a nombre
de la entidad, incluyendo el nombre, dirección, capacidad total y la
cantidad actual de adultos mayores por categoría de servicio.

CU-2.3 Modificar hogar gerontológico

Actores

Tipo

Precondiciones

Postcondiciones

Coord. entidad

Opcional

El coordinador ha consultado la lista de hogares (CU-2.2) y selecciona un
hogar para modificar.

La infraestructura o datos del hogar seleccionado quedan actualizados en
el sistema.

Referencias Cruzadas,
Req.

RF-GH-02

Descripción

El coordinador selecciona un hogar existente y ajusta su infraestructura o
habilita y deshabilita las categorías de servicio A (individual), B
(compartida) y C (adulto mayor de día, máx. 10 cupos).

CU-2.4 Eliminar hogar gerontológico

Actores

Tipo

Precondiciones

Coord. entidad

Opcional

El coordinador ha consultado la lista de hogares (CU-2.2) y selecciona un
hogar para eliminar.

Postcondiciones

El hogar es marcado como inactivo en el sistema.

Referencias Cruzadas,
Req.

RF-GH-04

Descripción

El coordinador de la entidad selecciona un hogar de la lista y solicita su
eliminación. El sistema realiza una eliminación lógica, marcando el hogar
como inactivo sin borrar los registros históricos asociados.

CU-2.5 Administrar hogares gerontológicos

Actores

Tipo

Coord. entidad

Primario

Precondiciones

El coordinador de la entidad ha iniciado sesión con su rol correspondiente.

Postcondiciones

El coordinador accede a las opciones de gestión de hogares del sistema.

Referencias Cruzadas,
Req.

Descripción

RF-GH-01, RF-GH-02, RF-GH-03, RF-GH-04

El coordinador de la entidad accede al módulo de gestión de hogares,
desde donde puede crear, consultar, modificar y eliminar hogares
gerontológicos. Este caso de uso agrupa las operaciones CRUD sobre los
hogares y las delega a los casos de uso específicos correspondientes.

5.3 Módulo Preinscripción y admisiones

CU-3.1 Registrar preinscripción

Actores

Tipo

Precondiciones

Responsable de un adulto mayor

Primario

El responsable accede al formulario de preinscripción desde la pantalla
inicial de la aplicación.

Postcondiciones

La preinscripción queda registrada en el sistema y se notifica
automáticamente a la coordinación.

Referencias Cruzadas,
Req.

Descripción

RF-PA-01, RF-PA-02

El responsable diligencia el formulario web con sus datos personales
(nombres, apellidos, contacto) y el perfil básico del adulto mayor
(nombres, apellidos, edad, categoría de servicio solicitada). Al enviar, el
sistema registra la preinscripción y genera una notificación automática a
la coordinación.

CU-3.2 Registrar más de una preinscripción

Actores

Tipo

Precondiciones

Postcondiciones

Responsable de un adulto mayor

Secundario

El responsable ha diligenciado el formulario principal de preinscripción
(CU-3.1) y desea registrar otro adulto mayor.

Se generan registros independientes para cada adulto mayor preinscrito
por el mismo responsable.

Referencias Cruzadas,
Req.

RF-PA-01

Descripción

Desde el formulario de preinscripción, el responsable puede agregar otro
adulto mayor. El sistema habilita un nuevo formulario con los mismos
campos del perfil del adulto mayor, generando un registro independiente
para cada uno al enviar.

CU-3.3 Consultar lista de preinscripciones

Actores

Tipo

Precondiciones

Postcondiciones

Coord. hogar

Primario

El coordinador del hogar ha accedido al módulo de preinscripción (CU-
3.4)

Se visualiza la lista de aspirantes ordenada por fecha de envío del
formulario

Referencias Cruzadas,
Req.

RF-PA-01

Descripción

El coordinador accede a la lista de preinscripciones recibidas,
visualizando los datos básicos del responsable y del adulto mayor
aspirante, ordenados según la fecha de envío del formulario.

CU-3.4 Administrar preinscripciones

Actores

Tipo

Coord. hogar

Primario

Precondiciones

El coordinador del hogar ha iniciado sesión en el sistema.

Postcondiciones

El coordinador accede a las funcionalidades de gestión de
preinscripciones.

Referencias Cruzadas,
Req.

Descripción

RF-PA-01, RF-PA-02, RF-PA-03, RF-PA-04

El coordinador del hogar accede al módulo de preinscripción y
admisiones, desde donde puede consultar la lista de preinscripciones
recibidas, gestionar citaciones de admisión y aceptar adultos mayores a
categorías de servicio. Este caso de uso actúa como punto de entrada a las
operaciones del módulo.

CU-3.5 Gestionar citación de admisión

Actores

Tipo

Precondiciones

Postcondiciones

Coord. hogar

Primario

El coordinador ha consultado la lista de preinscripciones (CU-3.3) y desea
programar una citación.

La citación queda registrada y el responsable del adulto mayor es
notificado con la fecha y hora de la cita.

Referencias Cruzadas,
Req.

RF-PA-03

Descripción

El coordinador programa y registra la citación para entrevista con el
responsable y la visita diagnóstica por parte del trabajador social y el
médico. El sistema notifica al responsable la fecha, hora y lugar de la cita.

CU-3.6 Aceptar adulto mayor a categoría de servicio

Actores

Tipo

Coord. hogar

Primario

Precondiciones

Se ha realizado la entrevista y el diagnóstico del aspirante.

Postcondiciones

El adulto mayor queda asignado a una categoría de servicio y habitación,
y el sistema actualiza los cupos disponibles.

Referencias Cruzadas,
Req.

RF-PA-04

Descripción

Tras la entrevista y el diagnóstico, el coordinador selecciona al adulto
mayor aceptado y le asigna una categoría de servicio (A, B o C) y una
habitación disponible. El sistema actualiza automáticamente los cupos
disponibles del hogar.

5.4. Módulo de Seguimiento y Bitácoras

CU-4.1 Registrar diagnóstico inicial

Actores

Tipo

Precondiciones

Postcondiciones

Trabajador social, Médico

Primario

El adulto mayor ha sido aceptado y asignado a una categoría de servicio
en el hogar.

El diagnóstico psicosocial y clínico inicial del adulto mayor queda
registrado en el sistema.

Referencias Cruzadas,
Req.

RF-SB-01

Descripción

El trabajador social y/o médico registra el diagnóstico psicosocial y
clínico inicial del adulto mayor al momento de su ingreso al hogar,
incluyendo antecedentes de salud, condición actual y observaciones
relevantes para el cuidado.

CU-4.2 Gestionar plan de atención

Actores

Tipo

Médico, Trabajador social

Primario

Precondiciones

El adulto mayor tiene diagnóstico inicial registrado en el sistema.

Postcondiciones

El plan de atención individualizado queda creado o actualizado en el
sistema.

Referencias Cruzadas,
Req.

RF-SB-02

Descripción

El equipo profesional crea y actualiza el plan de atención individualizado
para el adulto mayor, estableciendo las directrices de cuidado, actividades
y responsabilidades del personal a cargo.

CU-4.3 Gestionar plan de medicamentos

Actores

Médico

Tipo

Primario

Precondiciones

El adulto mayor tiene historial clínico registrado en el sistema.

Postcondiciones

El plan de medicamentos y terapias queda registrado o actualizado.

Referencias Cruzadas,
Req.

RF-SB-03

Descripción

El médico registra y actualiza el plan de administración de medicamentos
y terapias del adulto mayor, especificando nombres de medicamentos o
terapias, dosis, frecuencia y observaciones particulares.

CU-4.4 Registrar bitácora diaria

Actores

Tipo

Precondiciones

Postcondiciones

Referencias Cruzadas,
Req.

Descripción

Enfermero(a)

Primario

El enfermero ha iniciado sesión y tiene adultos mayores asignados bajo su
responsabilidad.

Los eventos del día quedan registrados en la bitácora del adulto mayor
correspondiente.

RF-SB-05, RF-SB-06

El enfermero registra en su bitácora individual los eventos relevantes del
día para cada adulto mayor a su cargo, incluyendo observaciones de salud,
comportamiento y novedades. El personal también puede registrar eventos
en la bitácora compartida del hogar.

CU-4.5 Chequeo de asistencia Cat. C

Actores

Tipo

Enfermero(a)

Primario

Precondiciones

Los adultos mayores de la categoría C (solo diurnos) han llegado al hogar.

Postcondiciones

La entrada y salida diaria de los adultos mayores de categoría C queda
registrada en el sistema.

Referencias Cruzadas,
Req.

RF-SB-08

Descripción

El personal de enfermería registra la entrada y la salida diaria de los
adultos mayores de la categoría C (asistencia solo durante el día),
llevando el control de asistencia y horario de permanencia en el hogar.

CU-4.6 Administrar hoja de vida del adulto mayor

Actores

Tipo

Coord. hogar, Médico, Trabajador social

Primario

Precondiciones

El adulto mayor ha sido admitido al hogar.

Postcondiciones

La hoja de vida del adulto mayor queda creada o actualizada con la
información de ingreso.

Referencias Cruzadas,
Req.

RF-SB-07

Descripción

El coordinador del hogar accede al módulo de administración de hojas de
vida, que agrupa las funciones de creación, actualización y solicitud de
modificación de la hoja de vida del adulto mayor. Desde aquí se delega a
los casos de uso CU-4.7 y CU-4.8.

CU-4.7 Solicitar modificación a la hoja de vida del adulto mayor

Actores

Tipo

Precondiciones

Postcondiciones

Responsable de un adulto mayor

Opcional

El responsable ha iniciado sesión y accede a la hoja de vida del adulto
mayor a su cargo.

La solicitud de modificación queda registrada y el coordinador es
notificado.

Referencias Cruzadas,
Req.

RF-SB-07

Descripción

El responsable del adulto mayor puede solicitar a la coordinación la
modificación de los datos de la hoja de vida. El sistema registra la
solicitud y genera una notificación al coordinador del hogar para su
revisión y aprobación. Solo el médico puede acceder directamente a esta
opción desde la administración de hojas de vida.

CU-4.8 Gestionar recomendaciones de atención

Actores

Tipo

Médico, Trabajador social

Primario

Precondiciones

El adulto mayor cuenta con diagnóstico y plan de atención registrados.

Postcondiciones

Las recomendaciones quedan registradas y son visibles para el personal de
cuidado autorizado.

Referencias Cruzadas,
Req.

RF-SB-04

Descripción

La coordinación registra y actualiza la hoja de vida del adulto mayor con
datos sobre su estado de salud, alergias y capacidades de aprendizaje al
momento del ingreso. Esta información se consolida posteriormente con
los datos de seguimiento acumulado.

CU-4.9 Gestionar citación a reunión

Actores

Tipo

Precondiciones

Coord. hogar

Primario

El coordinador del hogar ha iniciado sesión y accede a la funcionalidad de
seguimiento y bitácoras.

Postcondiciones

La citación a reunión queda registrada y los destinatarios son notificados.

Referencias Cruzadas,
Req.

Descripción

RF-SB-09, RF-CM-01, RF-CM-02

El coordinador del hogar crea convocatorias masivas (dirigidas a todo el
personal) o selectivas (dirigidas a usuarios específicos) para reuniones,

indicando fecha, hora, lugar y asunto. El sistema notifica automáticamente
a los destinatarios y, en caso de reuniones con acudientes, también les
envía la notificación correspondiente.

5.5. Módulo de Reportes y consultas

CU-5.1 Consultar registros de seguimiento

Actores

Personal profesional, Coord. hogar

Tipo

Primario

Precondiciones

El usuario ha iniciado sesión y accede al módulo de reportes y consultas.

Postcondiciones

Se visualizan los registros de seguimiento del adulto mayor seleccionado.

Referencias Cruzadas,
Req.

RF-RC-02

Descripción

El personal profesional y el coordinador del hogar pueden consultar los
registros de seguimiento (diagnósticos, planes de atención, bitácoras) de
los adultos mayores bajo su responsabilidad.

CU-5.2 Generar reporte PDF de seguimiento

Actores

Tipo

Personal profesional, Coord. hogar

Primario

Precondiciones

Existen registros de seguimiento para el adulto mayor seleccionado.

Postcondiciones

Se genera y descarga un archivo PDF con el reporte consolidado de
seguimiento del adulto mayor.

Referencias Cruzadas,
Req.

RF-RC-03

Descripción

El sistema genera un reporte consolidado en formato PDF imprimible con
todos los registros de seguimiento del adulto mayor seleccionado,
incluyendo diagnósticos, planes de atención, bitácoras y
recomendaciones.

CU-5.3 Consultar datos de seguimiento (responsable)

Actores

Tipo

Responsable de un adulto mayor

Primario

Precondiciones

El responsable ha iniciado sesión con sus credenciales de acceso externo.

Postcondiciones

El responsable visualiza los datos de seguimiento del adulto mayor a su
cargo.

Referencias Cruzadas,
Req.

RF-RC-04

Descripción

El responsable del adulto mayor puede consultar, mediante sus
credenciales de acceso externo, los registros de seguimiento del adulto
mayor bajo su responsabilidad, con la información que la coordinación
haya habilitado para visualización externa.

CU-5.4 Generar listado de adultos mayores por categoría

Actores

Tipo

Precondiciones

Coord. hogar, Coord. entidad

Primario

Existen adultos mayores registrados y asignados a categorías de servicio
en el hogar.

Postcondiciones

Se genera y descarga un listado en formato PDF clasificado por categoría
de servicio.

Referencias Cruzadas,
Req.

RF-RC-01

Descripción

El sistema genera un listado de adultos mayores clasificados por categoría
de servicio (A, B, C) con su ubicación dentro del hogar. El listado puede
descargarse en formato PDF.

CU-5.5 Generar hoja de vida consolidada en PDF

Actores

Tipo

Coord. hogar, Coord. entidad

Primario

Precondiciones

El adulto mayor tiene hoja de vida y registros de seguimiento acumulados.

Postcondiciones

Se genera y descarga el reporte consolidado de la hoja de vida del adulto
mayor en formato PDF.

Referencias Cruzadas,
Req.

RF-RC-06

Descripción

El sistema genera el reporte consolidado de la hoja de vida del adulto
mayor, integrando los datos de ingreso y todo el seguimiento acumulado a
la fecha, en formato PDF descargable.

CU-5.6 Descargar datos de seguimiento (responsable)

Actores

Tipo

Precondiciones

Postcondiciones

Responsable de un adulto mayor

Secundario

El responsable ha consultado los datos de seguimiento del adulto mayor a
su cargo.

El responsable descarga un PDF con los datos de seguimiento del adulto
mayor.

Referencias Cruzadas,
Req.

RF-RC-05

Descripción

El responsable del adulto mayor puede descargar en formato PDF los
datos de seguimiento del adulto mayor bajo su responsabilidad, para su
consulta fuera de la plataforma.

5.6. Módulo de Asignación de Personal

CU-6.1 Consultar enfermeros

Actores

Tipo

Precondiciones

Coord. hogar

Primario

El coordinador del hogar ha iniciado sesión y accede al módulo de
asignación de personal.

Postcondiciones

Se visualiza la lista de enfermeros disponibles y sus asignaciones actuales.

Referencias Cruzadas,
Req.

RF-AP-02

Descripción

El coordinador del hogar consulta la lista de enfermeros registrados en el
sistema, visualizando su distribución actual por categoría de servicio y los
adultos mayores que cada uno tiene asignados.

CU-6.2 Asignar enfermero a adulto mayor

Actores

Tipo

Coord. hogar

Primario

Precondiciones

El coordinador del hogar ha consultado la lista de enfermeros disponibles.

Postcondiciones

La asignación del enfermero al grupo de adultos mayores queda registrada
con fecha de vigencia.

Referencias Cruzadas,
Req.

RF-AP-01

Descripción

El coordinador del hogar asigna uno o más enfermeros a grupos de
adultos mayores por categoría de servicio, registrando la asignación con
su respectiva fecha de vigencia.

CU-6.3 Reasignar enfermero

Actores

Tipo

Precondiciones

Coord. hogar

Opcional

Existe al menos una asignación de enfermero a adultos mayores registrada
en el sistema.

Postcondiciones

La asignación del enfermero es actualizada en el sistema.

Referencias Cruzadas,
Req.

RF-AP-03

Descripción

El coordinador del hogar puede reasignar un enfermero que ya está
asignado a un grupo de adultos mayores, actualizando la distribución de
manera eficiente según las necesidades del hogar.

CU-6.4 Administrar asignación de personal

Actores

Tipo

Precondiciones

Postcondiciones

Referencias Cruzadas,
Req.

Descripción

Coord. hogar

Primario

El coordinador del hogar ha iniciado sesión y accede al módulo de
asignación de personal.

El coordinador accede a las opciones de consulta y gestión de asignación
de enfermeros.

RF-AP-01, RF-AP-02, RF-AP-03

El coordinador del hogar accede al módulo de asignación de personal,
desde donde puede consultar la lista de enfermeros, asignarlos a adultos
mayores por categoría de servicio y reasignarlos cuando sea necesario.
Este caso de uso actúa como punto de entrada y delega a los casos de uso
específicos.

5.7. Módulo de Usuarios y Autenticación

CU-7.1 Autenticar usuario

Actores

Tipo

Precondiciones

Postcondiciones

Referencias Cruzadas,
Req.

Descripción

Usuario

Primario

El usuario ha ingresado sus credenciales (correo y contraseña) en la
pantalla de inicio de sesión.

El sistema habilita las funcionalidades correspondientes al rol del usuario
autenticado.

RF-GA-02, RF-GA-03

El sistema valida el correo electrónico y la contraseña ingresados, verifica
que existan en la base de datos y que correspondan al mismo usuario. Si
las credenciales son correctas, habilita las opciones del menú según el rol
asignado al usuario.

CU-7.2 Administrar usuarios

Actores

Tipo

Coord. entidad

Primario

Precondiciones

El coordinador de la entidad ha iniciado sesión con su rol de dirección.

Postcondiciones

El coordinador accede a las opciones de gestión de usuarios del sistema.

Referencias Cruzadas,
Req.

Descripción

RF-UA-01, RF-UA-02, RF-UA-03, RF-UA-04

El coordinador de la entidad accede al módulo de administración de
usuarios, desde donde puede crear, consultar, modificar y eliminar
usuarios del sistema. Este caso de uso actúa como punto de entrada y
delega cada operación a los casos de uso CU-7.3 al CU-7.6.

CU-7.3 Crear usuario

Actores

Tipo

Precondiciones

Postcondiciones

Coord. entidad

Primario

El coordinador de la entidad ha accedido al módulo de administración de
usuarios (CU-7.2).

El nuevo usuario queda registrado en el sistema y recibe sus credenciales
por correo electrónico.

Referencias Cruzadas,
Req.

RF-UA-01

Descripción

El coordinador define el nombre, correo, contraseña temporal y rol del
nuevo usuario (lista predefinida). El sistema registra el usuario y le envía
automáticamente sus credenciales de acceso al correo electrónico
indicado.

CU-7.4 Modificar usuario

Actores

Tipo

Precondiciones

Coord. entidad

Opcional

El coordinador de la entidad ha accedido al módulo de administración de
usuarios (CU-7.2) y selecciona un usuario existente.

Postcondiciones

Los datos y/o rol del usuario quedan actualizados en el sistema.

Referencias Cruzadas,
Req.

RF-UA-02

Descripción

El coordinador modifica los datos personales y/o el rol asignado de un
usuario existente en el sistema, actualizando la información en la base de
datos.

CU-7.5 Consultar usuario

Actores

Tipo

Precondiciones

Postcondiciones

Coord. entidad

Primario

El coordinador de la entidad ha accedido al módulo de administración de
usuarios (CU-7.2).

Se visualiza la lista de usuarios registrados con sus datos y roles
asignados.

Referencias Cruzadas,
Req.

RF-UA-04

Descripción

El coordinador consulta la lista completa de usuarios registrados en el
sistema, con información de nombre, correo, rol y estado de cada uno.

CU-7.6 Eliminar usuario

Actores

Tipo

Precondiciones

Coord. entidad

Opcional

El coordinador de la entidad ha accedido al módulo de administración de
usuarios (CU-7.2) y selecciona un usuario para eliminar.

Postcondiciones

El usuario es dado de baja (eliminación lógica) y pierde acceso al sistema.

Referencias Cruzadas,
Req.

RF-UA-03

Descripción

El coordinador da de baja a un usuario, revocando su acceso al sistema.
La eliminación es lógica, por lo que los registros históricos asociados al
usuario se conservan en la base de datos.

6. Matriz de cobertura

8. Mockups y mapa de navegación

8.1. Menu de ingreso:

8.2. Inicio de sesión:

8.3. Registrar preinscripción:

8.4. Coordinador de la entidad:

8.5. Coordinador del hogar:

9. Requerimientos no funcionales a implementar

Disponibilidad

El  sistema  deberá  garantizar  una  disponibilidad  mínima  del  95%  durante  el  horario  de
operación del hogar gerontológico. Se implementará manejo exhaustivo de excepciones para
prevenir  cierres  inesperados;  ante  cualquier  fallo  técnico,  el  sistema  mostrará  mensajes
informativos en pantalla sin detener la ejecución ni perder los datos ya guardados. Los errores
críticos quedarán registrados en un archivo de log para facilitar el diagnóstico y corrección.

Usabilidad

La interfaz será diseñada priorizando la facilidad de uso para personal con nivel variable de
competencia  digital.  Se  utilizará  un  diseño  consistente  con  tipografía  legible,  colores
diferenciados  para  mensajes  de  error  (rojo)  y  confirmación  (verde),  y  formularios  con
validación en tiempo real que oriente al usuario ante campos incompletos o datos incorrectos.
La  navegación  se  realizará  mediante  menús  contextuales  por  rol,  evitando  exponer
funcionalidades no autorizadas. Las operaciones críticas requerirán confirmación explícita del
usuario antes de ejecutarse.

Confiabilidad

Se implementarán validaciones automáticas en todas las operaciones de escritura sobre datos
sensibles, como el registro de preinscripciones, la admisión de adultos mayores y el registro de
diagnósticos.  Las  operaciones  compuestas  que  involucren  múltiples  entidades  se  ejecutarán
dentro de transacciones ACID para garantizar consistencia ante fallos. Los registros de bitácora
y los diagnósticos serán inmutables una vez guardados, preservando la integridad del historial
clínico.

Seguridad

El acceso al sistema requerirá autenticación mediante credenciales únicas. Las contraseñas se
almacenarán  con  función  de  hash  segura  (bcrypt  o  similar).  El  control  de  acceso  por  rol
garantizará  que  ningún  usuario  pueda  acceder  a  funcionalidades  ni  a  datos  que  no  le
correspondan. Las comunicaciones entre el front-end y el back-end en la  modalidad web se
realizarán sobre HTTPS. Los datos sensibles de adultos mayores estarán protegidos conforme
a las regulaciones de privacidad aplicables.

Rendimiento

El sistema deberá responder a las consultas habituales (lista de adultos mayores, bitácora del
día,  notificaciones)  en  un  tiempo  máximo  de  tres  segundos  bajo  condiciones  normales  de
operación.  La  generación  de  reportes  PDF  podrá  tomar  hasta  diez  segundos  sin  que  esto  se
considere  un  fallo.  La  base  de  datos  deberá  estar  correctamente  indexada  para  soportar  el
volumen de datos generado por el seguimiento diario de todos los adultos mayores de ambos
hogares.

10. Propuesta de negociación

•  CU-5.3  Consultar  datos  de  seguimiento  (responsable):  No  se  implementará  en  el
prototipo dado que requiere un flujo de autenticación adicional para usuarios externos
al  personal  del  hogar,  lo  cual  implica  trabajo  extra  que,  sumado  al  resto  de
funcionalidades del sistema, haría difícil cumplir con los tiempos del proyecto.

•  CU-5.5 Generar hoja de vida consolidada en PDF: No se desarrollará en esta etapa
ya  que  requiere  consolidar  información  de  varios  módulos  del  sistema  en  un  único
reporte en PDF. Se considera que el esfuerzo de implementación no es proporcional al
tiempo  disponible,  teniendo  en  cuenta  que  ya  se  contempla  la  generación  de  otros
reportes PDF en el sistema.

•  CU-5.6 Descargar datos de seguimiento (responsable): No se implementará debido
a que depende directamente de CU-5.3, el cual tampoco será desarrollado. Al no existir
el  portal  del  responsable,  esta  funcionalidad  no  tiene  contexto  en  el  que  pueda
ejecutarse.

•  CU-4.2  Gestionar  plan  de  atención:  No  se  incluirá  en  el  prototipo.  Si  bien  es  una
funcionalidad  relevante  para  el  sistema,  su  implementación  requiere  un  tiempo  de
desarrollo  considerable  que,  en  el  marco  del  proyecto  semestral,  comprometería  la
entrega de las demás funcionalidades prioritarias.

•  CU-4.3 Gestionar plan de medicamentos: No se desarrollará en este prototipo por las
mismas razones que CU-4.2. Ambas funcionalidades están estrechamente relacionadas
y su implementación conjunta dentro del tiempo disponible no es viable sin afectar la
calidad del resto del sistema.

•  CU-4.5 Chequeo de asistencia Cat. C: No se implementará en esta etapa. Aunque la
funcionalidad está claramente definida en el enunciado, su desarrollo requiere lógica
de control de horarios y estados diarios que tomaría más tiempo del disponible, por lo
que se priorizaron otros módulos de mayor impacto para el prototipo.

•  CU-4.7 Solicitar modificación a la hoja de vida del AM: No se desarrollará dado que
implica un flujo de aprobación entre el responsable del adulto mayor y la coordinación.
Implementar correctamente este proceso de solicitud, notificación y respuesta dentro
del tiempo del proyecto resultaría tedioso y podría afectar negativamente la entrega de
las demás funcionalidades.

•  CU-7.4 Modificar usuario: No se implementará en el prototipo. Para el alcance de esta
entrega  se  consideran  suficientes  las  funcionalidades  de  crear,  consultar  y  eliminar
usuarios.

11. Bibliografia

•  Sparx Systems. EA tool setup. [En línea]. Disponible en:

https://sparxsystems.com/enterprise_architect_user_guide/17.1/guide_books/ea_tool_
setup.html. Fecha de consulta: 11 de marzo de 2026.

•  Lucidchart. Tutorial — Diagrama de actividades UML. [En línea]. Disponible en:

https://www.lucidchart.com/pages/es/tutorial-diagrama-de-actividades-uml. Fecha de
consulta: 11 de marzo de 2026.

•  Northware. Técnicas efectivas para la toma de requerimientos. [En línea]. Disponible

en: https://www.northware.mx/blog/tecnicas-efectivas-para-la-toma-de-
requerimientos/. Fecha de consulta: 11 de marzo de 2026.

•  Object Management Group. About UML — UML 2.5.1 Specification. [En línea].
Disponible en: https://www.omg.org/spec/UML/2.5.1/About-UML. Fecha de
consulta: 11 de marzo de 2026.

•  GeeksforGeeks. Use Case Diagram — System Design. [En línea]. Disponible en:

https://www.geeksforgeeks.org/system-design/use-case-diagram/. Fecha de consulta:
11 de marzo de 2026.

