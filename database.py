# database.py
from sqlalchemy import create_engine

DB_USER = "your_user"
DB_PASSWORD = "your_password"
DB_HOST = "localhost-example"
DB_NAME = "Your_db_name"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Creamos el motor
engine = create_engine(DATABASE_URL)
