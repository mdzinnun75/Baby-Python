class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


p1 = Point()
p1.x = 10
p1.y = 20
print(p1.x)
p1.draw()

p2 = Point()
p2.x = 1
print(p2.x)
p2.move()


