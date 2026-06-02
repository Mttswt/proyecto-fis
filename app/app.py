import datetime
import streamlit as st
import bcrypt
from database import engine, get_db
import models

try:
    from fpdf import FPDF
except ImportError:
    FPDF = None

# Crear las tablas en la BD si no existen
models.Base.metadata.create_all(bind=engine)

# --- Funciones Auxiliares ---

def check_password(hashed_password, user_password):
    """Valida la contraseña del usuario contra el hash almacenado."""
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password.encode('utf-8'))

def hash_password(password):
    """Genera un hash bcrypt para la contraseña dada."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def init_db(db):
    """Inicializa la BD con roles y usuario admin por defecto."""
    # Crear roles por defecto
    roles_default = [
        {"nombre": "Admin", "valor": 1},
        {"nombre": "Coordinador", "valor": 2},
        {"nombre": "Enfermero", "valor": 3},
        {"nombre": "Medico", "valor": 4},
    ]
    for rol_data in roles_default:
        if not db.query(models.Rol).filter(models.Rol.nombre == rol_data["nombre"]).first():
            db.add(models.Rol(nombre=rol_data["nombre"], valor=rol_data["valor"]))
    db.commit()

    # Crear usuario admin por defecto si no existe
    if not db.query(models.TokenUsuario).filter(models.TokenUsuario.nombreUsuario == "admin").first():
        rol_admin = db.query(models.Rol).filter(models.Rol.nombre == "Admin").first()
        admin_user = models.TokenUsuario(
            nombreUsuario="admin",
            correo="admin@hogar.com",
            contrasenaHash=hash_password("admin123"),
            rol_id=rol_admin.idRol
        )
        db.add(admin_user)
        db.commit()

def limpiar_texto(texto):
    """Reemplaza caracteres especiales para compatibilidad con FPDF (latin-1)."""
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

# --- Interfaz de Streamlit ---

st.set_page_config(page_title="Hogar Gerontologico", page_icon="🌸", layout="centered")

# =============================================
# CSS PERSONALIZADO - TEMA ROSA PASTEL TIERNO
# =============================================
st.markdown("""
<style>
    /* ---- Fuente Google (Poppins: suave y redondeada) ---- */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif !important;
    }

    /* ---- Fondo general ---- */
    .stApp {
        background: linear-gradient(180deg, #fff5f7 0%, #fce4ec 50%, #fff0f3 100%) !important;
    }

    /* ---- Sidebar ---- */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #fce4ec 0%, #f8bbd0 100%) !important;
        border-right: 2px solid #f8a4b8;
    }
    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] .stMarkdown h1,
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: #5d4037 !important;
    }

    /* ---- Títulos ---- */
    h1 {
        color: #d81b60 !important;
        font-weight: 600 !important;
    }
    h2, h3 {
        color: #ad1457 !important;
        font-weight: 500 !important;
    }

    /* ---- Botones ---- */
    .stButton > button {
        background: linear-gradient(135deg, #f8a4b8 0%, #f48fb1 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: 500 !important;
        font-family: 'Poppins', sans-serif !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 8px rgba(244, 143, 177, 0.35) !important;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #f48fb1 0%, #ec407a 100%) !important;
        box-shadow: 0 4px 15px rgba(236, 64, 122, 0.4) !important;
        transform: translateY(-1px) !important;
    }

    /* ---- Inputs y text areas ---- */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div {
        border-radius: 12px !important;
        border: 1.5px solid #f8bbd0 !important;
        background-color: #fff9fb !important;
        font-family: 'Poppins', sans-serif !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #f48fb1 !important;
        box-shadow: 0 0 0 2px rgba(244, 143, 177, 0.25) !important;
    }

    /* ---- Tabs ---- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 15px 15px 0 0 !important;
        padding: 8px 20px !important;
        font-family: 'Poppins', sans-serif !important;
    }

    /* ---- Expander ---- */
    .streamlit-expanderHeader {
        background-color: #fce4ec !important;
        border-radius: 10px !important;
        font-family: 'Poppins', sans-serif !important;
    }

    /* ---- Métricas ---- */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #fce4ec 0%, #fff0f3 100%);
        border: 1.5px solid #f8bbd0;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0 2px 8px rgba(244, 143, 177, 0.15);
    }
    [data-testid="stMetricValue"] {
        color: #d81b60 !important;
        font-weight: 600 !important;
    }

    /* ---- Forms ---- */
    [data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.7) !important;
        border: 1.5px solid #f8bbd0 !important;
        border-radius: 15px !important;
        padding: 20px !important;
        box-shadow: 0 2px 12px rgba(244, 143, 177, 0.12) !important;
    }

    /* ---- Success/Error/Info/Warning boxes ---- */
    .stAlert {
        border-radius: 12px !important;
    }

    /* ---- Download button ---- */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #ce93d8 0%, #ba68c8 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        font-family: 'Poppins', sans-serif !important;
        box-shadow: 0 2px 8px rgba(186, 104, 200, 0.35) !important;
    }

    /* ---- Radio buttons en sidebar ---- */
    .stRadio > label {
        font-family: 'Poppins', sans-serif !important;
    }

    /* ---- Scrollbar ---- */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #fff0f3; }
    ::-webkit-scrollbar-thumb { background: #f8bbd0; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #f48fb1; }

    /* ---- Login Card ---- */
    .login-card {
        background: rgba(255, 255, 255, 0.85);
        border: 2px solid #f8bbd0;
        border-radius: 25px;
        padding: 40px 30px 30px 30px;
        max-width: 420px;
        margin: 0 auto;
        box-shadow: 0 8px 32px rgba(244, 143, 177, 0.2);
        text-align: center;
    }
    .login-emoji {
        font-size: 64px;
        margin-bottom: 5px;
    }
    .login-title {
        color: #d81b60 !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 28px;
        margin-bottom: 3px;
    }
    .login-subtitle {
        color: #8d6e63;
        font-family: 'Poppins', sans-serif;
        font-weight: 300;
        font-size: 15px;
        margin-bottom: 20px;
    }
    .welcome-banner {
        text-align: center;
        padding: 10px;
        margin-bottom: 10px;
    }

    /* ---- Ocultar menú hamburguesa y footer ---- */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

db = get_db()
init_db(db)

if not st.session_state["logged_in"]:
    # --- Pantalla de Login ---
    st.markdown("""
    <div class="welcome-banner">
        <div class="login-emoji">🌸</div>
        <div class="login-title">Hogar Gerontológico</div>
        <div class="login-subtitle">Sistema de Gestión Integral</div>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("login_form"):
        username = st.text_input("👤 Usuario", placeholder="admin")
        password = st.text_input("🔒 Contraseña", type="password", placeholder="admin123")
        submit_button = st.form_submit_button("🌷 Ingresar")
        
        if submit_button:
            if not username or not password:
                st.error("Por favor ingresa usuario y contraseña.")
            else:
                user = db.query(models.TokenUsuario).filter(
                    models.TokenUsuario.nombreUsuario == username
                ).first()
                if user and check_password(user.contrasenaHash, password):
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = user.nombreUsuario
                    st.session_state["role"] = user.rol.nombre
                    st.success("¡Inicio de sesión exitoso!")
                    st.rerun()
                else:
                    st.error("Usuario o contraseña incorrectos.")
else:
    # --- Navegación ---
    st.sidebar.markdown("""
    <div style="text-align:center; padding: 10px 0;">
        <span style="font-size: 36px;">🌸</span><br>
        <span style="font-family: 'Poppins', sans-serif; font-weight: 600; color: #d81b60; font-size: 16px;">
            Hogar Gerontológico
        </span>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.write(f"👤 **{st.session_state['username']}** · {st.session_state['role']}")
    st.sidebar.write("---")
    
    menu = st.sidebar.radio(
        "Menú Principal",
        ["🏠 Dashboard", "🏡 Gestión de Hogares", "📝 Preinscripción", "🩺 Seguimiento Clínico", "🖨️ Reportes PDF", "👥 Personal"]
    )
    
    st.sidebar.write("---")
    if st.sidebar.button("🚪 Cerrar Sesión"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
    
    # ============================
    # DASHBOARD
    # ============================
    if menu == "🏠 Dashboard":
        st.markdown("""
        <div style="text-align:center; padding: 15px 0 5px 0;">
            <span style="font-size: 48px;">🌷</span>
            <h1 style="margin:0;">¡Bienvenido!</h1>
            <p style="color: #8d6e63; font-size: 16px;">Panel de control del sistema de gestión</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            total_hogares = db.query(models.HogarGerontologico).count()
            st.metric("🏡 Hogares", total_hogares)
        with col2:
            total_pacientes = db.query(models.AdultoMayor).filter(models.AdultoMayor.activo == True).count()
            st.metric("🧓 Pacientes Activos", total_pacientes)
        with col3:
            total_pendientes = db.query(models.Preinscripcion).filter(models.Preinscripcion.estado == "PENDIENTE").count()
            st.metric("📋 Solicitudes Pendientes", total_pendientes)
        
        st.write("")
        st.info("🌸 Selecciona un módulo en el menú lateral para comenzar.")
        
    # ============================
    # GESTIÓN DE HOGARES
    # ============================
    elif menu == "🏡 Gestión de Hogares":
        st.title("🏡 Gestión de Hogares")
        
        tab1, tab2 = st.tabs(["Listado de Hogares", "Crear Nuevo Hogar"])
        
        with tab1:
            hogares = db.query(models.HogarGerontologico).all()
            if not hogares:
                st.info("No hay hogares registrados en el sistema.")
            else:
                for hogar in hogares:
                    with st.expander(f"Hogar: {hogar.nombre}"):
                        st.write(f"**Dirección:** {hogar.direccion}")
                        st.write(f"**Capacidad Total:** {hogar.capacidadTotal}")
                        st.write(f"**Estado:** {'Activo' if hogar.activo else 'Inactivo'}")
                        st.write(f"**Fecha Creación:** {hogar.fechaCreacion}")
        
        with tab2:
            st.subheader("Registrar un nuevo hogar")
            with st.form("nuevo_hogar"):
                nombre = st.text_input("Nombre del Hogar")
                direccion = st.text_input("Dirección")
                capacidad = st.number_input("Capacidad Total (Cupos)", min_value=1, value=30)
                submit_hogar = st.form_submit_button("Guardar Hogar")
                
                if submit_hogar:
                    if nombre and direccion:
                        nuevo_hogar = models.HogarGerontologico(
                            nombre=nombre,
                            direccion=direccion,
                            capacidadTotal=capacidad
                        )
                        db.add(nuevo_hogar)
                        db.commit()
                        st.success(f"Hogar '{nombre}' creado exitosamente.")
                        st.rerun()
                    else:
                        st.error("Por favor completa los campos obligatorios.")

    # ============================
    # PREINSCRIPCIÓN Y ADMISIÓN
    # ============================
    elif menu == "📝 Preinscripción":
        st.title("📝 Preinscripción y Admisión")
        
        tab1, tab2 = st.tabs(["Nueva Preinscripción", "Gestión de Admisiones"])
        
        with tab1:
            st.subheader("Registrar Preinscripción")
            with st.form("preinscripcion_form"):
                st.write("**Datos del Responsable**")
                resp_nombre = st.text_input("Nombres del Responsable")
                resp_apellido = st.text_input("Apellidos del Responsable")
                resp_id = st.text_input("Identificación del Responsable")
                resp_correo = st.text_input("Correo Electrónico del Responsable")
                
                st.write("**Datos del Adulto Mayor**")
                am_nombre = st.text_input("Nombres del Adulto Mayor")
                am_apellido = st.text_input("Apellidos del Adulto Mayor")
                am_id = st.text_input("Identificación del Adulto Mayor")
                am_edad = st.number_input("Edad", min_value=60, value=70)
                am_cat = st.selectbox("Categoría Solicitada", ["A_INDIVIDUAL", "B_COMPARTIDA", "C_DIURNA"])
                
                submit_pre = st.form_submit_button("Enviar Solicitud")
                
                if submit_pre:
                    if resp_nombre and resp_id and am_nombre and am_id:
                        # Verificar que el adulto mayor no esté ya registrado
                        existe_am = db.query(models.AdultoMayor).filter(
                            models.AdultoMayor.identificacion == am_id
                        ).first()
                        if existe_am:
                            st.error("Ya existe un adulto mayor con esa identificación.")
                        else:
                            # Crear o buscar responsable
                            nuevo_resp = db.query(models.Responsable).filter(
                                models.Responsable.identificacion == resp_id
                            ).first()
                            if not nuevo_resp:
                                nuevo_resp = models.Responsable(
                                    primerNombre=resp_nombre,
                                    primerApellido=resp_apellido,
                                    identificacion=resp_id,
                                    correoElectronico=resp_correo
                                )
                                db.add(nuevo_resp)
                                db.commit()
                            
                            # Crear preinscripcion
                            nueva_pre = models.Preinscripcion(responsable_id=nuevo_resp.idResponsable)
                            db.add(nueva_pre)
                            db.commit()
                            
                            # Crear adulto mayor
                            nuevo_am = models.AdultoMayor(
                                primerNombre=am_nombre,
                                primerApellido=am_apellido,
                                identificacion=am_id,
                                edad=am_edad,
                                categoriaServicio=am_cat,
                                responsable_id=nuevo_resp.idResponsable,
                                preinscripcion_id=nueva_pre.idPreinscripcion
                            )
                            db.add(nuevo_am)
                            db.commit()
                            
                            st.success("¡Preinscripción enviada exitosamente!")
                            st.rerun()
                    else:
                        st.error("Por favor completa los campos obligatorios (Nombres e Identificaciones).")

        with tab2:
            st.subheader("Solicitudes Pendientes")
            pendientes = db.query(models.Preinscripcion).filter(
                models.Preinscripcion.estado == "PENDIENTE"
            ).all()
            
            if not pendientes:
                st.info("No hay solicitudes pendientes.")
            else:
                for p in pendientes:
                    if p.adultos_mayores:
                        am = p.adultos_mayores[0]
                        with st.expander(f"Solicitud #{p.idPreinscripcion} - {am.primerNombre} {am.primerApellido}"):
                            st.write(f"**Adulto Mayor:** {am.primerNombre} {am.primerApellido} (ID: {am.identificacion})")
                            st.write(f"**Edad:** {am.edad}")
                            st.write(f"**Responsable:** {p.responsable.primerNombre} {p.responsable.primerApellido}")
                            st.write(f"**Categoría Solicitada:** {am.categoriaServicio}")
                            st.write(f"**Fecha de Envío:** {p.fechaEnvio}")
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                if st.button("✅ Aprobar", key=f"apr_{p.idPreinscripcion}"):
                                    p.estado = "APROBADA"
                                    am.activo = True
                                    am.fechaIngreso = datetime.date.today()
                                    db.commit()
                                    st.success("Solicitud aprobada.")
                                    st.rerun()
                            with col2:
                                if st.button("❌ Rechazar", key=f"rej_{p.idPreinscripcion}"):
                                    p.estado = "RECHAZADA"
                                    db.commit()
                                    st.warning("Solicitud rechazada.")
                                    st.rerun()

    # ============================
    # SEGUIMIENTO CLÍNICO
    # ============================
    elif menu == "🩺 Seguimiento Clínico":
        st.title("🩺 Seguimiento Clínico y Bitácoras")
        
        # Buscar pacientes activos
        pacientes = db.query(models.AdultoMayor).filter(models.AdultoMayor.activo == True).all()
        
        if not pacientes:
            st.warning("No hay pacientes activos en el sistema. Debes aprobar una preinscripción primero.")
        else:
            opciones_pacientes = {
                f"{p.primerNombre} {p.primerApellido} (ID: {p.identificacion})": p 
                for p in pacientes
            }
            seleccion_paciente = st.selectbox("Seleccione un paciente:", list(opciones_pacientes.keys()))
            paciente = opciones_pacientes[seleccion_paciente]
            
            st.write("---")
            tab1, tab2 = st.tabs(["Bitácora Diaria", "Diagnósticos"])
            
            with tab1:
                st.subheader("Registrar Observación Diaria")
                with st.form("bitacora_form"):
                    fecha_hora = st.text_input(
                        "Fecha y Hora", 
                        value=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    )
                    signos = st.text_input("Signos Vitales (ej: PA: 120/80, FC: 70)")
                    obs = st.text_area("Observaciones Generales")
                    submit_bitacora = st.form_submit_button("Guardar Registro")
                    
                    if submit_bitacora:
                        if obs:
                            nueva_bitacora = models.BitacoraDiaria(
                                fechaHora=fecha_hora,
                                signosVitales=signos,
                                observaciones=obs,
                                adulto_mayor_id=paciente.idAdulto,
                                registradoPor=st.session_state['username']
                            )
                            db.add(nueva_bitacora)
                            db.commit()
                            st.success("Bitácora registrada exitosamente.")
                            st.rerun()
                        else:
                            st.error("Las observaciones no pueden estar vacías.")
                            
                st.subheader("Historial de Bitácoras")
                bitacoras = db.query(models.BitacoraDiaria).filter(
                    models.BitacoraDiaria.adulto_mayor_id == paciente.idAdulto
                ).order_by(models.BitacoraDiaria.idBitacora.desc()).all()
                if not bitacoras:
                    st.info("No hay registros para este paciente.")
                else:
                    for b in bitacoras:
                        with st.expander(f"Registro: {b.fechaHora} - {b.registradoPor}"):
                            st.write(f"**Signos Vitales:** {b.signosVitales}")
                            st.write(f"**Observaciones:** {b.observaciones}")
            
            with tab2:
                st.subheader("Nuevo Diagnóstico")
                with st.form("diagnostico_form"):
                    tipo_diag = st.selectbox("Tipo", ["Medico", "Psicologico", "Nutricional"])
                    desc_diag = st.text_area("Descripción del Diagnóstico")
                    submit_diag = st.form_submit_button("Añadir Diagnóstico")
                    
                    if submit_diag:
                        if desc_diag:
                            nuevo_diag = models.Diagnostico(
                                tipo=tipo_diag,
                                descripcion=desc_diag,
                                adulto_mayor_id=paciente.idAdulto
                            )
                            db.add(nuevo_diag)
                            db.commit()
                            st.success("Diagnóstico añadido.")
                            st.rerun()
                        else:
                            st.error("La descripción es obligatoria.")
                        
                st.subheader("Diagnósticos Actuales")
                diagnosticos = db.query(models.Diagnostico).filter(
                    models.Diagnostico.adulto_mayor_id == paciente.idAdulto
                ).all()
                if not diagnosticos:
                    st.info("No hay diagnósticos registrados.")
                else:
                    for d in diagnosticos:
                        st.markdown(f"**{d.fecha} - {d.tipo}**: {d.descripcion}")

    # ============================
    # REPORTES PDF
    # ============================
    elif menu == "🖨️ Reportes PDF":
        st.title("🖨️ Reportes PDF")
        
        if FPDF is None:
            st.error("La libreria FPDF2 no esta instalada. Ejecuta: pip install -r requirements.txt")
        else:
            tab1, tab2 = st.tabs(["Listado por Categoría", "Hoja de Vida de Residente"])
            
            with tab1:
                st.subheader("Listado de Adultos Mayores por Categoría")
                cat_select = st.selectbox("Categoría a exportar:", ["A_INDIVIDUAL", "B_COMPARTIDA", "C_DIURNA"])
                if st.button("Generar Reporte de Categoría"):
                    pacientes_cat = db.query(models.AdultoMayor).filter(
                        models.AdultoMayor.categoriaServicio == cat_select,
                        models.AdultoMayor.activo == True
                    ).all()
                    
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Helvetica", "B", 16)
                    pdf.cell(0, 10, limpiar_texto(f"Listado de Pacientes - Categoria: {cat_select}"), ln=True, align='C')
                    pdf.ln(10)
                    
                    if not pacientes_cat:
                        pdf.set_font("Helvetica", size=12)
                        pdf.cell(0, 8, "No hay pacientes activos en esta categoria.", ln=True)
                    else:
                        pdf.set_font("Helvetica", size=12)
                        for p in pacientes_cat:
                            texto = limpiar_texto(f"- {p.primerNombre} {p.primerApellido} (ID: {p.identificacion}) - Edad: {p.edad}")
                            pdf.cell(0, 8, texto, ln=True)
                    
                    pdf_bytes = bytes(pdf.output())
                    st.download_button(
                        label="Descargar PDF",
                        data=pdf_bytes,
                        file_name=f"reporte_{cat_select}.pdf",
                        mime="application/pdf"
                    )
            
            with tab2:
                st.subheader("Generar Hoja de Vida")
                pacientes_activos = db.query(models.AdultoMayor).filter(
                    models.AdultoMayor.activo == True
                ).all()
                if not pacientes_activos:
                    st.info("No hay residentes activos.")
                else:
                    opciones = {f"{p.primerNombre} {p.primerApellido}": p for p in pacientes_activos}
                    seleccion = st.selectbox("Seleccione el residente:", list(opciones.keys()))
                    p_sel = opciones[seleccion]
                    
                    if st.button("Generar Hoja de Vida Completa"):
                        pdf = FPDF()
                        pdf.add_page()
                        pdf.set_font("Helvetica", "B", 18)
                        pdf.cell(0, 10, "HOJA DE VIDA CLINICA", ln=True, align='C')
                        pdf.ln(5)
                        
                        pdf.set_font("Helvetica", "B", 14)
                        pdf.cell(0, 8, "Datos Personales", ln=True)
                        pdf.set_font("Helvetica", size=12)
                        pdf.cell(0, 8, limpiar_texto(f"Nombre: {p_sel.primerNombre} {p_sel.primerApellido}"), ln=True)
                        pdf.cell(0, 8, limpiar_texto(f"Identificacion: {p_sel.identificacion}"), ln=True)
                        pdf.cell(0, 8, limpiar_texto(f"Edad: {p_sel.edad} | Categoria: {p_sel.categoriaServicio}"), ln=True)
                        if p_sel.fechaIngreso:
                            pdf.cell(0, 8, limpiar_texto(f"Fecha de Ingreso: {p_sel.fechaIngreso}"), ln=True)
                        pdf.ln(5)
                        
                        pdf.set_font("Helvetica", "B", 14)
                        pdf.cell(0, 8, "Diagnosticos", ln=True)
                        pdf.set_font("Helvetica", size=12)
                        if p_sel.diagnosticos:
                            for d in p_sel.diagnosticos:
                                pdf.multi_cell(0, 8, limpiar_texto(f"[{d.fecha}] {d.tipo}: {d.descripcion}"))
                        else:
                            pdf.cell(0, 8, "Sin diagnosticos registrados.", ln=True)
                        pdf.ln(5)
                        
                        pdf.set_font("Helvetica", "B", 14)
                        pdf.cell(0, 8, "Ultimas Bitacoras", ln=True)
                        pdf.set_font("Helvetica", size=10)
                        ultimas_bitacoras = list(p_sel.bitacoras)[-5:]
                        if ultimas_bitacoras:
                            for b in ultimas_bitacoras:
                                texto = limpiar_texto(
                                    f"{b.fechaHora} ({b.registradoPor}) - SV: {b.signosVitales}\nObs: {b.observaciones}"
                                )
                                pdf.multi_cell(0, 6, texto)
                                pdf.ln(2)
                        else:
                            pdf.cell(0, 8, "Sin bitacoras registradas.", ln=True)
                            
                        pdf_bytes = bytes(pdf.output())
                        st.download_button(
                            label=f"Descargar Hoja de Vida - {p_sel.primerNombre}",
                            data=pdf_bytes,
                            file_name=f"hv_{p_sel.identificacion}.pdf",
                            mime="application/pdf"
                        )

    # ============================
    # GESTIÓN DE PERSONAL
    # ============================
    elif menu == "👥 Personal":
        st.title("👥 Gestión de Personal")
        
        tab1, tab2 = st.tabs(["Listado", "Registrar Personal"])
        
        with tab1:
            personal = db.query(models.Personal).all()
            if not personal:
                st.info("No hay personal registrado.")
            else:
                for p in personal:
                    with st.expander(f"{p.primerNombre} {p.primerApellido} - {p.tipoPersonal}"):
                        st.write(f"**Identificación:** {p.identificacion}")
                        st.write(f"**Correo:** {p.correoElectronico}")
                        st.write(f"**Fecha Contratación:** {p.fechaContratacion}")
                        st.write(f"**Estado:** {'Activo' if p.activo else 'Inactivo'}")
        
        with tab2:
            st.subheader("Registrar nuevo miembro del personal")
            with st.form("nuevo_personal"):
                p_nombre = st.text_input("Nombres")
                p_apellido = st.text_input("Apellidos")
                p_id = st.text_input("Identificación")
                p_correo = st.text_input("Correo Electrónico")
                p_tipo = st.selectbox("Tipo de Personal", ["Coordinador", "Enfermero", "Medico", "Psicologo", "Nutricionista"])
                submit_personal = st.form_submit_button("Guardar")
                
                if submit_personal:
                    if p_nombre and p_id:
                        existe = db.query(models.Personal).filter(
                            models.Personal.identificacion == p_id
                        ).first()
                        if existe:
                            st.error("Ya existe personal con esa identificación.")
                        else:
                            nuevo_p = models.Personal(
                                primerNombre=p_nombre,
                                primerApellido=p_apellido,
                                identificacion=p_id,
                                correoElectronico=p_correo,
                                tipoPersonal=p_tipo
                            )
                            db.add(nuevo_p)
                            db.commit()
                            st.success(f"Personal '{p_nombre} {p_apellido}' registrado.")
                            st.rerun()
                    else:
                        st.error("Nombre e Identificación son obligatorios.")
