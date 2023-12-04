import math


# Значение функции
def my_func(x):
    return math.sin(x) + 0.2 - 2 * x * x


# Первая производная
def my_func_first(x):
    return math.cos(x) - 4 * x


# Вторая производная
def my_func_sec(x):
    return -math.sin(x) - 4


# Функция для вычисления в МПИ
def func_mpi(x):
    return math.sqrt((math.sin(x) + 0.2) / 2)


# Половинное деление отрезка
def dihotomia(a, b, eps):
    iteration = 0
    while abs((b - a) / 2) > eps:
        mid_point = (a + b) / 2
        if my_func(mid_point) == 0:
            return mid_point, iteration
        elif (my_func(mid_point) * my_func(a)) < 0:
            b = mid_point
        else:
            a = mid_point
        iteration += 1

    return (a + b) / 2, iteration


# Метод Ньютона
def method_newton(a, eps):
    iteration = 0
    while abs(my_func(a) / my_func_first(a)) > eps:
        a = a - (my_func(a) / my_func_first(a))
        iteration += 1
    return a, iteration


# Модифицированный метод Ньютона
def mod_method_newton(a, eps):
    iteration = 0
    x0 = my_func_first(a)
    while abs(my_func(a) / my_func_first(a)) > eps:
        a = a - (my_func(a) / x0)
        iteration += 1
    return a, iteration


# Метод хорд
def method_hord(a, b, eps):
    fx0 = my_func(a)
    iteration = 0
    while abs(my_func(b) / my_func_first(b)) > eps:
        t = my_func(b)
        b = b - ((t * (b - a)) / (t - fx0))
        iteration += 1
    return b, iteration


# Метод подвижных хорд
def podv_method_hord(a, b, eps):
    iteration = 0
    c = a
    b = b
    a = b - ((my_func(b) * (b - c)) / (my_func(b) - my_func(c)))
    while abs(my_func(a) / my_func_first(a)) > eps:
        a = b - ((my_func(b) * (b - c)) / (my_func(b) - my_func(c)))
        c = b
        b = a
        iteration += 1

    return a, iteration


# Метод простой итерации
def mpi(a, b, eps):
    x = (a + b) / 2
    iteration = 0
    while abs(my_func(x) / my_func_first(x)) > eps:
        x = func_mpi(x)
        iteration += 1

    return x, iteration


if __name__ == '__main__':
    eps = 0.000005
    a = 0.5
    b = 1

    print(dihotomia(a, b, eps))
    print(method_newton(b, eps))
    print(mod_method_newton(b, eps))
    print(method_hord(b, a, eps))
    print(podv_method_hord(b, a, eps))
    print(mpi(a, b, eps))
