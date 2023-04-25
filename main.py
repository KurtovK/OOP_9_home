#Задача 1
#Допустим у нас есть класс RentCarService и в нем есть несколько
#методов: найти машину по номеру, забронировать машину по номеру,
#распечатать заказ на бронирование, получить информацию о машине,
#отправить сообщение клиенту с информацией о его брони.
#У данного класса есть несколько зон ответственности, что является
#нарушением принципа единой ответственности, так как отвечает за разные действия.
#Необходимо создать класс PrinterService и вынести туда функционал по печати.
#Работу связанную с получением информации о машине перенести в класс CarInfoService.
#Метод по отправке сообщений перенести в класс NotificationService.
#Метод поиска машины по номеру в класс CarService.

class Car:
    def __init__(self, number: str, brand: str, model: str, year: int):
        self.number = number
        self.brand = brand
        self.model = model
        self.year = year
        self.rented = False


class CarService:
    def __init__(self):
        self.cars = []

    def find_car_by_number(self, number):
        for car in self.cars:
            if car.number == number:
                return car
        return None

    def add_car(self, car):
        self.cars.append(car)


class CarInfoService:
    @staticmethod
    def get_car_info(car):
        return f"Номер автомобиля: {car.number}, Бренд: {car.brand}, Модель: {car.model}, Год выпуска: {car.year}"


class NotificationService:
    @staticmethod
    def send_notification(customer_email, message):
        print(f"Сообщение '{message}' отправлено на почту {customer_email}")


class PrinterService:
    @staticmethod
    def print_order(order):
        print(f"Заказ на бронирование '{order}' распечатан")


class RentCarService:
    def __init__(self):
        self.car_service = CarService()

    def find_car_by_number(self, number):
        return self.car_service.find_car_by_number(number)

    def book_car(self, number, customer_email):
        car = self.find_car_by_number(number)
        if car and not car.rented:
            car.rented = True
            message = f"Ваш автомобиль {car.brand} {car.model} с номером {car.number} забронирован"
            NotificationService.send_notification(customer_email, message)
            PrinterService.print_order(message)
            return True
        else:
            return False



def execute_application():
    rent_car_service = RentCarService()
    rent_car_service.car_service.add_car(Car("C009HK", "WW", "Passat", 2018))
    rent_car_service.car_service.add_car(Car("DEF456", "Honda", "Civic", 2020))

    car = rent_car_service.find_car_by_number("C009HK")
    if car:
        car_info = CarInfoService.get_car_info(car)
        print(car_info)
    else:
        print("Автомобиль не найден")

    booking_successful = rent_car_service.book_car("C009HK", "kurtov@yst.ru")
    if booking_successful:
        print("Машина успешно забронирована")
    else:
        print("Машина не найдена или уже забронирована")

if __name__=="__main__":
    execute_application()