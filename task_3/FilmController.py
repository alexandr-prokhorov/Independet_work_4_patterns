class FilmController:
    def __init__(self, model):
        self.model = model

    def get_film(self):
        """
        Функция выводит информацию из списка фильмов. Смотреть могут все пользователи.
        :return: Возвращает список фильмов.
        """
        return self.model.get_film()

    def add_film(self, name, genre, director, year_of_release, duration, studio, actors, filename, user_role="guest"):
        """
        Функция ограничивает права на добавление фильмов в список, добавлять могу админ, модератор, а так же
        зарегистрированный пользователь.
        :param name: Название фильма.
        :param genre: Жанр.
        :param director: Режиссер.
        :param year_of_release: Год выпуска.
        :param duration: Длительность.
        :param studio: Студия.
        :param actors: ФИО актера и его роль.
        :param filename: Название файла для сохранения.
        :param user_role: Тип пользователя.
        :return: Возвращает результат добавления фильма.
        """
        if user_role not in ["super_staff", "is_staff", "user_owner"]:
            return "Forbidden!"
        else:
            return self.model.add_film(name, genre, director, year_of_release, duration, studio, actors, filename)

    def remove_film(self, name, filename, user_role="guest"):
        """
        Функция ограничивает права на удаления фильма из списка, удалять могут админ, модератор.
        :param name: Название фильма.
        :param filename: Название файла для изменения.
        :param user_role: Тип пользователя.
        :return: Возвращает результат удаления фильма.
        """
        if user_role not in ["super_staff", "is_staff"]:
            return "Forbidden!"
        else:
            return self.model.remove_film(name, filename)
