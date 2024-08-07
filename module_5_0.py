class Human():
    name = str(None)
    age = 0

    def __init__(self, name, age):
        self.name, self.age = name, age

    def say_info(self):
        print('Привет, меня зовут {}, мне {}, моя фамилия {}'.format(self.name, self.age, self.surname ))


bob = Human('Bob', 64)
alex = Human('Alex', 43)

bob.surname = 'Smirnoff'
bob.say_info()
alex.say_info()
