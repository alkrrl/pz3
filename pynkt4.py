import numpy as np
from calculations import square, cube, sine, cosine, exp_func
from visualization import plot_function, print_table

if __name__ == "__main__":
    a = float(input("Введите начало диапазона a: "))
    b = float(input("Введите конец диапазона b: "))
    step = float(input("Введите шаг: "))

    functions = {
        "1": ("(x**2)**0.5", Abs(x),
        "2": ("x**2", Square(x)),
        "3": (" x**0.5", Sqrt(x)),
        "4": ("1/x", Gip(x)),
        "5": ("2*x", Prum(x))
    }

    print("Выберите функцию:")
    for key, (name, _) in functions.items():
        print(f"{key}: {name}")

    choice = input("Ваш выбор: ")

    if choice not in functions:
        print("Неверный выбор функции!")
        exit()

    func_name, func = functions[choice]

    X = np.arange(a, b, step)
    Y = [func(x) for x in X]

    print_table(X, Y)
    plot_function(X, Y, func_name)
