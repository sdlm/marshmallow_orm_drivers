from marshmallow_orm_drivers.tests.models.sqlalchemy import get_model
from marshmallow_orm_drivers.tests.serializers.sqlalchemy import get_schema
from marshmallow_orm_drivers.tests.tests import SchemaTests
from marshmallow_orm_drivers.tests.utils.sqlalchemy import SQLAlchemyQuerySet


class SQLAlchemySchemaTests(SchemaTests):

    def setUp(self):
        self.get_schema = get_schema
        self.qs = SQLAlchemyQuerySet
        self.get_model = get_model
        super().setUp()
