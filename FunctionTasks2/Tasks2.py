"""
Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси.
"""
def parameter(distance):
    return 4 + (distance // 0.14) * 0.25

distance = int(input('Введите расстояние: '))
print(parameter(distance))






