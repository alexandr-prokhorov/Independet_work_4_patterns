from data_handler import Menu_pizza, Ingredients
from abc import ABC, abstractmethod


class Pizza(ABC):
    """
    Класс для предоставления пиццы.
    """

    def __init__(self, name, base_price, cost_price, toppings=None):
        """
        Функция инициализирует объект пиццы.
        :param name: Название пиццы
        :param base_price: Цена пиццы при продаже.
        :param cost_price: Себестоимость приготовления пиццы.
        :param toppings: Добавки к пиццам.
        """
        self.name = name
        self.base_price = base_price
        self.cost_price = cost_price
        self.toppings = toppings if toppings else []

    @abstractmethod
    def calculate_price(self):
        """
        Функция расчета полной стоимости.
        """
        pass

    def calculate_profit(self):
        """
        Функция рассчитывает прибыл при продаже пиццы.
        :return: Возвращает разницу между ценой при продаже и себестоимости.
        """
        return self.calculate_price() - self.cost_price


class CustomPizza(Pizza):
    """
    Класс для пиццы которую собирает пользователь
    """

    def calculate_price(self):
        """
        Функция рассчитывает стоимость пиццы собранной пользователем.
        :return: Возвращает итоговую стоимость.
        """
        return self.base_price + sum(Ingredients.get(t, 0) for t in self.toppings)


class PizzaFactory:
    """
    Класс фабрики для создания пиццы
    """

    @staticmethod
    def create_pizza(pizza_type, toppings=None):
        """
        Функция создания пиццы из меню.
        :param pizza_type: Тип пиццы из меню
        :param toppings: Добавки к пицце, по желанию клиента, по умолчанию None.
        :return: Возвращает Объект пиццы если она есть в меню или None если нет.
        """
        if pizza_data := Menu_pizza.get(pizza_type):
            return CustomPizza(
                pizza_data["name"],
                pizza_data["base_price"],
                pizza_data["cost_price"],
                toppings or []
            )
        return None

    @staticmethod
    def create_custom():
        """
        Функция создания пиццы пользователем.
        :return: Возвращает объект пиццы созданной пользователем или None, если пользователь не выбрал ингредиенты
        """
        print("\nСоздание своей пиццы:")
        print("Доступные ингредиенты:")
        for ingr, price in Ingredients.items():
            print(f"- {ingr} ({price} руб.)")

        selected = input("Введите ингредиенты через запятую: ").split(",")
        ingredients = []
        for i in selected:
            stripped_i = i.strip()
            if stripped_i in Ingredients:
                ingredients.append(stripped_i)

        if not ingredients:
            print("Нужно выбрать хотя бы 1 ингредиент!")
            return None

        return CustomPizza("Моя пицца", 100, 50, ingredients)

    @staticmethod
    def show_menu():
        """
        Функция показывает меню пиццы.
        :return: Возвращает меню, если файл с пиццами пуст возвращает "Меню пустое!"
        """
        if not Menu_pizza:
            print("Меню пустое!")
            return

        print("\nМЕНЮ ПИЦЦЕРИИ")
        for name, data in Menu_pizza.items():
            print(f"\n{name} - {data['base_price']} руб.")
            print(f"Состав: {', '.join(data['ingredients'])}")
