from typing import List

from sqlalchemy import (
    Column,
    Integer,
    String,
    DATETIME
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from database_adapter.database import engine

Base = declarative_base()


class DataPost(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)

    company_name = Column(String)
    date = Column(Integer)
    resource = Column(String)
    title = Column(String)
    link = Column(String, unique=True)
    category = Column(String)
    doc = Column(String)


Base.metadata.create_all(engine)


class BasePost(BaseModel):
    company_name: str
    date: int
    resource: str
    title: str
    link: str
    category: str
    doc: str

    class Config:
        orm_mode = True


class PostSeries(BaseModel):
    number_of_posts: int = 0
    series: List[BasePost] = []
