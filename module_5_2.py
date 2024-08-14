class House():
    name = ''
    number_of_floors = 0

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

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
