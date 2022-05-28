import random

from faker import Faker


def title() -> str:
    """
    генерируется название книги из определенного списка
    :return: Название в виде str
    """
    list_ = []
    with open('books.txt', "r", encoding="utf-8") as file:
        for i in file:
            list_.append(i.strip())
    title = random.choice(list_)
    return title


def year() -> int:
    """
    генерируется год написания книги.
    Предполагается, что книга написана в последние 300 лет
    :return Год написания в виде числа:
    """
    year = random.randint(1750, 2020)
    return year


def pages() -> int:
    """
    генерируется количество страниц
    :return: число страниц в виде целого числа
    """
    pages = random.randint(15, 350)
    return pages


def isbn13() -> str:
    """
    генерируется международный код книги
    :return код-номер книги в виде строки:
    """
    fake = Faker()
    num = fake.isbn13()
    return num


def rating() -> float:
    """
    генерируется рейтинг книги. Рейтинг книги может быть от 0 до 5 включительно
    :return Рейтинг, float:
    """
    rating = random.uniform(0, 5)
    return round(rating, 1)


def price() -> float:
    """
    генерируется цена на книгу вплоть до копеек
    :return Цена, float:
    """
    price = random.uniform(1, 100000)
    return round(price,2)


def author() -> list:
    """
    Создается список авторов. Их может быть от одного до 3 человек
    :return: Авторы, list
    """
    fake = Faker('ru_RU')
    list_autors = []
    for _ in range(random.randint(1, 3)):
        list_autors.append(fake.name())
    return list_autors


