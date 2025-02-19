import os
import sys
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base, Mapped, mapped_column
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    nombre: Mapped[str] = mapped_column(String(250), nullable=False)
    apellido: Mapped[str] = mapped_column(String(250), nullable=False)
    fecha_suscripcion: Mapped[Date] = mapped_column(Date, nullable=False)

    favoritos = relationship("Favorite", back_populates="usuario")

class Character(Base):
    __tablename__ = "character"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(250), nullable=False)
    altura: Mapped[float] = mapped_column(Float)
    peso: Mapped[float] = mapped_column(Float)
    color_ojos: Mapped[str] = mapped_column(String(50))
    color_pelo: Mapped[str] = mapped_column(String(50))
    nacimiento: Mapped[str] = mapped_column(String(50))
    genero: Mapped[str] = mapped_column(String(50))
    planeta_id: Mapped[int] = mapped_column(Integer, ForeignKey("planet.id"))
    
    planeta = relationship("Planet", back_populates="personajes")
    favoritos = relationship("Favorite", back_populates="personaje")

class Planet(Base):
    __tablename__ = "planet"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(250), nullable=False)
    clima: Mapped[str] = mapped_column(String(100))
    terreno: Mapped[str] = mapped_column(String(100))
    poblacion: Mapped[int] = mapped_column(Integer)
    
    personajes = relationship("Character", back_populates="planeta")
    favoritos = relationship("Favorite", back_populates="planeta")

class Favorite(Base):
    __tablename__ = "favorite"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    character_id: Mapped[int] = mapped_column(Integer, ForeignKey("character.id"), nullable=True)
    planet_id: Mapped[int] = mapped_column(Integer, ForeignKey("planet.id"), nullable=True)
    
    usuario = relationship("User", back_populates="favoritos")
    personaje = relationship("Character", back_populates="favoritos")
    planeta = relationship("Planet", back_populates="favoritos")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')



