from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database_entities import Category

Base = declarative_base()

engine = create_engine('sqlite:///itemcatalogwithcategory.db')

Base.metadata.bind = engine

DB_session = sessionmaker(bind=engine)

session = DB_session()

category0 = Category(category='Books')
category1 = Category(category='Sporting')
category2 = Category(category='Video gaming')
category3 = Category(category='Music instruments')
category4 = Category(category='Household')
category5 = Category(category='Furniture')
category6 = Category(category='Business')
category7 = Category(category='Cell phones')
category8 = Category(category='Clothes')
category9 = Category(category='Computers')
category10 = Category(category='Auto parts')
category11 = Category(category='Electronics')

session.add(category0)
session.add(category1)
session.add(category2)
session.add(category3)
session.add(category4)
session.add(category5)
session.add(category6)
session.add(category7)
session.add(category8)
session.add(category9)
session.add(category10)
session.add(category11)

session.commit()

print 'Categories created!'
