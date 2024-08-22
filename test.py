class Human:
    head = True
    _legs = True
    __arms = True

class Student(Human):
    __arms = False

print(dir(Human))
print(dir(Student))