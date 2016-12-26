from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    category = Column(String(250), nullable=False)


class Item(Base):
    __tablename__ = 'item'

    item_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship(User)
    category_id = Column(Integer, ForeignKey('category.category_id'))
    cat = relationship(Category)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'user_id': self.user_id,
            'category_id': self.category_id,
        }


engine = create_engine('sqlite:///itemcatalogwithcategory.db')

Base.metadata.create_all(engine)
