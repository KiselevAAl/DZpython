"""
Напишите программу определяющую допуск ученика к зачету.
Программа должна запрашивать число учеников, затем у каждого ученика запрашивать балл за финальный тест
и в ответ печатать, допущен ли он (True или False) к зачету (необходимо набрать больше 50 баллов).
Ученикам без допуска должно печататься "Вы отчислены".
Выдачу допуска реализуй как функцию.
"""
def exam(number):
    for i in range(0, number):
        point = int(input('Введите число баллов за финальеый тест: '))
        if point > 50:
            print('Допущен')
        else:
            print('Вы отчислены')


exam(int(input('Введите число учеников: ')))