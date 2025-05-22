from http.client import HTTPException

from fastapi import  FastAPI
from sqlalchemy import create_engine, text
from database import engine  # Importamos la conexión
from schemas import ProductoCreate, ProductoUpdate
app=FastAPI()

#todo los metodos
#GET , PUT ,POST, DELETE

@app.get("/")
def read_root():
    return {"mensaje": "Conexión a FastAPI activa"}

@app.get("/productos")
def get_productos():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM productos"))
        productos = [dict(row._mapping) for row in result]  # <-- usa _mapping
    return {"productos": productos}

@app.post("/productos")
def create_producto(producto: ProductoCreate):
    query = text("""
        INSERT INTO productos (nombre, foto, categoria_id, fotomostrador1, fotomostrador2, fotomostrador3,
        cantidad, PRECIO_ORIGINAL_YEN, PRECIO_ORIGINAL_EUR, PRECIO_VENTA_YEN, 
        PRECIO_IDEAL_EUR, PRECIO_ACTUAL, fecha_lanzamiento)
        VALUES (:nombre, :foto, :categoria_id, :fotomostrador1, :fotomostrador2, :fotomostrador3, 
        :cantidad, :PRECIO_ORIGINAL_YEN, :PRECIO_ORIGINAL_EUR, :PRECIO_VENTA_YEN, 
        :PRECIO_IDEAL_EUR, :PRECIO_ACTUAL, :fecha_lanzamiento)
    """)
    with engine.connect() as conn:
        conn.execute(query, producto.dict())
        conn.commit()
    return {"mensaje": "Producto creado exitosamente"}

@app.put("/productos/{producto_id}")
def update_producto(producto_id: int, producto: ProductoUpdate):
    # Verificar si el producto existe
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM productos WHERE producto_id = :id"), {"id": producto_id})
        if result.fetchone() is None:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        # Si existe, actualiza
        query = text("""
            UPDATE productos SET
                nombre = :nombre,
                foto = :foto,
                categoria_id = :categoria_id,
                fotomostrador1 = :fotomostrador1,
                fotomostrador2 = :fotomostrador2,
                fotomostrador3 = :fotomostrador3,
                cantidad = :cantidad,
                PRECIO_ORIGINAL_YEN = :PRECIO_ORIGINAL_YEN,
                PRECIO_ORIGINAL_EUR = :PRECIO_ORIGINAL_EUR,
                PRECIO_VENTA_YEN = :PRECIO_VENTA_YEN,
                PRECIO_IDEAL_EUR = :PRECIO_IDEAL_EUR,
                PRECIO_ACTUAL = :PRECIO_ACTUAL,
                fecha_lanzamiento = :fecha_lanzamiento
            WHERE producto_id = :producto_id
        """)
        values = producto.dict()
        values["producto_id"] = producto_id
        conn.execute(query, values)
        conn.commit()

    return {"mensaje": "Producto actualizado"}

@app.delete("/productos/{producto_id}")
def delete_producto(producto_id: int):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM productos WHERE producto_id = :id"), {"id": producto_id})
        if result.fetchone() is None:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        conn.execute(text("DELETE FROM productos WHERE producto_id = :id"), {"id": producto_id})
        conn.commit()

    return {"mensaje": "Producto eliminado"}
