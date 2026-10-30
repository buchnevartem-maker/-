class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def shift(self, dx, dy):
        self.x += dx
        self.y += dy

p = Point(1, 2)
p.shift(3, 4)
print(p.x, p.y)