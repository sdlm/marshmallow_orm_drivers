from marshmallow import fields

import marshmallow_orm_drivers as orm_drivers
from marshmallow_orm_drivers.tests.models.pony import Tag, Post, User


class PonyUserSchema(orm_drivers.PonyModelSchema):
    name = fields.String(attribute='username')

    class Meta:
        model = User


class PonyTagSchema(orm_drivers.PonyModelSchema):
    term = fields.String(attribute='name')

    class Meta:
        model = Tag


class PonyEntrySchema(orm_drivers.PonyModelSchema):
    title = fields.String()
    summary = fields.String(attribute='text')
    link = fields.Url(attribute='url')
    hash = fields.String(attribute='hash')

    author = fields.Nested(PonyUserSchema)
    tags = fields.Nested(PonyTagSchema, many=True)

    class Meta:
        model = Post


def get_schema(model_name: str):
    assert model_name in ['user', 'tag', 'post']
    switch = {
        'user': PonyUserSchema,
        'tag': PonyTagSchema,
        'post': PonyEntrySchema,
    }
    return switch[model_name]
