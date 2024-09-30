def triangle_perimeter(a=7, b=2, c=8):
    return a + b + c

def triangle_area(a=7, b=2, c=8):
    s = triangle_perimeter(a, b, c) / 2  # полупериметр
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # формула Герона
    return area