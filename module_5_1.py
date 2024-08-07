class House():
    name = ''
    number_of_floors = 0

    def __init__(self, name, floors):
        self.name, self.number_of_floors = name, floors

    def go_to(self, new_floor):
        if new_floor in range(1, self.number_of_floors):
            for fl in range(new_floor):
                print(fl+1)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

