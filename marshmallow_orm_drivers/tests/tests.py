from unittest import TestCase

from faker import Faker


class SchemaTests(TestCase):
    user_schema = None

    # noinspection PyUnresolvedReferences
    def setUp(self):
        model_user = self.get_model('user')
        self.user_qs = self.qs(model_user)

        user_schema_cls = self.get_schema('user')
        self.user_schema = user_schema_cls()

    def test_basic(self):
        fake = Faker()
        name = fake.user_name()
        self.user_schema.load(data={'name': name})
        self.assertTrue(self.user_qs.exists(username=name))
