from datetime import datetime
from pony.orm import *


db = Database()
db.bind(provider='sqlite', filename=':memory:', create_db=True)


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Required(str)
    posts = Set('Post')


class Tag(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    posts = Set('Post')


class Post(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Optional(str)
    text = Optional(str)
    author = Optional(User)
    tags = Set(Tag)
    url = Optional(str, unique=True)
    hash = Optional(str, unique=True)
    created = Optional(datetime)


db.generate_mapping(create_tables=True)


def get_model(model_name: str):
    assert model_name in ['user', 'tag', 'post']
    switch = {
        'user': User,
        'tag': Tag,
        'post': Post,
    }
    return switch[model_name]
