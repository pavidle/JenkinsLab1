from peewee import (
    Model,
    CharField,
    ForeignKeyField,
    DateField,
    IntegerField,
    TextField
)
from peewee import SqliteDatabase

DATABASE_NAME = 'client.db'
database = SqliteDatabase(DATABASE_NAME)


class BaseModel(Model):
    class Meta:
        database = database

    @classmethod
    def get_fields(cls):
        return cls._meta.fields


class Client(BaseModel):
    name = CharField()
    city = CharField()
    address = CharField()


class Order(BaseModel):
    client = ForeignKeyField(Client, backref='orders')
    date = DateField()
    amount = IntegerField()
    description = TextField()
