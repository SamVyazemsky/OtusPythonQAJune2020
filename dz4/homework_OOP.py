import math
import pytest


class Figure:
    def __init__(self, area, name, angles):
        self.area = area
        self.name = name
        self.angles = angles

    def add_area(self, other):
        if not isinstance(self, Figure):
            raise Exception("Argument must be instance of Figure class")
        else:
            return self.area() + other.area()


class Circle(Figure):
    def __init__(self, radius):
        super().__init__(self.area, 'circle', 0)
        self.radius = radius

    def perimeter(self):
        return 2*math.pi*self.radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Triangle(Figure):
    def __init__(self, first_side, second_side, third_side):
        super().__init__(self.area, 'triangle', 3)
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side
        if first_side + second_side > third_side and \
            second_side + third_side > first_side and \
            third_side + first_side > second_side:
                print("triangle exist")
        else:
            raise Exception('The sum of any two sides of a triangle'
                            'must be greater than the third side')

    def perimeter(self):
        return self.first_side + self.second_side + self.third_side

    def area(self):
        self.half_perimeter = self.perimeter()/2
        # Формула площади треугольника через длины сторон:
        # S = sqrt(p(p-a)(p-b)(p-c), где p - половина периметра фигуры; a,b,c - стороны треугольника.
        return math.sqrt(self.half_perimeter * (
                (self.half_perimeter - self.first_side) *
                (self.half_perimeter - self.second_side) *
                (self.half_perimeter - self.third_side)))


class Rectangle(Figure):
    def __init__(self, lengh, width):
        super().__init__(self.area, 'rectangle', 4)
        self.lengh = lengh
        self.width = width

    def perimeter(self):
        return (self.lengh + self.width) * 2

    def area(self):
        return self.lengh * self.width


class Square(Figure):
    def __init__(self, side_size):
        super().__init__(self.area, 'square', 4)
        self.side_size = side_size

    def perimeter(self):
        return self.side_size * 4

    def area(self):
        return self.side_size ** 2


@pytest.mark.parametrize('radius', [3, 5, 12, 15, 18])
def test_circle(radius):
    testCircle = Circle(radius)
    assert testCircle.area() == math.pi * (radius ** 2)


@pytest.mark.parametrize('first_side, second_side, third_side, area',
                         [(7, 6, 12, 14.95), (15, 18, 12, 89.29),
                          (3, 4, 5, 6), (8, 7, 9, 26.83), (10, 15, 8, 36.98)])
def test_triangle(first_side, second_side, third_side, area):
    testTriangle = Triangle(first_side, second_side, third_side)
    assert float("%.2f" % testTriangle.area()) == area


@pytest.mark.parametrize('lengh, width, side_size, sum_area', [(4, 6, 2, 28), (4, 7, 8, 92),
                                                     (2, 9, 2, 22), (2, 5, 1, 11), (9, 2, 7, 67)])
def test_rectangle(lengh, width, side_size, sum_area):
    testRectangle = Rectangle(lengh, width)
    testSquare = Square(side_size)
    assert (testRectangle.add_area(testSquare)) == sum_area


@pytest.mark.parametrize('side_size', [1, 2, 3, 4, 5])
def test_square(side_size):
    testSquare = Square(side_size)
    assert testSquare.perimeter() / 4 == side_size
