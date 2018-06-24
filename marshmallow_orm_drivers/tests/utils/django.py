from marshmallow_orm_drivers.tests.models.django import get_model
from marshmallow_orm_drivers.tests.utils.abstract import MyQuerySet


class DjangoQuerySet(MyQuerySet):

    def get_qs(self, **kwargs):
        return self.model.objects.filter(**kwargs)

    def get(self, **kwargs):
        return self.get_qs(**kwargs).first()

    def exists(self, **kwargs):
        return self.get_qs(**kwargs).exists()

    def count(self, **kwargs):
        return self.get_qs(**kwargs).count()

    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def values_of_field(self, field_name):
        return list(self.model.objects.values_list(field_name, flat=True))
