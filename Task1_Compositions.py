"""
Создайте композицию User состояющую из:
Объекта Profile со свойствами: name,last_name,age,pasport и методом print_info.
Объекта Address со свойствами : City,street,zipcode
Объекта Role со свойствами: role,hours_worked
Объекта BankAccount со свойствами: card_number, balance
Объекта Order с методом устанавливающими параметры заказа: Item,date,delivery,price
Добавьте в композицию методы создания профиля, установки адреса, роли, привязки банковского аккаунта и добавления заказа
"""

class Profile():
    def __init__(self, name, last_name, age, passport):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.passport = passport

    def print_info(self):
        print(self.name, self.last_name, self.passport)

class Adress:

    def __init__(self,city,street,zipcode):
        self.city = city
        self.street = street
        self.zipcode = zipcode


class Role:
    def __init__(self,role,hours_worked):
        self.role = role
        self.hours_worked = hours_worked


class BankAccount:
    def __init__(self,card_number,balance):
        self.card_number = card_number
        self.balance = balance


class Order:
    def __init__(self,item,date,delivery,price):
        self.item = item
        self.date = date
        self.delivery = delivery
        self.price = price


    def new_order(self):
        print(self.item,self.date,self.delivery,self.price)


class User:
    def __init__(self):
        self.adress = []
        self.bankaccount = []
        self.order = []


    def new_profile(self,name,last_name,passport):
        self.profile=Profile(name,last_name,passport)


    def your_adress(self,city,street,zipcode):
        self.adress.append(Adress(city,street,zipcode))


user1 = User()
user1.new_profile("Катя","Иванова", 124323)
user1.your_adress("Сочи","Ленина",354340)
print(user1.profile)
print(user1.adress)
print(user1.profile.name, user1.profile.last_name)
print(user1.adress[0].city)