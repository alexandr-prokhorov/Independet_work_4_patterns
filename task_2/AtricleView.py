class ArticleView:

    def __init__(self, controller):
        self.controller = controller

    def display_article(self, ):
        """
        Функция выводит список статей.
        """
        result = self.controller.get_article()
        if result:
            for item in result:
                print(f'"Название": {item["Название"]}, "Автор": {item["Автор"]}, '
                      f'"Количество знаков": {item["Количество знаков"]}, '
                      f'"Впервые опубликована": {item["Впервые опубликована"]},'
                      f' "Краткое описание": {item["Краткое описание"]} ')
        else:
            print("Нет данных.")

    def display_add_article(self, name_article, author, number_of_characters, publication, description, filename,
                            user_role="guest"):
        """
        Функция выводит результат добавления статьи в список после проверки прав.
        :param name_article: Название статьи.
        :param author: Автор статьи.
        :param number_of_characters: Количество символов.
        :param publication: Где впервые опубликована.
        :param description: Краткое описание.
        :param filename: Название файла для сохранения.
        :param user_role: Тип пользователя.
        :return: Возвращает результат добавления статьи.
        """
        result = self.controller.add_article(name_article, author, number_of_characters, publication, description,
                                             filename, user_role)
        if result == "Forbidden!":
            print(result)
        elif result is True:
            print(f"Статья: {name_article} успешно добавлена.")
        else:
            print(result)

    def display_remove_article(self, name_article, filename, user_role="guest"):
        """
        Функция возвращает результат удаления статьи после проверки прав.
        :param name_article: Название статьи.
        :param filename: Название файла для изменения.
        :param user_role: Тип пользователя.
        :return: Возвращает результат удаления статьи.
        """
        result = self.controller.remove_article(name_article, filename, user_role)
        if result == "Forbidden!":
            print(result)
        elif result is True:
            print(f"Статья: {name_article} успешно удалена.")
        else:
            print(result)
