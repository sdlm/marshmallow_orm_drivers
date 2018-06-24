from django.contrib.auth.models import User
from marshmallow import fields

import marshmallow_orm_drivers as orm_drivers
from marshmallow_orm_drivers.tests.models.django import Tag, Post


class DjangoUserSchema(orm_drivers.DjangoModelSchema):
    name = fields.String(attribute='username')

    class Meta:
        model = User


class DjangoTagSchema(orm_drivers.DjangoModelSchema):
    term = fields.String(attribute='name')

    class Meta:
        model = Tag


class DjangoEntrySchema(orm_drivers.DjangoModelSchema):
    title = fields.String()
    summary = fields.String(attribute='text')
    link = fields.Url(attribute='url')
    hash = fields.String(attribute='hash')

    author = fields.Nested(DjangoUserSchema)
    tags = fields.Nested(DjangoTagSchema, many=True)

    class Meta:
        model = Post


def get_schema(model_name: str):
    assert model_name in ['user', 'tag', 'post']
    switch = {
        'user': DjangoUserSchema,
        'tag': DjangoTagSchema,
        'post': DjangoEntrySchema,
    }
    return switch[model_name]
