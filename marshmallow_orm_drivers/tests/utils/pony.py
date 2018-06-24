from pony.orm import db_session, commit, count, exists, select

from marshmallow_orm_drivers.tests.utils.abstract import MyQuerySet


class PonyQuerySet(MyQuerySet):

    @db_session
    def get(self, **kwargs):
        return self.model.get(**kwargs)

    @db_session
    def exists(self, **kwargs):
        return exists(s for s in self.model)

    @db_session
    def count(self, **kwargs):
        return count(s for s in self.model)

    @db_session
    def create(self, **kwargs):
        self.model(**kwargs)
        commit()

    @db_session
    def values_of_field(self, field_name):
        return list(select(getattr(o, field_name) for o in self.model))
