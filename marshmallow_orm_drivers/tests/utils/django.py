from marshmallow_orm_drivers.tests.models.django import get_model
from marshmallow_orm_drivers.tests.utils.abstract import MyQuerySet


class DjangoQuerySet(MyQuerySet):

    get_model_by_name = get_model

    def get(self, **kwargs):
        return self.model.objects.get(**kwargs)

    def exists(self, **kwargs):
        return self.model.objects.filter(**kwargs).exists()

    def count(self, **kwargs):
        return self.model.objects.filter(**kwargs).count()

    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)
