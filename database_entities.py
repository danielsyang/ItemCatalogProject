from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_login = Column(String(250), primary_key=True)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    category = Column(String(250), nullable=False)


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    user_login = Column(String(250), ForeignKey('user.user_login'))
    user = relationship(User)
    category_id = Column(String(250), ForeignKey('category.category_id'))
    cat = relationship(Category)


engine = create_engine('sqlite:///itemcatalogwithcategory.db')

Base.metadata.create_all(engine)
