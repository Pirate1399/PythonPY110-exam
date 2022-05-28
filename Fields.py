import random

from faker import Faker


def Title() -> str:
    list_ = []
    with open('books.txt', "r", encoding="utf-8") as file:
        for i in file:
            list_.append(i.strip())
    title = random.choice(list_)
    return title


def Year() -> int:
    year = random.randint(1750, 2020)
    return year


def pages() -> int:
    pages = random.randint(15, 350)
    return pages


def isbn13() -> str:
    fake = Faker()
    num = fake.isbn13()
    return num


def rating() -> float:
    rating = random.uniform(0, 5)
    return round(rating, 1)


def price() -> float:
    price = random.uniform(1, 100000)
    return price


def author() -> list:
    fake = Faker('ru_RU')
    list_autors = []
    for _ in range(random.randint(1, 3)):
        list_autors.append(fake.name())
    return list_autors
