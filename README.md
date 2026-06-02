# Hogar Gerontológico - Sistema de Gestión 🌸

Sistema de gestión integral para hogares gerontológicos desarrollado con **Python** y **Streamlit**, utilizando **SQLAlchemy** (Data Mapper) como ORM y una base de datos SQLite.

## 🚀 Requisitos Previos

Cualquier persona que vaya a descargar o evaluar este proyecto necesitará tener instalado en su computadora:
- [Python 3.10 o superior](https://www.python.org/downloads/)
- Git (opcional, para clonar el repositorio)

## 🛠️ Instrucciones de Instalación y Ejecución

Sigue estos pasos en tu terminal (CMD, PowerShell o Bash) para clonar el proyecto, instalar las dependencias y ejecutarlo:

**1. Clonar o descargar el repositorio:**
```bash
git clone https://github.com/Mttswt/proyecto-fis.git
cd proyecto-fis
```
*(Si lo descargas como ZIP, simplemente descomprímelo y abre una terminal dentro de la carpeta `proyecto-fis`)*.

**2. Crear y activar el entorno virtual (Recomendado):**
- En Windows (PowerShell/CMD):
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
- En macOS/Linux:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

**3. Instalar las librerías necesarias:**
```bash
pip install -r app/requirements.txt
```

**4. Cargar la base de datos con datos de prueba (Población masiva):**
Para que la aplicación no esté vacía, tenemos un script que genera 29 perfiles de personal, 20 pacientes activos y decenas de registros clínicos y bitácoras.
```bash
cd app
python populate_db.py
```

**5. Iniciar la aplicación:**
```bash
# Asegúrate de estar dentro de la carpeta 'app'
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador web (por lo general en `http://localhost:8501`).

---

## 🔐 Usuarios de Prueba

Una vez en la pantalla de inicio de sesión, puedes utilizar las siguientes credenciales de prueba que se generan con el script:

- **Administrador:** 
  - Usuario: `admin` 
  - Contraseña: `admin123`
- **Enfermero (Ejemplo):** 
  - Usuario: `enf001` (hasta `enf015`)
  - Contraseña: `123`
- **Médico (Ejemplo):** 
  - Usuario: `med001` (hasta `med003`)
  - Contraseña: `123`
