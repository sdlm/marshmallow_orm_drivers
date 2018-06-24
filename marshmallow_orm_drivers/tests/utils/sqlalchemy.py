from marshmallow_orm_drivers.tests.models.sqlalchemy import get_model
from marshmallow_orm_drivers.tests.utils.abstract import MyQuerySet


class SQLAlchemyQuerySet(MyQuerySet):

    get_model_by_name = get_model

    def get(self, **kwargs):
        ...

    def exists(self, **kwargs):
        ...

    def count(self, **kwargs):
        ...

    def create(self, **kwargs):
        ...
