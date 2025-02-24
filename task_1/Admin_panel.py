from data_handler import Menu_pizza, Ingredients, save_json


class AdminPanel:
    """
    Клас для работы панели администратора.
    """

    @staticmethod
    def main_menu():
        """
        Функция для управления меню администратора.
        """
        while True:
            print("\nАДМИН-ПАНЕЛЬ")
            print("1. Управление пиццами")
            print("2. Управление ингредиентами")
            print("3. Выйти")
            choice = input("Выберите действие: ")

            if choice == "1":
                AdminPanel.manage_pizzas()
            elif choice == "2":
                AdminPanel.manage_ingredients()
            elif choice == "3":
                break
            else:
                print("Неверный ввод!")

    @staticmethod
    def manage_pizzas():
        """
        Функция управления пиццами администратором.
        """
        while True:
            print("\nУПРАВЛЕНИЕ ПИЦЦАМИ")
            print("1. Добавить пиццу")
            print("2. Удалить пиццу")
            print("3. Показать все пиццы")
            print("4. Назад")
            choice = input("Выберите действие: ")

            if choice == "1":
                AdminPanel.add_pizza()
            elif choice == "2":
                AdminPanel.delete_pizza()
            elif choice == "3":
                AdminPanel.show_pizzas()
            elif choice == "4":
                break
            else:
                print("Неверный ввод!")

    @staticmethod
    def add_pizza():
        """
        Функция добавления пиццы в меню администратором.
        :return: Возвращает результат добавления пиццы в меню.
        """
        print("\nДОБАВЛЕНИЕ ПИЦЦЫ")
        name = input("Название: ").strip()

        if name in Menu_pizza:
            print("Такая пицца уже есть в меню!")
            return

        try:
            base = float(input("Базовая цена: "))
            cost = float(input("Себестоимость: "))
        except ValueError:
            print("Некорректная сумма!")
            return

        print("Доступные ингредиенты:", ", ".join(Ingredients.keys()))
        ings = input("Ингредиенты через запятую: ").split(",")
        valid_ings = []
        for i in ings:
            stripped_i = i.strip()
            if stripped_i in Ingredients:
                valid_ings.append(stripped_i)
        Menu_pizza[name] = {
            "name": name,
            "base_price": base,
            "cost_price": cost,
            "ingredients": valid_ings
        }
        save_json("menu_pizza.json", Menu_pizza)
        print("Пицца успешно добавлена!")

    @staticmethod
    def delete_pizza():
        """
        Функция удаляет пиццу из меню администратором.
        :return:
        """
        print("\nУДАЛЕНИЕ ПИЦЦЫ")
        AdminPanel.show_pizzas()
        name = input("Название пиццы: ").strip()

        if name in Menu_pizza:
            del Menu_pizza[name]
            save_json("menu_pizza.json", Menu_pizza)
            print("Пицца удалена!")
        else:
            print("Пицца не найдена!")

    @staticmethod
    def show_pizzas():
        """
        Функция показывает все пиццы которые есть в меню.
        :return: Возвращает список пицц или сообщение "Меню пустое!" если список пуст.
        """
        if not Menu_pizza:
            print("Меню пустое!")
            return

        for name, data in Menu_pizza.items():
            print(f"\n{name} - {data['base_price']} руб.")
            print("Ингредиенты:", ", ".join(data['ingredients']))

    @staticmethod
    def manage_ingredients():
        """
        Функция для меню управления ингредиентами администратором.
        :return:
        """
        while True:
            print("\nУПРАВЛЕНИЕ ИНГРЕДИЕНТАМИ")
            print("1. Добавить ингредиент")
            print("2. Удалить ингредиент")
            print("3. Показать все ингредиенты")
            print("4. Назад")
            choice = input("Выберите действие: ")

            if choice == "1":
                AdminPanel.add_ingredient()
            elif choice == "2":
                AdminPanel.delete_ingredient()
            elif choice == "3":
                AdminPanel.show_ingredients()
            elif choice == "4":
                break
            else:
                print("Неверный ввод!")

    @staticmethod
    def add_ingredient():
        """
        Добавление ингредиента администратором.
        :return: Возвращает результат добавления.
        """
        print("\nДОБАВЛЕНИЕ ИНГРЕДИЕНТА")
        name = input("Название: ").strip()

        if name in Ingredients:
            print("Ингредиент уже существует!")
            return

        try:
            price = float(input("Стоимость: "))
        except ValueError:
            print("Некорректная сумма!")
            return

        Ingredients[name] = price
        save_json("ingredients.json", Ingredients)
        print("Ингредиент добавлен!")

    @staticmethod
    def delete_ingredient():
        """
        Функция удаления ингредиента из списка администратором.
        :return: Возвращает рещультат удаления.
        """
        print("\nУДАЛЕНИЕ ИНГРЕДИЕНТА")
        AdminPanel.show_ingredients()
        name = input("Название ингредиента: ").strip()

        if name not in Ingredients:
            print("Ингредиент не найден!")
            return

        del Ingredients[name]
        save_json("ingredients.json", Ingredients)
        print("Ингредиент удален!")

    @staticmethod
    def show_ingredients():
        """
        Функция показывает полный список ингредиентов.
        :return: Возвращает список ингредиентов либо "Список ингредиентов пуст!" если он пуст.
        """
        if not Ingredients:
            print("Список ингредиентов пуст!")
            return

        for ingr, price in Ingredients.items():
            print(f"- {ingr}: {price} руб.")
