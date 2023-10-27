import random

def cube():
    throw= random.randint(1, 6)
    print(f"Выпало: {throw}")

    if throw in [5, 6]:
        print("Вы победили")
    elif throw in [3, 4]:
        print("Бросаете кубик еще раз:")
        cube()
    else:
        print("Вы проиграли")

if __name__ == '__main__':
    cube()
