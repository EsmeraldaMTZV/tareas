from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class UsuarioSchema(BaseModel):
    nombre: str = Field(min_length=8, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8)

class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class TareaSchema(BaseModel):
    titulo: str = Field(min_length=1, max_length=200)
    descripcion: Optional[str] = None
    prioridad: str = "media"
    clasificacion: str = "personal"
    
class UsuarioFormSchema(BaseModel):
    nombre: str = Field(min_lenght=2, max_lenght=30)
    apellido: str = Field(min_lenght=8, max_lenght=30)
    email: EmailStr
    password : str = Field (min_lenght=8)
    telefono : Optional[str] =Field(None, min_lenght=7,max_lenght=15)
    foto : Optional[str] =Field(None,max_lenght=255)
    
    activo: bool = True
    fecha_creacion: datetime = Field(None, min_lenght=7,max_lenght=15)
    fecha_modificacion: Optional[datetime] = None
