from unittest import TestCase

from faker import Faker


class SchemaTests(TestCase):
    user_schema = None

    # noinspection PyUnresolvedReferences
    def setUp(self):
        model_user = self.get_model('user')
        self.user_qs = self.qs(model_user)

        model_tag = self.get_model('tag')
        self.tag_qs = self.qs(model_tag)

        user_schema_cls = self.get_schema('user')
        self.user_schema = user_schema_cls()

        post_schema_cls = self.get_schema('post')
        self.post_schema = post_schema_cls()

    def test_basic(self):
        fake = Faker()
        name = fake.user_name()
        self.load_user(data={'name': name})
        self.assertTrue(self.user_qs.exists(username=name))

    def test_fk_relation(self):
        entry = get_fake_entry()
        del entry['tags']
        self.load_entry(entry)
        name = entry['author']['name']
        self.assertTrue(self.user_qs.exists(username=name))

    def test_m2m_relation(self):
        entry = get_fake_entry(tags_count=5)
        tag_names = {x['term'] for x in entry['tags']}
        self.load_entry(entry)
        self.assertEqual(set(self.tag_qs.values_of_field('name')), tag_names)

    def load_entries(self, entries):
        for entry in entries:
            self.load_entry(entry)

    def load_entry(self, entry):
        self.post_schema.load(entry)

    def load_user(self, data):
        self.user_schema.load(data)


def get_fake_entry(tags_count: int = 1, link: str = None) -> dict:
    fake = Faker()
    return {
        'title': fake.sentence(),
        'summary': fake.text(),
        'author': {'name': fake.user_name()},
        'tags': [{'term': fake.word()} for _ in range(tags_count)],
        'link': link or fake.url()
    }
