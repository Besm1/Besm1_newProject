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


class Walker():
    name = str(None)
    current_house = None
    current_floor = None

    def __init__(self, name, cur_house = None, cur_fl = None):
        # Класс "Пешеход". У него есть имя и текущее положение - текущий дом и этаж
        # Пешеход умеет ходить по домам и сообщать о своих передвижениях.
        self.name, self.current_house, self.current_floor = name, cur_house, cur_fl

    def go_to(self, house, floor = None):
         # Метод передвигает пешехода из текущего местоположения в другой дом
        if isinstance(house, House):
            if floor in range(1, house.number_of_floors+1) or floor == None:
                print('Я {}, иду '.format(self.name), end = '')
                if self.current_house == None:
                    print('с улицы ', end = '')
                else:
                    print('из дома "{}" '.format(self.current_house.name), end = '')
                    if self.current_floor != None:
                        print('с {}-го этажа '.format(self.current_floor), end = '')
                print('в дом "{}"'.format(house.name), end = '')
                if floor != None:
                    print(' на {}-й этаж'.format(floor), end = '')
                print('.')
                self.current_house, self.current_floor = house, floor
            else:
                print('** В доме {} нет {}-го этажа!!!'.format(house, floor))
        else:
            print('А вот', house, '- это не дом, я туда не пойду!')



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(1)
h2.go_to(10)

john = Walker('Джонни')
john.go_to(h1,10)
john.go_to(h2,2)
john.go_to(h1)
john.go_to(15)
john.go_to(h1,15)

bob = Walker('Боб Марли', h2, 1)
bob.go_to(h1, 15)
