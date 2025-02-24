class FilmView:

    def __init__(self, controller):
        self.controller = controller

    def display_get_film(self):
        """
        Функция выводит список фильмов.
        """
        films = self.controller.get_film()
        if films:
            for film in films:
                print(film)
        else:
            print("Список фильмов пуст.")

    def display_add_film(self, name, genre, director, year_of_release, duration, studio, actors, filename,
                         user_role="guest"):
        """
        Функция выводит результат добавления фильма в список после проверки прав.
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
        result = self.controller.add_film(name, genre, director, year_of_release, duration, studio, actors, filename,
                                          user_role)
        if result == "Forbidden!":
            print(result)
        elif result is True:
            print(f"Фильм: {name} успешно добавлен.")
        else:
            print(result)

    def display_remove_film(self, name, filename, user_role="guest"):
        """
        Функция возвращает результат удаления фильма после проверки прав.
        :param name: Название фильма.
        :param filename: Название файла для изменения.
        :param user_role: Тип пользователя.
        :return: Возвращает результат удаления фильма.
        """
        result = self.controller.remove_film(name, filename, user_role)
        if result == "Forbidden!":
            print(result)
        elif result is True:
            print(f"Фильм: {name} успешно удален.")
        else:
            print(result)
