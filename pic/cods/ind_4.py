list_1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
list_2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
list_3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def update(grades):
    updated = []
    for grade in grades:
        if grade == 2:
            updated.append(4)
        elif grade == 3:
            updated.append(4)
        else:
            updated.append(grade)
    return updated

updated_1 = update(list_1)
updated_2 = update(list_2)
updated_3 = update(list_3)

print(updated_1)
print(updated_2)
print(updated_3)
