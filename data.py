import requests


def get_data(count):
    return requests.get(
        f'http://api.randomdatatools.ru?count={count}&params=LastName,FirstName,City,Address'
    ).json()
