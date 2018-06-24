from pony.orm import db_session, commit, count, exists

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
