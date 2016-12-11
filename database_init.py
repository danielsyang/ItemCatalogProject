from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database_entities import Category

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

session.add(category0)
session.add(category1)
session.add(category2)
session.add(category3)
session.add(category4)

session.commit()

print 'Categories created!'
