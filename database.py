# database.py
from sqlalchemy import create_engine

DB_USER = "root"
DB_PASSWORD = "root"
DB_HOST = "localhost"
DB_NAME = "tienda_figuras_anime"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Creamos el motor
engine = create_engine(DATABASE_URL)
