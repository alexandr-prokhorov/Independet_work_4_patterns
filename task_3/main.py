from FilmModel import Film
from FilmController import FilmController
from FilmView import FilmView

if __name__ == '__main__':
    filename = "films.json"
    guest = "guest"
    user = 'user_owner'
    staff = 'is_staff'
    superuser = 'super_staff'

    model = Film()
    controller = FilmController(model)
    view = FilmView(controller)

    print()
    # Проверяю добавление в список разными пользователями
    view.display_add_film(
        name="Форрест Гамп ",
        genre="Драма",
        director="Роберт Земекис",
        year_of_release="1994",
        duration="2ч22мин",
        studio="Paramount",
        actors=[
            "Том Хэнкс - Форрест Гамп",
            "Робин Райт - Дженни Каррен",
            "Салли Филд - Миссис Гамп",
            "Гэри Синиз - Лейтенант Дэн Тейлор",
            "Майкелти Уильямсон - Бубба Блу "
        ],
        filename=filename,
        user_role=superuser)
    view.display_add_film(
        name="Пролетая над гнездом кукушки",
        genre="драма",
        director="Милош Форман",
        year_of_release="1975",
        duration="2ч14мин",
        studio="Fantasy Films",
        actors=[
            "Джек Николсон - Рэндл Патрик Макмёрфи",
            " Луиза Флетчер - Медсестра Милдред Рэтчед",
            "Уилл Сэмпсон - Вождь Бромден",
            "Уильям Редфилд - Дейл Хардинг",
            "Дэнни ДеВито - Мартинчетти"
        ],
        filename=filename,
        user_role=staff)
    view.display_add_film(
        name="Побег из Шоушенка",
        genre="Драма",
        director="Фрэнк Дарабонт",
        year_of_release="1994",
        duration="2ч22мин",
        studio="Castle Rock Entertainment",
        actors=[
            "Тим Роббинс - Энби Дюфрейн",
            "Морган Фриман - Эллис Бойд 'Рэд' Рэддинг",
            "Боб Гантон - Начальник тюрьмы Сэмюэл Нортон",
            "Уильям Сэдлер - Хейвуд"
        ],
        filename=filename,
        user_role=user)
    view.display_add_film(
        name="Побег из Шоушенка",
        genre="Драма",
        director="Фрэнк Дарабонт",
        year_of_release="1994",
        duration="2ч22мин",
        studio="Castle Rock Entertainment",
        actors=[
            "Тим Роббинс - Энби Дюфрейн",
            "Морган Фриман - Эллис Бойд 'Рэд' Рэддинг",
            "Боб Гантон - Начальник тюрьмы Сэмюэл Нортон",
            "Уильям Сэдлер - Хейвуд"
        ],
        filename=filename,
        user_role=guest)
    print()
    # Вывожу список после добавления.
    view.display_get_film()
    print()
    # Проверяю удаление из списка пользователями.
    view.display_remove_film("Побег из Шоушенка", filename, user)
    view.display_remove_film("Побег из Шоушенка", filename, guest)
    view.display_remove_film("Побег из Шоушенка", filename, staff)
    view.display_remove_film("Побег из Шоушенка", filename, superuser)
    print()
    # Вывожу список после удаления.
    view.display_get_film()
