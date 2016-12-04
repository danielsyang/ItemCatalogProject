from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    category = Column(String(250), nullable=False)    
