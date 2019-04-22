import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float,TIME,Boolean, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Table, create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'
    ID = Column(Integer, primary_key=True)
    name = Column(String(50))
    #To Be changed later to the proper column type for the next 3 columns
    timeStart= Column(String())
    timeEnd= Column(String())
    Locations= Column(String(1000))
    # relations
    branches = relationship('Branch', back_populates="restaurant")
    Items = relationship('Item',back_populates="restaurant")
    complains = relationship('Complain',back_populates="restaurant")


class Branch (Base):
    __tablename__ = 'branch'
    ID = Column(Integer, primary_key=True)
    #To Be changed later to the proper column type
    Address = Column(String(250), nullable=False)
    numOfTables = Column(Integer)
    delivery = Column(Boolean(250), nullable=False)
    resID = Column(Integer, ForeignKey('restaurant.ID'))
    # relations
    restaurant = relationship('Restaurant', back_populates='branches')
    Tables = relationship('table', back_populates='branch')


class table(Base):
    __tablename__ = 'Table'
    ID = Column(Integer, primary_key=True)
    branchID = Column(Integer,ForeignKey('branch.ID'))
    numOfSeats = Column(Integer)
    reserved = Column(Boolean)
    # relations
    branch = relationship('Branch', back_populates='Tables')

class Complain(Base):
   __tablename__ = 'complain'
   ID= Column(Integer, primary_key=True)
   branchID = Column(Integer, ForeignKey('branch.ID'))
   resID = Column(Integer, ForeignKey('restaurant.ID'))
   File = Column(TEXT)
   customer_ID = Column(Integer, ForeignKey('customer.id'))
   #relations
   restaurant = relationship('Restaurant',back_populates="complains")

class Item (Base):
   __tablename__ = 'Item'
   ID= Column(Integer, primary_key=True)
   resID = Column(Integer, ForeignKey('restaurant.ID'))
   name= Column(String)
   price= Column(Float)
   #relatoins
   restaurant= relationship('Restaurant',back_populates="Items")


class User (Base):
   __tablename__ = 'User'
   ID = Column(Integer, primary_key=True)
   mail = Column(String(250), nullable=False)
   password = Column(String(250),nullable = False)
   discriminator = Column(String(250), nullable = False)
   __mapper_args__ = { 'polymorphic_identity': 'User',
       'polymorphic_on': discriminator}


class Customer (User):
    __tablename__ = 'Customer'
    id = Column(None, ForeignKey('User.ID'), primary_key=True)
    name = Column(String)
    Phone = Column(TEXT)
    Address = Column(TEXT)
    __mapper_args__ = {'polymorphic_identity': 'Customer'}


class Admin (User):
    __mapper_args__ = {'polymorphic_identity': 'Admin'}
    __tablename__ = 'Admin'
    id = Column(None, ForeignKey('User.ID'), primary_key=True)
    resID = Column(Integer, ForeignKey('restaurant.ID'))

class Reservation(Base):
    __tablename__ = 'Reservation'
    ID = Column(Integer, primary_key=True)
    CusID= Column(Integer, ForeignKey('Customer.id'))
    numOfPeople= Column (Integer)
    BranchID= Column(Integer,ForeignKey('branch.ID'))
    tableID= Column(Integer, ForeignKey('Table.ID'))
    resID= Column(Integer, ForeignKey('restaurant.ID'))
    #To Be changed later to the proper column type
    timeReserved= Column (TEXT)
    timeMade= Column(TEXT)


engine = create_engine('sqlite:///PH.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
r=Reservation(ID=0, CusID=1, numOfPeople=8, BranchID=0, tableID=0,resID=0, timeReserved="6", timeMade="9")
#album = Restaurant(ID=0, name="nour",timeStart="9",timeEnd="12",Locations="hdhhgygdhdgfuyehduhfsufhdjsfhuhjdhf" )
#br= Branch(ID=0,Address="dhsjhsjfsf",numOfTables=5, delivery=True,resID=0)
#t=table(ID=0, branchID=0, numOfSeats=4,reserved=False)
#g=Item(ID=0,resID=0, name="fdjkdfhujhdfurhfudf", price=89.3)
#h=Customer(ID=1,mail="fdfdf",password="dfdf",name="dsdsdsdc",Phone="434242",Address="fdfsd")

session.add(r)
session.commit()

