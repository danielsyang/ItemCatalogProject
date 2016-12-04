from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from user import User
from category import Category

Base = declarative_base()

class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    user_login = Column(String(250), ForeignKey('user.user_login'))
    user = relationship(User)
    category_id = Column(String(250), ForeignKey('cat.category_id'))
    cat = relationship(Category)
