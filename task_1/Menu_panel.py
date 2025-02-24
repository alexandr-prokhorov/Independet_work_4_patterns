from data_handler import Menu_pizza, Ingredients
from Pizza_factory import PizzaFactory
from order_manager import OrderManager
from Admin_panel import AdminPanel


def main():
    """
    Функция реализует работу меню приложения, содержит меню заказа для клиента и меню администратора.
    """
    order_manager = OrderManager()

    while True:
        print("\nГЛАВНОЕ МЕНЮ")
        print("1. Клиент")
        print("2. Администратор")
        print("3. Выход.")
        user = input("Введите кто вы: ")
        if user == "1":
            while True:
                print("\nМЕНЮ ЗАКАЗА!")
                print("1. Выбрать пиццу из меню")
                print("2. Создать свою пиццу")
                print("3. Выход")
                choice = input("Выберите действие: ")

                if choice == "1":
                    PizzaFactory.show_menu()
                    pizza_type = input("Введите название пиццы: ").strip()

                    if pizza_type not in Menu_pizza:
                        print("Пицца не найдена!")
                        continue

                    available_toppings = [
                        t for t in Ingredients
                        if t not in Menu_pizza[pizza_type]["ingredients"]
                    ]

                    toppings = []
                    if available_toppings:
                        print("\nДоступные топпинги:")
                        for t in available_toppings:
                            print(f"- {t} ({Ingredients[t]} руб.)")
                        selected = input("Введите топпинги через запятую: ").split(",")
                        toppings = []
                        for t in selected:
                            stripped_t = t.strip()
                            if stripped_t in available_toppings:
                                toppings.append(stripped_t)

                    pizza = PizzaFactory.create_pizza(pizza_type, toppings)
                    if pizza:
                        order_manager.add_order(pizza)
                        print(f"\nПицца '{pizza.name}' заказана!")
                        print(f"Состав: {', '.join(pizza.toppings)}")
                        print(f"Цена: {pizza.calculate_price()} руб.")
                elif choice == "2":
                    pizza = PizzaFactory.create_custom()
                    if pizza:
                        order_manager.add_order(pizza)
                        print(f"\nСоздана пицца '{pizza.name}'!")
                        print(f"Состав: {', '.join(pizza.toppings)}")
                        print(f"Цена: {pizza.calculate_price()} руб.")

                elif choice == "3":
                    print("До свидания!")
                    break

        elif user == "2":
            while True:
                print("\nМЕНЮ АДМИНИСТРАТОРА.")
                print("1. Статистика продаж.")
                print("2. Работа с меню пицц.")
                print("3. Выход.")
                choice = input("Выберите действие.")

                if choice == "1":
                    order_manager.show_stats()

                elif choice == "2":
                    AdminPanel.main_menu()
                elif choice == "3":
                    print("Вы вышли из панели администратора.")
                    break
        elif user == "3":
            print("Всего доброго!")
            break


if __name__ == '__main__':
    main()
