from math import sqrt


def task(a, b, c):
    p = (a + b + c) / 2
    S = sqrt(p * (p - a) * (p - b) * (p - c))
    return S


one = [12, 25, 3, 48, 71]
min_one = min(one)
max_one = max(one)
two = [5, 18, 40, 62, 98]
min_two = min(two)
max_two = max(two)
three = [4, 21, 37, 56, 84]
min_three = min(three)
max_three = max(three)

S_1 = task(min_one, min_two, min_three)
S_2 = task(max_one, max_two, max_three)

print("Площадь первого треугольника:", S_1)
print("Площадь второго треугольника:", S_2)
