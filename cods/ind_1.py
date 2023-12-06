def fib(count: int):
    f1: int = 0
    f2: int = 1

    yield 0
    yield 1
    for _ in range(1, count):
        f1, f2 = f2, f1 + f2
        yield f2


if __name__ == '__main__':
    for i in fib(200):
        print(i)
