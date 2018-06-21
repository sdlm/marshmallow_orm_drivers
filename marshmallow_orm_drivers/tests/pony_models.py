from datetime import datetime
from pony.orm import *


db = Database()


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


db.generate_mapping()
