class Point:
    def move(self):
        print("move")

    def draw(self):
        print("Draw")


point1 = Point()
point1.x = 10
point1.y = 12
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 22
print(point2.x)
point2.draw()