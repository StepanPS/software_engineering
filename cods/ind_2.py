from ind_1 import fib

if __name__ == '__main__':
    with open("fib.txt", "w") as file:
        for i in fib(200):
            file.write(f"{i}\n")
