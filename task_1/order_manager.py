from data_handler import load_json, save_json


class OrderManager:
    """
    Класс реализует чек с продажей, вывод статистики продаж.
    """

    def __init__(self):
        """
        Функция инициализирует объекты заказов, вычисляя общее количество, их полную стоимость и прибыль.
        """
        self.orders = load_json("orders.json") or []
        self.total = len(self.orders)
        self.revenue = sum(i["price"] for i in self.orders)
        self.profit = sum(i["profit"] for i in self.orders)

    def add_order(self, pizza):
        """
        Функция добавляет заказ в общий список заказов.
        """
        order = {
            "name": pizza.name,
            "price": pizza.calculate_price(),
            "profit": pizza.calculate_profit(),
            "toppings": pizza.toppings
        }
        self.orders.append(order)
        self.total += 1
        self.revenue += order["price"]
        self.profit += order["profit"]
        save_json("orders.json", self.orders)

    def show_stats(self):
        """
        Функция показывает общую статистику.
        """
        print("\nСТАТИСТИКА")
        print(f"Всего заказов: {self.total}")
        print(f"Общая выручка: {self.revenue} руб.")
        print(f"Чистая прибыль: {self.profit} руб.")
