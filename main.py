from typing import Dict, List
#Задача 1
#Создайте класс Passport (паспорт), который будет содержать
#паспортную информацию о гражданине страны. С помощью механизма
#наследования, реализуйте класс ForeignPassport (загран.паспорт)
#производный от Passport.
class Passport:
    def __init__(self, name : Dict[str, str],gender: str, date_birthday: Dict[str, str], place_birth: str):
        self.__name = name
        self.__gender = gender
        self.__date_brithday = date_birthday
        self.__place_birth = place_birth
def execute_application():
    pass





if __name__=="__main__":
    execute_application()