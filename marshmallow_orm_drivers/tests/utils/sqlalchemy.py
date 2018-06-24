from marshmallow_orm_drivers.tests.models.sqlalchemy import session
from marshmallow_orm_drivers.tests.utils.abstract import MyQuerySet


class SQLAlchemyQuerySet(MyQuerySet):

    def get_query(self, **kwargs):
        return session.query(self.model).filter_by(**kwargs)

    def get(self, **kwargs):
        return self.get_query(**kwargs).first()

    def exists(self, **kwargs):
        return self.get_query(**kwargs).count() > 0

    def count(self, **kwargs):
        return self.get_query(**kwargs).count()

    def create(self, **kwargs):
        ed_user = self.model(**kwargs)
        session.add(ed_user)
        session.commit()

    def values_of_field(self, field_name):
        return list(session.query(getattr(self.model, field_name)))
