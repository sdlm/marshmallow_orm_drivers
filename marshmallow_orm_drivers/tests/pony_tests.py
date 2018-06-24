from marshmallow_orm_drivers.tests.models.pony import get_model
from marshmallow_orm_drivers.tests.serializers.pony import get_schema
from marshmallow_orm_drivers.tests.tests import SchemaTests
from marshmallow_orm_drivers.tests.utils.pony import PonyQuerySet


class PonySchemaTests(SchemaTests):

    def setUp(self):
        self.get_schema = get_schema
        self.qs = PonyQuerySet
        self.get_model = get_model
        super().setUp()
