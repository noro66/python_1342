from math import sqrt


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self):
        if self.width < 50:
            result = ""
            for y in range(self.height):
                result += "*" * self.width + "\n"
            return result
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape):
        self_area = self.get_area()
        area = shape.get_area()
        return self_area // area


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width
        self.side = new_width

    def set_height(self, new_height):
        self.width = new_height
        self.height = new_height
        self.side = new_height

    def set_side(self, side):
        self.side = side
        self.width = self.side
        self.height = self.side

    def __str__(self):
        return f"Square(side={self.side})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
