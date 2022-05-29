from json import load as json_load, dump as json_dump, JSONDecodeError
from config import POST_PATH
from sys import getsizeof as gs
from flask import abort
from re import findall


class DataBase:
    def __init__(self, path: str = POST_PATH):
        self.path = path
        self.data = []

    def __repr__(self) -> str:
        return f"БД: {self.path}\nСодержит записей: {len(self.data)}\nРазмер БД: {gs(DataBase)}"

    def _json_loader(self):
        """
        Метод класса для загрузки json
        Обработка ошибок загрузки, чтения json

        """
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                return json_load(f)
        except FileNotFoundError:
            return abort(400)
        except JSONDecodeError:
            return abort(400)

    def database_loader(self):
        """
        Метод класса для заполнения данными экземлпяра класса

        """
        for line in self._json_loader():
            self.data.append(line)

    def json_write(self, data_to_write):
        """
        Метод класса запись в БД json
        :param data_to_write: данные для записи

        """
        database = self._json_loader()
        database.append(data_to_write)
        with open(self.path, 'w', encoding='utf-8') as f:
            json_dump(database, f, ensure_ascii=False, indent=2)

    def search_in_database(self, query: str) -> list:
        """
        Метод класса поиск в базе данных по вхождению строки в комментарии
        :param query: Строка поиска

        """
        output_data = []
        for line in self.data:
            if query.lower().strip() in line["content"].lower():  # findall(r"\w+", ):
                output_data.append(line)
        return output_data
