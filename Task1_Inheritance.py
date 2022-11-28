"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и attack.
"""
class Hero():
    def __init__(self,name,health,armor):
        self.name = name
        self.health = health
        self.armor = armor

    def print_info(self):
        print('Уровень здоровья: ', self.health)
        print('Класс брони: ', self.armor, '\n')


class Magician(Hero):
    def __init__(self, name, health, armor):
        super().__init__(name, health, armor)

    def hello(self):
        print(f'Добро пожаловать! {self.name}')
        self.print_info()

    def attack(self, enemy):
        print('-> УДАР! Храбрый воин', self.name, 'атакует', enemy.name, 'мечом!')
        enemy.armor -= 15
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print('Страшный удар обрушился на противника. \nТеперь его броня: ' + str(enemy.armor) + ', а уровень здоровья: ' + str(enemy.health) + '\n')


hero = Hero('Влад',100, 10)
magic = Magician('Кирилл', 1000, 100)
magic.hello()
magic.attack(hero)


