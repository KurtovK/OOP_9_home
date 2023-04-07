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
        return f"ФИО: {self.__name}\n" \
            f"Пол: {self.__gender}\n"\
            f"Дата рождения: {self.__date_birthday}\n"\
            f"Место рождения: {self.__place_birth}\n"

    def info(self):
        print(f"\nКласс: {self.__class__.__name__}\n"
            f"ФИО: {self.__name}\n"
            f"Пол: {self.__gender}\n"
            f"Дата рождения: {self.__date_birthday}\n"
            f"Место рождения: {self.__place_birth}")


class ForeignPassport(Passport):
    def __init__(self, name: Dict[str, str], gender: str, date_birthday: Dict[str, str], place_birth: str,
                 citizenship: str, date_issue: Dict[str, str],expiration_date: Dict[str, str], issued_at: str,
                 series: str, number: str):
        super().__init__(name, gender, date_birthday, place_birth)
        self.__citizenship = citizenship
        self.__date_issue = date_issue
        self.__expiration_date = expiration_date
        self.__issued_at = issued_at
        self.__series = series
        self.__number = number

    def info(self):
        super().info()
        print(f"Гражданство: {self.__citizenship}\n"
            f"Дата выдачи: {self.__date_issue}\n"
            f"Дата окончвния: {self.__expiration_date}\n"
            f"Выдано:{self.__issued_at}\n"  
            f"Серия:{self.__series}\n"  
            f"Номер: {self.__number}")
def execute_application():
    name = {"Имя": "Константин", "Фамилия": "Куртов", "Отчество":"Дмитриевич"}
    gender = "Мужской"
    date_birthday = {"день": "21", "месяц": "февраль", "год": "1987"}
    place_birth = "с.Илек"
    passport = Passport(name, gender, date_birthday, place_birth)

    passport.info()

    name = {"Имя": "Konstantyn", "Фамилия": "Kurtov", "Отчество": "Dmitrievich"}
    gender = "М"
    date_birthday = {"день": "21", "месяц": "February", "год": "1987"}
    place_birth = "s.Ilek"
    citizenship = "Russia"
    date_issue = {"день": "16", "месяц": "May", "год": "2014"}
    expiration_date = {"день": "16", "месяц": "May", "год": "2024"}
    issued_at = "ОФМС"
    series = "КК087"
    number = "21021987"

    for_passport = ForeignPassport(name, gender, date_birthday, place_birth, citizenship, date_issue, expiration_date,
                                   issued_at, series, number)
    print()
    for_passport.info()

if __name__=="__main__":
    execute_application()