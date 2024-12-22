import math


class Figure:
    side_count = 0

    def __init__(self, color, *sides):
        if self.__is_valid_side(*sides):
            self.__sides = sides
        else:
            self.__sides = []
            if len(sides) == 1:
                val = sides[0]
            else:
                val = 1
            for side in range(0, self.side_count):
                self.__sides.append(val)
        if self.__is_valid_color(color[0], color[1], color[2]):
            self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if all((type(r) == int, type(g) == int, type(b) == int)):
            if (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255):
                return True
            else:
                return False
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid_side(self, *args):
        if len(args) == self.side_count:
            for arg in args:
                if not ((type(arg) == int) and (arg > 0)):
                    return False
        else:
            return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        sum_ = 0
        for side in self.__sides:
            sum_ += side
        return sum_

    def set_sides(self, *new_sides):
        if self.__is_valid_side(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    side_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return math.pi * self.__radius * 2


class Triangle(Figure):
    side_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        p = 0.5 * (a + b + c)
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    side_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_volume(self):
        a = self.get_sides()[0]
        return a * a * a


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
tri = Triangle((222, 35, 130), 6, 5, 4)
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
