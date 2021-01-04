class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_narcissistic(self):
        print('narcissistic')


d1 = Dog()
d1.walk()
d1.bark()

c1 = Cat()
c1.be_narcissistic()


