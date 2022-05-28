import json

import conf
import Fields

MODEL = conf.var


def generator() -> dict:
    dict_books = {"title": Fields.Title(),
                  "Year": Fields.Year(),
                  "pages": Fields.pages(),
                  "isbn13": Fields.isbn13(),
                  "rating": Fields.rating(),
                  "price": Fields.price(),
                  "Autor": Fields.author()}
    return dict_books


def main(amount: int) -> json:  # amount - количество книг, которые хотели бы записать в файл
    pk = 1
    for _ in range(amount):
        dict_book = {"Model": MODEL, "pk": pk, "fields": generator()}
        file = "Books.json"
        with open(file, "a", encoding="utf-8") as f:
            json.dump(dict_book, f, indent=4, ensure_ascii=False)
        pk += 1


if __name__ == '__main__':
    main(100)
