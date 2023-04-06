#Задание 1.
#Создайте класс для конвертирования температуры из Цельсия в
#Фаренгейт и наоборот. У класса должно быть два статических метода: для
#перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий.
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """
        Подсчитывает градусы Фаренгейта, из полученных из градусов Цельсия
        :param celsius: градусы Цельсия
        :return:
                градусы Фаренгейта
        """
        return (celsius * 9/5) + 32

def execute_application():
    pass





if __name__=="__main__":
    execute_application()