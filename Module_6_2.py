class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner:str, model:str, color:str, engine_power:int):
        super().__init__()
        if engine_power <= 0:
            print('Мощность должна быть положительной')
        elif color.lower() not in self._Vehicle__COLOR_VARIANTS:
            print('Такой цвет недоступен')
        else:
            self.owner = owner
            self.__model = model
            self.__engine_power = engine_power
            self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print (self.get_model() + '\n' + str(self.get_horsepower()) + '\n' +
                self.get_color() + '\nВладелец: ' + self.owner)



    def set_color(self, new_color:str):
        if new_color.lower() not in self._Vehicle__COLOR_VARIANTS:
            print(f'Нельзя поменять цвет на {new_color}')
        else:
            self.__color = new_color



if __name__ == '__main__':
    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()
