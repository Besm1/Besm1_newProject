from functools import reduce
from math import pi

class Figure:
    sides_count = 0

    def __init__(self, color: tuple, *sides, filled=False):
        # print(f'figure.Init. Sides = {sides}')
        self.__is_initializing = True
        self.set_sides(*sides)
        self.set_color(*color)
        self.filled = filled
        self.__is_initializing = False

    def __is_valid_color(self, *color: tuple):
        return len(color) == 3 and all(isinstance(color_, int) and color_ in range(0, 255) for color_ in color)

    def set_color(self, *color: tuple):
        if self.__is_valid_color(*color):
            self.__color = color

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *args):
        return (len(args) == self.sides_count) and all(isinstance(side_, int) and (side_ > 0) for side_ in args)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.get_sides())

    def set_sides(self, *sides):
        # print(f'set_sides: sides = {sides}, {self.__is_valid_sides(*sides)}')
        # Если неверные стороны, то поведение разное при инициализации и при изменении сторон:
        #   при инициализации принимаем все стороны равными 1
        #   при изменении не делаем ничего
        if self.__is_valid_sides(*sides):
            self.__sides = sides
        elif self.__is_initializing:
            self.__sides = tuple(self.sides_count * [1])
        # print(f'set_sides. __sides = {self.__sides}')

    def __str__(self):
        return f'Цвет: {self.__color}, стороны: {self.__sides}, {'' if self.filled else 'не '}закрашен'



class Triangle(Figure):
    sides_count = 3


    def set_sides(self, *sides):
        if all(2 * s_ < sum(sides) for s_ in sides):
            super().set_sides(*sides)
        else:
            super().set_sides(1)    # передадим неверное число сторон, чтобы сработали разные алгоритмы при инициализации и при смене.

    def __is_valid_sides(self, *args):
        print(f'Triangle: __is_valid_sides {args}')
        return super().__is_valid_sides(*args) and all(2 * s_ < sum(args) for s_ in args)

    def get_square(self):
        p = self.__len__() / 2.
        return (p * reduce(lambda x, y: x * y, (p - s_ for s_ in self.get_sides()))) ** 0.5

    def __str__(self):
        return 'Треугольник. ' + super().__str__()


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled=filled)
        self.__radius = sides[0] / (2 * pi)

    def get_square(self):
        return self.__radius ** 2 * pi

    def __str__(self):
        return 'Окружность. ' + super().__str__()

class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple, *sides, filled=False):
        super().__init__(color, *sides, filled)
        # Кол-во параметров длин сторон не совпадает с sides_count,
        # поэтому родительский класс инициализирует стороны единицами
        # Нам надо переинициализировать
        self.set_sides(*sides)

    def set_sides(self, *sides):
        if len(sides) == 1:
            super().set_sides(*self.sides_count * [sides[0]])
        else:
            super().set_sides(1)   # передадим "неверное" число сторон, чтобы сработали разные алгоритмы при инициализации и при смене.

    def get_volume(self):
        return self.get_sides()[0] ** 3

    def __str__(self):
        return 'Куб. ' + super().__str__()


if __name__ == '__main__':
    #
    #   Моя проверка
    #
    # tri1 = Triangle((200,200,33),3, 4, 5)
    # print('Нач.значение: ' + str(tri1))
    # tri1.set_sides(3, 4, 25)
    # print('Попытка изменения сторон "tri1.set_sides(3, 4, 25)": ' + str(tri1))
    # tri1.set_sides(3, 4, 6)
    # print('Попытка изменения сторон "tri1.set_sides(3, 4, 6)": ' + str(tri1))
    # tri1.set_color((300, 200, 6))
    # print('Попытка изменения цвета "tri1.set_color((300, 200, 6))": ' + str(tri1))
    # tri1.set_color(50, 100, 150)
    # print('Попытка изменения цвета "tri1.set_color((50, 100, 150))": ' + str(tri1))
    # print(tri1.get_sides())
    # print(tri1.get_color())
    # print(len(tri1))
    # print(tri1.get_square())

    # c1 = Circle((200,200,100), 10)
    # print(c1)
    # c2 = Circle((200,200,100), 10, 11)
    # print(c2)

    # cu1 = Cube((200,100,75), 10)
    # print(cu1)
    # print(f'Объём куба: {cu1.get_volume()}')
    # cu2 = Cube((200,100,75), 10, 12)
    # print(cu2)
    # print(f'Объём куба: {cu2.get_volume()}')

    #   Код для проверки из задания
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())



