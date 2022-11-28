
def lessons(a):
    if 'расп' in a:
        schedule()
    elif 'трен' in a:
        trainer()
    elif 'оплат' in a:
        sum()
    elif 'групп' in a:
        group()
    elif 'абонемент' in a:
        gym()

    else:
        error()


def schedule():
    print('Расписание занятий: пн-выходной, вт-пт:8:00-22:00, сб:9:00-21:00, вс:8:00-23:00')
    h = input('Выберите день, когда вам будет удобно заниматься: ')
    if  'понедельник' in h:
        print(input('Наверное вы не заметили, но у нас в этот день выходной. Поэтому вам лучше выбрать другой день.'))
    elif 'вторник' in h:
        print('Хороший день для тренировки, т.к. сегодня действует скидка 10%')
    elif 'среда' in h:
        print('Отлчино, запись успешно выполнена')
    elif 'четверг' in h:
        print('Отлчино, запись успешно выполнена')
    elif 'пятница' in k:
        print('Отлчино, запись успешно выполнена')
    elif 'суббота' in k:
        print('Отлчино, в этот день действует скидка 15%')
    elif 'Воскресенье' in k:
        print('Отлчино, запись успешно выполнена')


def trainer():
    print('Контактные данные тренера: 89121065484, qwerty@qwert.com')


def sum():
    s = input('Какой день вы выбрали?')
    z = 1700
    if 'вторник' in s:
        print('Сумма к оплате вместе со скидкой будет: ' +  {z*0.01})


def group():
    print('Имеются групповые занятия.')
    b = input('В какое время вам будет удобно заниматься? На вечер либо на утро, вас записать?')
    if 'вечер' in b:
        print('Занятие состоится в 19:00')
    else:
        if 'утр' in b:
            print('Занятие состоится в 10:00')


def gym():
    print('Можно оформить абонемент в тренажерный зал на 2 месяца, пол года и на один год')


def error():
    print('Ошибка')