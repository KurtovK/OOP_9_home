#Задание 1.
#Создайте класс для перевода из метрической системы в английскую и
#наоборот. Функциональность необходимо реализовать в виде статических
#методов.

class MetricConverter:
    @staticmethod
    def meters_to_feet(meters: float) -> float:
        """
        Переводит метры в футы
        :param meters: метры
        :return:
                футы
        """
        return meters * 3.28084

    @staticmethod
    def feet_to_meters(feet: float) -> float:
        """
        Переводит футы в метры
        :param feet: футы
        :return:
                метры
        """
        return feet / 3.28084

    @staticmethod
    def kilometers_to_miles(kilometers: float) -> float:
        """
        Преобразует километры в мили
        :param kilometers (float): Километры
        :return:
                float: Мили
        """
        return kilometers * 0.62137

def execute_application():
    pass





if __name__=="__main__":
    execute_application()