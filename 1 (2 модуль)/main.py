from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Оплата картой на сумму {amount} сом.")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Оплата через PayPal на сумму {amount} сом.")

class CryptoPayment(Payment):
    def pay(self, amount):
        print(f"Оплата криптовалютой на сумму {amount} сом.")

class Delivery(ABC):
    @abstractmethod
    def deliver(self):
        pass

class HomeDelivery(Delivery):
    def deliver(self):
        print("Доставка на дом.")

class PickupPoint(Delivery):
    def deliver(self):
        print("Доставка в пункт выдачи.")

class DroneDelivery(Delivery):
    def deliver(self):
        print("Доставка с помощью дрона.")

class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_info(self):
        return f"Название: {self.__name}, Цена: {self.__price} сом."

    def buy(self, amount):
        if self.__quantity >= amount:
            self.__quantity -= amount
            return True
        return False

class User:
    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance

    def add_balance(self, amount):
        self.__balance += amount
        print(f"Баланс пользователя {self.__name} пополнен на {amount} сом.")

    def purchase(self, product, payment):
        if product.buy(1):
            if self.__balance >= int(product.get_info().split("Цена: ")[1].split()[0]):
                self.__balance -= int(product.get_info().split("Цена: ")[1].split()[0])
                payment.pay(int(product.get_info().split("Цена: ")[1].split()[0]))
                print(f"Покупка успешна! Баланс: {self.__balance} сом.")
            else:
                print("Недостаточно средств для покупки.")
        else:
            print("Товара нет в наличии.")

product1 = Product("Laptop", 50000, 10)
product2 = Product("Smartphone", 30000, 2)

payment_methods = [
    CreditCardPayment(),
    PayPalPayment(),
    CryptoPayment()
]

users = [
    User("Эльнара", "elnara@mail.com", 600000),
    User("Диана", "diana@mail.com", 1500000),
    User("Батма", "batma@mail.com", 899900)
]

delivery_methods = [
    HomeDelivery(),
    PickupPoint(),
    DroneDelivery()
]

for user in users:
    for product in [product1, product2]:
        print(f"\nПокупка для пользователя: {user._User__name}")
        user.purchase(product, payment_methods[0])
        delivery_methods[0].deliver()