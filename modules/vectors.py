class vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v2):
        return vector2(self.x+v2.x, self.y+v2.y)

    def __sub__(self, v2):
        return vector2(self.x-v2.x, self.y-v2.y)

    def __mul__(self, v2):
        return vector2(self.x*v2.x, self.y*v2.y) 

    def __truediv__(self, v2):
        return vector2(self.x/v2.x, self.y/v2.y) 

    