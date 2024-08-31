import functools as ft

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
            lst_ = []
            for i_ in range (0, self.sides_count):
                lst_.append(1)
            self.__sides = tuple(lst_)
        # print(f'set_sides. __sides = {self.__sides}')


class Triangle(Figure):
    sides_count = 3

    # def __init__(self, color, *sides, filled=False):
    #     # print(f'Иниц треуг. sides = {sides}')
    #     super().__init__(color, *sides, filled=filled)
    #
    def __is_valid_sides(self, *args):
        print(f'Triangle: __is_valid_sides {args}')
        return super().__is_valid_sides(*args) and all(2 * s_ < sum(args) for s_ in args)

    def get_square(self):
        p = self.__len__() / 2.
        return (p * ft.reduce(lambda x, y: x * y, (p - s_ for s_ in self.get_sides()))) ** 0.5

if __name__ == '__main__':
    tri1 = Triangle((200,200,33),3, 4, 5)
    print(tri1.get_sides())
    print(tri1.get_color())
    print(len(tri1))
    print(tri1.get_square())


