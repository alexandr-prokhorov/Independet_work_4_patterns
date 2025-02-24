class ArticleController:
    def __init__(self, model):
        self.model = model

    def get_article(self):
        """
        Функция выводит информацию из списка статей. Смотреть могут все пользователи.
        :return: Возвращает список статей.
        """
        return self.model.get_article()

    def add_article(self, name_article, author, number_of_characters, publication, description, filename,
                    user_role="guest"):
        """
        Функция ограничивает права на добавления статей в список, добавлять могу админ, модератор, а так же
        зарегистрированный пользователь.
        :param name_article: Название статьи.
        :param author: Автор статьи.
        :param number_of_characters: Количество символов.
        :param publication: Где впервые опубликована.
        :param description: Краткое описание.
        :param filename: Название файла для сохранения.
        :param user_role: Тип пользователя.
        :return: Возвращает результат добавления статьи.
        """
        if user_role not in ["super_staff", "is_staff", "user_owner"]:
            return "Forbidden!"
        else:
            return self.model.add_article(name_article, author, number_of_characters, publication, description,
                                          filename)

    def remove_article(self, name_article, filename, user_role="guest"):
        """
        Функция ограничивает права на удаления статей из списка, удалять могут админ, модератор.
        :param name_article: Название статьи.
        :param filename: Название файла для изменения.
        :param user_role: Тип пользователя.
        :return: Возвращает результат удаления статьи.
        """
        if user_role not in ["super_staff", "is_staff"]:
            return "Forbidden!"
        else:
            return self.model.remove_article(name_article, filename)
