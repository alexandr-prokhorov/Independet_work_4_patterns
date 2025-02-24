import json


def load_json(filename):
    """
    Функция загружает данные из JSON файла.
    :param filename: Название файла загрузки.
    :return: Возвращает пустой словарь если файл не найден
    """
    try:
        with open(filename, "r", encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_json(filename, data):
    """
    Функция сохраняет данные в JSON файл.
    :param filename: Название файла для сохранения.
    :param data: Данные для сохранения.
    """
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# Меню с готовыми пиццами и их ценами и составом.
Menu_pizza = load_json("menu_pizza.json")
# Ингридиенты для топпингов и создания своей пиццы.
Ingredients = load_json("ingredients.json")
