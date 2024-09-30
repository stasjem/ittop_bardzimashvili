import math

__default_radius = 5

def circle_perimeter(radius):
    return 2 * math.pi * radius

def circle_area(radius):
    return math.pi * (radius ** 2)


def default_circle_perimeter():
    return circle_perimeter(__default_radius)

def default_circle_area():
    return circle_area(__default_radius)