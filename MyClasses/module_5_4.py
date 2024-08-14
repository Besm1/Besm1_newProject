class House():
    # name = ''
    # number_of_floors = 0
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.args = args
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, floors):
        self.name, self.number_of_floors = name, floors

    def go_to(self, new_floor):
        if new_floor in range(1, self.number_of_floors+1):
            for fl in range(new_floor):
                print(fl+1)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return 'Название: {}, кол-во этажей: {}'.format(self.name, self.number_of_floors)


    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return None

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return None

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return None

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return None

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return None

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return None

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __iadd__(self, value):
        return self.__add__( value)

    def __radd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        if isinstance(value, int):
            self.number_of_floors -= value
        return self


    def __isub__(self, value):
        return self.__sub__(value)


    def __del__(self):
        print('{} разрушен, но он останется в истории.'.format(self.name))


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

