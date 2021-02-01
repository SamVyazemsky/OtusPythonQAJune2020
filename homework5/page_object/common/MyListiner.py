import datetime
from selenium.webdriver.support.events import AbstractEventListener


class MyListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        print(f'\n========= Ищем элемент. Тип селектора: {by} ', f'Путь до элемента: {value} =========')

    def after_find(self, by, value, driver):
        pass
        print(f"========= Элемент {value} - найден! =========")

    def before_click(self, element, driver):
        print(f"\n========= Кликаем по элементу - {element} =========")

    def after_click(self, element, driver):
        print(f"\n========= Клик по элементу {element} успешно совершен! =========")

    def before_change_value_of(self, element, driver):
        print(f"\n========= Изменяем элемент - {element} =========")

    def after_change_value_of(self, element, driver):
        print(f"\n========= Изменения элемента {element} прошло успешно =========")

    def on_exception(self, exception, driver):
        name_file = f"screenshots_{exception}_{datetime.time}.png"
        path = f'../screenshots/{name_file}'
        driver.save_screenshot(path)
        print(f"\n========= Произошла ошибка - {exception} =========")

    def before_quit(self, driver):
        print(f"\n========= Выполнения теста закончилось! =========")
        pass
