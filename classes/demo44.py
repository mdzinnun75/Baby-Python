class Point:
    def __init__(self, x, y):       # to construct or create an object
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


p1 = Point(10, 20)      # constructor
p1.x = 11       # value of x updated
print(p1.x)
p1.draw()

