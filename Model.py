import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float,TIME,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Table, create_engine

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'
    ID = Column(Integer, primary_key=True)
    name = Column(String(50))
    timeStart= Column(TIME())
    timeEnd= Column(TIME())
    #To Be changed later to the proper column type
    Locations= Column(String(1000))
    # relations
    branches= relationship('Branch', back_populates="restaurant")


class Branch (Base):
    __tablename__ = 'branch'
    ID = Column(Integer, primary_key=True)
    #To Be changed later to the proper column type
    Address = Column(String(250), nullable=False)
    numOfTables = Column(Integer)
    delivery = Column(Boolean(250), nullable=False)
    resID = Column(Integer, ForeignKey('Restaurant.ID'))
    # relations
    restaurant = relationship('Restaurant', back_populates='branches')
    Tables = relationship('table', back_populates='branch')


class table(Base):
    __tablename__ = 'Table'
    ID = Column(Integer, primary_key=True)
    branchID = Column(Integer,ForeignKey('Branch.ID'))
    numOfSeats = Column(Integer)
    reserved = Column(Boolean)
    # relations
    branch = relationship('Branch', back_populates='Tables')

engine = create_engine('sqlite:///PH.db')
Base.metadata.create_all(engine)
