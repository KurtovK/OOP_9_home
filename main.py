#Задание 1.
#Реализуйте класс Retailltem (товарная единица), который содержит
#данные о товаре в магазине. Этот класс должен хранить данные в атрибутах:
#описание товара, количество единиц на складе и цена. После написания
#этого класса напишите программу, которая создает три объекта Retailitem.
#Создайте класс CashRegister (Кассовый аппарат), который может
#использоваться вместе с классом Retailltem. Класс CashRegister должен иметь
#внутренний список объектов Retailltem, а также приведенные ниже методы:
#Метод purchase_item() (приобрести товар) в качестве аргумента
#принимает объект Retailltem. При каждом вызове метода purchase_item()
#объект Retailltem, передан­ный в качестве аргумента, должен быть добавлен в список.
#Метод get_total () (получить сумму покупки) возвращает общую
#стоимость всех объектов Retailltem, хранящихся во внутреннем списке объекта CashRegister.
#Метод show_iterns () (показать товары) выводит данные об объектах
#Retailltem, хранящихся во внутреннем списке объекта CashRegister.
#Метод clear () (очистить) должен очистить внутренний список объекта CashRegister.
#Продемонстрируйте класс CashRegister в программе, которая
#позволяет пользователю выбрать несколько товаров для покупки. Когда
#пользователь готов рассчитаться за покупку, программа должна вывести
#список всех товаров, которые он выбрал для покупки, а также их общую стоимость
class Retailitem:
    def __init__(self, description, quantity, price):
        self.description = description
        self.quantity = quantity
        self.price = price

class CashRegister:
    def __init__(self):
        self.items = []

    def purchase_item(self, item):
        self.items.append(item)

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total

    def show_items(self):
        for item in self.items:
            print(f"{item.description} - {item.quantity} шт. по цене {item.price} руб.")

    def clear(self):
        self.items = []
def executer_application():
    pass
if __name__ =="__main__":
    executer_application()