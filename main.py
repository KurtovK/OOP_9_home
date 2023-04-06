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

    @staticmethod
    def miles_to_kilometers(miles: float) -> float:
        """
        Преобразует мили в километры
        :param miles (float): Мили
        :return:
                float: Километры
        """
        return miles * 1.609344
def execute_application():
    meters = float(input("Введите значение в метрах: "))
    feet = MetricConverter.meters_to_feet(meters)
    print(f"{meters} метров равно {feet:.01f} футов.")

    feet = float(input("Введите значение в футах: "))
    meters = MetricConverter.feet_to_meters(feet)
    print(f"{feet} футов равно {meters:.01f} метров.")

    kilometers = float(input("Введите значение в километрах: "))
    miles = MetricConverter.kilometers_to_miles(kilometers)
    print(f"{kilometers} километров равно {miles:.01f} миль.")

    miles = float(input("Введите значение в милях: "))
    kilometers = MetricConverter.miles_to_kilometers(kilometers)
    print(f"{miles} миль равно {kilometers:.01f} километров.")





if __name__=="__main__":
    execute_application()