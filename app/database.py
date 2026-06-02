import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# Configuramos SQLite para el prototipo
# La BD se crea en el mismo directorio donde se ejecuta la app
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'hogar.db')}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# scoped_session asegura una sesión por hilo, compatible con Streamlit
db_session = scoped_session(SessionLocal)

Base = declarative_base()

def get_db():
    """Retorna la sesión scoped actual. No la cierra prematuramente."""
    return db_session()
