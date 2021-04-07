import os
from models import DATABASE_NAME, Client, Order


def test_database_exists():
    os.system('cd ..')
    os.system('python executor.py init')
    assert os.path.exists(DATABASE_NAME)


def test_columns_exists():
    if len(Order.select()) == 0 and len(Client.select()) == 0:
        os.system('cd ..')
        os.system('python executor.py fill')
    assert Order.select() and Client.select()


def test_limit_on_lines():
    assert len(Order.select()) >= 10 and len(Client.select()) >= 10
