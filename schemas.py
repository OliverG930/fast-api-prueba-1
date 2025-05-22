from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date

class ProductoBase(BaseModel):
    nombre: str = Field(..., min_length=1, description="Nombre no puede estar vacío")
    foto: str = Field(..., min_length=1, description="La foto principal es obligatoria")
    categoria_id: Optional[int] = None
    fotomostrador1: Optional[str] = None
    fotomostrador2: Optional[str] = None
    fotomostrador3: Optional[str] = None
    cantidad: int = Field(..., ge=0, description="Cantidad debe ser >= 0")
    PRECIO_ORIGINAL_YEN: int = Field(..., ge=0)
    PRECIO_ORIGINAL_EUR: float = Field(..., ge=0.0)
    PRECIO_VENTA_YEN: int = Field(..., ge=0)
    PRECIO_IDEAL_EUR: float = Field(..., ge=0.0)
    PRECIO_ACTUAL: float = Field(..., ge=0.0)
    fecha_lanzamiento: Optional[date] = None

    # Validador extra (opcional) para evitar espacios en blanco como nombre
    @validator("nombre", "foto")
    def no_espacios_en_blanco(cls, v):
        if not v.strip():
            raise ValueError("Este campo no puede estar vacío o en blanco")
        return v

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass
