class Coordinates2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinate(self):
        num = int(input('Введите координату x: '))
        if num >= 0:
            if num <= 100:
                print('')
        else:
            print('Координата неверна')

        num1 = int(input('Введите координату y: '))
        if num1 >= 0:
            if num1 <= 100:
                print('')
        else:
            print('Координата неверна')




coordinat = Coordinates2
coordinat.coordinate()


