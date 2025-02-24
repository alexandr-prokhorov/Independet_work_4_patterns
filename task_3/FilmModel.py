import json


class Film:
    def __init__(self):
        """
        Функция инициализирует пустой список для добавления информации о фильме.
        """
        self.films = []

    def get_film(self):
        """
        Функция возвращает список фильмов.
        :return: Возвращает список фильмов.
        """
        return self.films

    def add_film(self, name, genre, director, year_of_release, duration, studio, actors, filename):
        """
        Функция добавляет информацию о фильме в список.
        :param name: Название фильма.
        :param genre: Жанр.
        :param director: Режиссер.
        :param year_of_release: Год выпуска.
        :param duration: Длительность.
        :param studio: Студия.
        :param actors: ФИО актера и его роль.
        :param filename: Название файла для сохранения.
        :return: Возвращает информацию о добавлении.
        """
        film = {"Название": name, "Жанр": genre, "Режиссер": director, "Год выпуска": year_of_release,
                "Длительность": duration, "Студия": studio, "Актеры": actors}
        self.films.append(film)
        self.update_json(filename)
        return True

    def remove_film(self, name, filename):
        """
        Функция удаляет информацию о фильме из списка по его названию.
        :param name: Название фильма.
        :param filename: Название файла для изменения.
        :return: Возвращает информацию об удалении.
        """
        for film in self.films:
            if film["Название"] in name:
                self.films.remove(film)
                self.update_json(filename)
                return True
        return f"Фильм {name} не найден."

    def update_json(self, filename):
        """
        Функция сохраняет список в файл JSON.
        :param filename: Название файла для сохранения.
        """
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.films, file, ensure_ascii=False, indent=4)
