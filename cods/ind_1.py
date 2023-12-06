import time


def print_time(func):
    def wrapper(*args, **kwargs):
        start_time: float = time.time()
        result = func(*args, **kwargs)
        end_time: float = time.time()
        print()
        print(f"Время выполнения {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper


@print_time
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' \n')


if __name__ == '__main__':
    fibonacci()
