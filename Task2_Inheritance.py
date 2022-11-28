"""
Создайте класс который будет устанавливать свойство name и иметь метод
который к имени прибавляет надпись "гений". Создайте еще 1 класс, унаследуйте предыдущий.
Во втором классе вызовите метод класса родителя и добавьте к выводу надпись "но его отчислят если он не будет учить ООП".
Создайте экземпляр второго класса с вашим именем и вызовите метод печатающий всю надпись.
"""

class Name():
    def __init__(self, name):
        self.name =  name

    def print_info(self):
        return f'{self.name} гений'

class People(Name):
    def __init__(self, name):
        super().__init__(name)

    def object(self):
        abc = Name(self.name)
        return abc

    def name1(self):
        print(f'{self.object().print_info()}' + ', но его отчислят если он не будет учить ООП')


alena = People('Алёна')
alena.name1()
