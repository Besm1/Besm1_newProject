class Horse:
    sound = 'Frrr'
    x_distance = 0

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    sound = 'I train, eat, sleep, and repeat'
    y_distance = 0

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


p1 = Pegasus()
print(Pegasus.mro())

print(p1.get_pos())
p1.move(dx=10, dy=15)
print(p1.get_pos())
p1.move(dx=-5, dy=20)
print(p1.get_pos())

p1.voice()
