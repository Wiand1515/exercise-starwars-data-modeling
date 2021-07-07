import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable = False)
    password = Column(String(16), nullable = False)
    email = Column(String(50), unique=True, nullable=False)

class Favorite_characters(Base):
    __tablename__ = 'fav_character'    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id= Column(Integer, ForeignKey('character.id'))

class Favorite_planets(Base):
    __tablename__ = 'fav_planet'  
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id= Column(Integer, ForeignKey('planet.id'))
    
class Favorite_ships(Base):
    __tablename__ = 'fav_ship'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    ship_id= Column(Integer, ForeignKey('ship.id'))

class Characters(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    height = Column(String(5))
    mass = Column(String(5))
    hair_color = Column(String(5))
    skin_color = Column(String(5))
    eye_color = Column(String(5))
    birth_year = Column(String(5))
    gender = Column(String(5))
    name = Column(String(20), unique = True, nullable = False)
    homeworld = Column(String(200), ForeignKey('planet.id'))
   
class Planets(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique = True, nullable = False) 
    diameter = Column(String(20))
    rotation_period = Column(String(10))
    orbital_period = Column(String(10))
    gravity = Column(String(50))
    population = Column(Integer, nullable = False)
    climate = Column(String(100))
    terrain = Column(String(100))
    surface_water = Column(Integer)



class Ships(Base):
    __tablename__ = 'ship'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique = True)
    name = Column(String(50)) 
    model = Column(String(50))
    starship_class = Column(String(50))
    manufacturer = Column(String(50))
    cost_in_credits = Column(String(50))
    length = Column(String(50))
    crew = Column(String(50))
    passangers = Column(Integer, nullable = False)
    max_atmosphering_speed = Column(String(50))
    hyperdrive_rating = Column(String(50))
    mglt = Column(String(50))
    cargo_capacity = Column(String(50))
    consumables = Column(String(50))
    pilots = Column(String(50))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')