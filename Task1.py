"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму(сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""

class BankAccount():
    def __init__(self, name, balance, passport):
        self._name = name
        self.__balance = balance
        self.__passport = passport

    def getbalance(self):
        return self.__balance

    def getpassport(self):
        return self.__passport

    def setbalance(self, new_balance):
        self.__balance = new_balance

    def setpassport(self, new_passport, password):
        if password == self.get_password():
            self.__passport = new_passport
            print('успешно изменен')
        else:
            print('Не тот пароль')

    def delpassport(self, password):
        if password == self.getpassword():
            del self.__passport
            print('паспорт удален')
        else:
            print('Не тот пароль')


account1 = BankAccount("qwrtp", 1000, 987654)
print(account1.getbalance())
print(account1.getpassport())
account1.setbalance(-34)
account1.setnomerpassport(9876, 98765)
account1.delpassport(4567)