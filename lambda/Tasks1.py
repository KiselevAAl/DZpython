"""
Напишите программу которая будет спрашивать пользователя ввод имени пока пользователь не введет off.
Программа должна используя lambda-функцию добавлять к каждому имени надпись "гений".
"""


while True:
    name = input('Введите имя: ')
    if name != 'off':
        a = lambda name_, a: print(name_, a)
        a(name, 'гений')
    else:
        break
