from marshmallow import fields

import marshmallow_orm_drivers as orm_drivers
from marshmallow_orm_drivers.tests.models.sqlalchemy import Tag, Post, User


class SQLAlchemyUserSchema(orm_drivers.SQLAlchemyModelSchema):
    name = fields.String(attribute='username')

    class Meta:
        model = User


class SQLAlchemyTagSchema(orm_drivers.SQLAlchemyModelSchema):
    term = fields.String(attribute='name')

    class Meta:
        model = Tag


class SQLAlchemyEntrySchema(orm_drivers.SQLAlchemyModelSchema):
    title = fields.String()
    summary = fields.String(attribute='text')
    link = fields.Url(attribute='url')
    hash = fields.String(attribute='hash')

    author = fields.Nested(SQLAlchemyUserSchema)
    tags = fields.Nested(SQLAlchemyTagSchema, many=True)

    class Meta:
        model = Post


def get_schema(model_name: str):
    assert model_name in ['user', 'tag', 'post']
    switch = {
        'user': SQLAlchemyUserSchema,
        'tag': SQLAlchemyTagSchema,
        'post': SQLAlchemyEntrySchema,
    }
    return switch[model_name]
