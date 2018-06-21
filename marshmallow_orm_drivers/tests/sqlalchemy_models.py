from sqlalchemy import Column, Integer, String, Sequence, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(128))


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, Sequence('tag_id_seq'), primary_key=True)
    name = Column(String(50))


class Post(Base):
    id = Column(Integer, Sequence('post_id_seq'), primary_key=True)
    title = Column(String(512))
    text = Column(Text())
    author = relationship("User", back_populates="posts")
    tags = relationship("Tag", back_populates="posts")
    url = Column(String(512), unique=True)
    hash = Column(String(512), unique=True)
    created = Column(DateTime())
