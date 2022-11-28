"""
В классе Hero из предыдущего занятия добавьте приватное свойство rank.
Создайте геттер, сеттер и делиттер чтобы можно было получить звание героя, установить звание "Победитель арены"
в случае победы героя в битве и удалить ранк в случае поражения.
"""

class Hero():
    def __init__(self,name,health,armor,rank):
        self.name = name
        self.health = health
        self.armor = armor
        self.__rank = rank

    def setrank(self, rank):
        self.__rank = rank

    def getrank(self):
        return self.__rank

    def delrank(self):
        del self.__rank

