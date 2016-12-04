from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_login = Column(String(250), primary_key=True)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)    
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
