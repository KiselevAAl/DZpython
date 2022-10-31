
"""
Каждый стажёр мог выбрать любое число предметов для изучения. По каждому предмету он мог набрать от 0 до 50 баллов.
Программа должна:
Пока пользователь не введет "стоп"":
1. Запрашивать имя студента и число предметов.
2. Запрашивать число баллов по каждому предмету и печатать общую сумму баллов: «Итоговый счёт: _».
3. По сумме баллов опеределять тип грамоты о прохождении стажировки:
- баллов больше 80 — «Наградить дипломом.»;
- баллов больше 50 и меньше или равно 80 — «Наградить похвальной грамотой.»;
- остальные случаи — «Выдать грамоту об участии.».
"""

def trainee():
    name = input('Введите имя: ')
    number = int(input('Введите число предметов: '))
    while name != 'стоп':
        sum = 0
        for i in range(0, number):
            sum += int(input('Введите число баллов: '))
        print('Итоговый счёт:', sum)
        if sum > 80:
            print('Наградить дипломом.')
        elif 50 > sum >= 80:
            print('Наградить похвальной грамотой.')
        elif sum <= 50:
            print('Выдать грамоту об участии.')
        name = input('Введите имя: ')
        number = int(input('Введите число предметов: '))


trainee()




