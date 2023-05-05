from abc import ABC, abstractmethod
#Задание 1.
#Рассмотрим принцип разделения интерфейсов.
#Допустим у нас имеется абстрактный класс Payments и в нем есть три метода:
#оплата WebMoney, оплата банковской карточкой и оплата по номеру телефона.
#class Payments(ABC):
#@abstarctmethod
#def payWebMoney(self): pass
#@abstarctmethod
#def payCreditCard(self): pass
#@abstarctmethod
#def payPhoneNumber(self): pass
#Выполните разделение интерфейса таким образом, чтобы можно было реализовать
#два класса-сервиса, которые будут у себя реализовывать различные виды проведения
#оплат (класс InternetPaymentService и TerminalPaymentService). При этом
#TerminalPaymentService не должен поддерживать проведение оплат по номеру телефона.
class WebMoneyPayments(ABC):
    @abstractmethod
    def payWebMoney(self):
        pass

class CreditCardPayments(ABC):
    @abstractmethod
    def payCreditCard(self):
        pass

class PhoneNumberPayments(ABC):
    @abstractmethod
    def payPhoneNumber(self):
        pass
class InternetPaymentService(WebMoneyPayments, CreditCardPayments, PhoneNumberPayments):
    def payWebMoney(self):
        print("Оплата WebMoney через InternetPaymentService")

    def payCreditCard(self):
        print("Оплата кредитной картой через InternetPaymentService")

    def payPhoneNumber(self):
        print("Оплата номером телефона через InternetPaymentService")


class TerminalPaymentService(WebMoneyPayments, CreditCardPayments):
    def payWebMoney(self):
        print("Оплата WebMoney через TerminalPaymentService")

    def payCreditCard(self):
        print("Оплата кредитной картой через TerminalPaymentService")


def execute_application():
    pass
if __name__ =="__main__":
    execute_application()
