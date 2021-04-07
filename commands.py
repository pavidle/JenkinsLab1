from models import Client, Order, database, BaseModel
from data import get_data
import random
import datetime

models = [Client, Order]


def init():
    if database.get_tables():
        database.drop_tables(models)
        print('База данных удалена')
        database.create_tables(models)
    else:
        database.create_tables(models)
    print('База данных создана')


def fill():
    if database.get_tables():
        for data in get_data(10):
            Client.create(
                name=data['LastName'] + " " + data['FirstName'],
                city=data['City'],
                address=data['Address']
            )
        for i in range(10):
            Order.create(
                client=Client.get_by_id(random.randint(1, 10)),
                date=datetime.datetime.now(),
                amount=random.randint(0, 30),
                description='some description'
            )
        print('База данных заполнена')


def show_help():
    print("""
        Запуск > python executor.py [параметр]

        Параметры:
        1. init - создаёт базу данных
        2. fill - заполняет базу данных некоторыми значениями
        3. show [table_name] - показывает указанную таблицу 
            """)


def show(table_name):
    model: BaseModel = globals()[table_name]
    print(*("{:<35}".format(name_column) for name_column in model.get_fields().keys()))
    for line in model.select():
        print(*("{:<35}".format(str(line.__dict__['__data__'][column])) for column in line.get_fields()))
