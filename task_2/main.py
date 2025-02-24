from ArticleModel import Article
from ArticleController import ArticleController
from AtricleView import ArticleView

if __name__ == '__main__':
    filename = "articles.json"
    guest = "guest"
    user = 'user_owner'
    staff = 'is_staff'
    superuser = 'super_staff'

    model = Article()
    controller = ArticleController(model)
    view = ArticleView(controller)

    print()
    # Проверяю добавление в список разными пользователями
    view.display_add_article("Эволюция современного искусства в XXI веке", "Сара Томпсон",
                             "10,200", "Искусство и Культура",
                             "Статья рассматривает ключевые тренды и направления в современном искусстве,"
                             " анализируя его развитие и влияние на общество.", filename, superuser)
    view.display_add_article("Эволюция современного искусства в XXI веке", "Сара Томпсон",
                             "10,200", "Искусство и Культура",
                             "Статья рассматривает ключевые тренды и направления в современном искусстве,"
                             " анализируя его развитие и влияние на общество.", filename, guest)
    view.display_add_article("Языковые модели ИИ: как ChatGPT и другие меняют коммуникацию",
                             "Алексей Морозов", "14,500", "Цифровые технологии",
                             " В статье анализируется, как языковые модели ИИ, такие как ChatGPT, "
                             "трансформируют общение, поддержку клиентов и создание контента.", filename, user)
    view.display_add_article("Нейронные сети: как они работают и где применяются", "Анна Воронова",
                             "13,500", "Философия и технологии",
                             "В статье рассматриваются этические вопросы, связанные с развитием ИИ, включая "
                             "проблемы конфиденциальности, безопасности и ответственности.", filename, staff)
    print()
    # Вывожу список после добавления.
    view.display_article()
    print()
    # Проверяю удаление из списка пользователями.
    view.display_remove_article("Эволюция современного искусства в XXI веке", filename, guest)
    view.display_remove_article("Эволюция современного искусства в XXI веке", filename, user)
    view.display_remove_article("Эволюция современного искусства в XXI веке", filename, superuser)
    view.display_remove_article("Эволюция современного искусства в XXI веке", filename, superuser)
    print()
    # Вывожу список после удаления.
    view.display_article()
