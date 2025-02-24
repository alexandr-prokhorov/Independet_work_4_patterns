import json


class Article:
    """
    Функция инициализирует пустой список для добавления информации о статье.
    """

    def __init__(self, ):
        self.articles = []

    def get_article(self):
        """
        Функция возвращает список со статьями.
        :return: Возвращает список статей.
        """
        return self.articles

    def add_article(self, name_article, author, number_of_characters, publication, description, filename):
        """
        Функция добавляет статью в список.
        :param name_article: Название статьи.
        :param author: Автор статьи.
        :param number_of_characters: Количество символов.
        :param publication: Где впервые опубликована.
        :param description: Краткое описание.
        :param filename: Название файла для сохранения.
        :return: Возвращает результат добавления.
        """
        article = {"Название": name_article, "Автор": author, "Количество знаков": number_of_characters,
                   "Впервые опубликована": publication, "Краткое описание": description}
        self.articles.append(article)
        self.update_json(filename)
        return True

    def remove_article(self, name_article, filename):
        """
        Функция удаляет статью из списка по ее названию.
        :param name_article: Название статьи.
        :param filename: Название файла для изменения.
        :return: Возвращает результат удаления.
        """
        for article in self.articles:
            if article["Название"] in name_article:
                self.articles.remove(article)
                self.update_json(filename)
                return True
        return f"Статья {name_article} не найдена."

    def update_json(self, filename):
        """
        Функция сохраняет список в файл JSON.
        :param filename: Название файла для сохранения.
        """
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(self.articles, fp, ensure_ascii=False, indent=4)
