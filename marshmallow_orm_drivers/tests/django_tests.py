from marshmallow_orm_drivers.tests.models.django import get_model
from marshmallow_orm_drivers.tests.serializers.django import get_schema
from marshmallow_orm_drivers.tests.tests import SchemaTests
from marshmallow_orm_drivers.tests.utils.django import DjangoQuerySet


class PonySchemaTests(SchemaTests):

    def setUp(self):
        self.get_schema = get_schema
        self.qs = DjangoQuerySet
        self.get_model = get_model
        super().setUp()
