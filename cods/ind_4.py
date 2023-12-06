class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Вызвана функция '{self.func.__name__}' с аргументами: {args}, {kwargs}")
        return self.func(*args, **kwargs)

@MyDecorator
def sum_numbers(a):
    return a * a

@MyDecorator
def multiply_numbers(a, b):
    return a + b


print(sum_numbers(2))
print(multiply_numbers(4, 5))
