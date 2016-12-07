from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from category import Category

Base = declarative_base()

engine = create_engine('sqlite:///itemcatalogwithcategory.db')

Base.metadata.bind = engine

DB_session = sessionmaker(bind=engine)

session = DB_session()

category0 = Category(category='Book')
category1 = Category(category='Sport')
category2 = Category(category='Video game')
category3 = Category(category='Movies')
category4 = Category(category='Household')

