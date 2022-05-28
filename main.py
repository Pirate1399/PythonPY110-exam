import json

import conf
import Fields

MODEL = conf.var


def generator() -> dict:
    '''
    Генератор книги
    :return все данные о книге в виде dict:
    '''
    dict_books = {"title": Fields.title(),
                  "Year": Fields.year(),
                  "pages": Fields.pages(),
                  "isbn13": Fields.isbn13(),
                  "rating": Fields.rating(),
                  "price": Fields.price(),
                  "Autor": Fields.author()}
    return dict_books


def main(amount: int) -> json:
    """
    Функция нацелена на то, чтобы я получил зачет
     :param amount:количество книг, которые хотели бы записать в файл
     :return формирует файл json в котором хранятся сгенерированые нами книги:
    """
    pk = 1
    list_book = []
    for _ in range(amount):
        dict_book = {"Model": MODEL, "pk": pk, "fields": generator()}
        list_book.append(dict_book)
        pk += 1
    file = "Books.json"
    with open(file, "w", encoding="utf-8") as f:
        json.dump(list_book, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    main(100)
