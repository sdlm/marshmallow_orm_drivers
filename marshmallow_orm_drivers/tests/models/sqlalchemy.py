from sqlalchemy import Column, Integer, String, Sequence, DateTime, Text, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite://')  # in-memory database
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(128))
    posts = relationship('Post')


association_table = Table(
    'post_tag',
    Base.metadata,
    Column('tag_id', Integer, ForeignKey('tag.id')),
    Column('post_id', Integer, ForeignKey('post.id'))
)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, Sequence('tag_id_seq'), primary_key=True)
    name = Column(String(50))
    posts = relationship('Post', secondary='post_tag')


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, Sequence('post_id_seq'), primary_key=True)
    title = Column(String(512))
    text = Column(Text())

    author = Column(Integer, ForeignKey('user.id'), primary_key=True)

    tags = relationship('Tag', secondary=association_table)

    url = Column(String(512), unique=True)
    hash = Column(String(512), unique=True, nullable=True)
    created = Column(DateTime(), nullable=True)


Session = sessionmaker(engine)
session = Session()
Base.metadata.create_all(engine)


def get_model(model_name: str):
    assert model_name in ['user', 'tag', 'post']
    switch = {
        'user': User,
        'tag': Tag,
        'post': Post,
    }
    return switch[model_name]
