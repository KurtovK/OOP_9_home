from typing import Dict, List
#Задача 1
#Создайте класс Passport (паспорт), который будет содержать
#паспортную информацию о гражданине страны. С помощью механизма
#наследования, реализуйте класс ForeignPassport (загран.паспорт)
#производный от Passport.
class Passport:
    def __init__(self, name : Dict[str, str], gender: str, date_birthday: Dict[str, str], place_birth: str):
        self.__name = name
        self.__gender = gender
        self.__date_birthday = date_birthday
        self.__place_birth = place_birth

    def __str__(self):
        return \
            f"ФИО: {self.__name}\n" \
            f"Пол: {self.__gender}\n"\
            f"Дата рождения: {self.__date_birthday}\n"\
            f"Место рождения: {self.__place_birth}\n"
    def info(self):
        print(\
            f"ФИО: {self.__name}\n" \
            f"Пол: {self.__gender}\n"\
            f"Дата рождения: {self.__date_birthday}\n"\
            f"Место рождения: {self.__place_birth}\n")

def execute_application():
    pass





if __name__=="__main__":
    execute_application()