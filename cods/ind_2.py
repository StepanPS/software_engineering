def Nicolai(tup, element):
    if element in tup:
        index = tup.index(element)
        return tup[:index] + tup[index+1:]
    else:
        return tup


tup1 = (1, 2, 3)
element1 = 1

tup2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
element2 = 3

tup3 = (2, 4, 6, 6, 4, 2)
element3 = 9

result1 = Nicolai(tup1, element1)
print(result1)
result2 = Nicolai(tup2, element2)
print(result2)
result3 = Nicolai(tup3, element3)
print(result3)
