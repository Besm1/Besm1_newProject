class Horse:
    sound = 'Frrr'
    x_distance = 0

    def run(self, dx):
        self.x_distance += dx

    def get_pos(self):
        return (self.x_distance)


class Eagle:
    sound = 'I train, eat, sleep, and repeat'
    y_distance = 0

    def fly(self, dy):
        self.y_distance += dy

    def get_pos(self):
        return (self.y_distance)


class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


# print(Pegasus.mro())
#
# h1 = Horse()
# print(h1.sound)
# print(h1.get_pos())
# h1.run(20)
# print(h1.get_pos())
#
# e1 = Eagle()
# print(e1.sound)
# print(e1.get_pos())
# e1.fly(50)
# print(e1.get_pos())


p1 = Pegasus()

print(p1.get_pos())
p1.move(dx=10, dy=15)
print(p1.get_pos())
p1.move(dx=-5, dy=20)
print(p1.get_pos())

p1.voice()
