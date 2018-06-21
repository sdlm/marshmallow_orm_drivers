# marshmallow_orm_drivers
За основу была взята библиотека [marshmallow](https://github.com/marshmallow-code/marshmallow), т.к. имеет простой интерфейс и легкую расширяемость.


### Пример использования
```
from marshmallow_orm_drivers import DjangoModelSchema

class NewsFeedSchema(DjangoModelSchema):
    title = fields.String()
    summary = fields.String(attribute='text')
    link = fields.Url(attribute='url')

    author = fields.Nested(UserSchema)
    tags = fields.Nested(TagSchema, many=True)

    class Meta:
        model = NewsFeed
```

### Поддерживаемые ORM
* DjangoORM

### Features
* `ManyToMany` fields
* `ForeignKey` fields
* fields with `unique=True`

### Схема БД
![marshmallow_orm_drivers_test_schema](https://rawgit.com/sdlm/test_app_for_integration_lib/master/static_files/marshmallow_orm_drivers_test_schema.png)

### В планах
* тесты для каждой ORM
* Поддержка SQLAlchemy
* reverse relation 
