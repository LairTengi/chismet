import math


def f(x):
    return math.cos(math.exp(x) + x)


def simps(a, b, h):
    m = (b - a) / h
    integral = 0
    for i in range(0, int(m)):
        integral += f(a + h * i) + 4 * f(a + h * (i + 1 / 2)) + f(a + h * (i + 1))
    return h / 6 * integral


def gregori(a, b, h):
    m = (b - a) / h
    part_1 = 1 / 2 * (f(a) + f(b))
    part_2 = h / 24 * (-3 * f(a) + 4 * f(a + h) - f(a + 2 * h) - 3 * f(b)
                       + 4 * f(b - h) - f(b - 2 * h))
    part_3 = 0
    for i in range(1, int(m)):
        part_3 += f(a + h * i)
    integral = h * (part_1 + part_3) + part_2
    return integral


if __name__ == "__main__":
    a = 0
    b = 2
    h1 = 0.1
    h2 = 0.05
    h3 = 0.025
    print('Составная формула Симпсона, h = ' + str(h1))
    print(simps(a, b, h1))
    print('Составная формула Симпсона, h = ' + str(h2))
    print(simps(a, b, h2))
    print('Составная формула Симпсона, h = ' + str(h3))
    print(simps(a, b, h3))

    print('Составная формула Грегори, h = ' + str(h1))
    print(gregori(a, b, h1))
    print('Составная формула Грегори, h = ' + str(h2))
    print(gregori(a, b, h2))
    print('Составная формула Грегори, h = ' + str(h3))
    print(gregori(a, b, h3))

    print("gauss")
    # print(0.8 * f(1) + 1.7 * f(1.77459666924148) + 0.2 * f(0.22540333075851))
    # print(-1.3333 * f(1) + 0.375663 * f(1.774596) + 2.95764 * f(0.225403))
    print(8 / 9 * f(1) + 5 / 9 * f(1 + (math.sqrt(15)) / 5) + 5 / 9 * f(1 - (math.sqrt(15)) / 5))

    print()
    print("Погрешность Симпсона")
    print('Погрешность для 0.1')
    print((simps(a, b, h2) - simps(a, b, h1)) / 15)
    print('Погрешность для 0.05')
    print((simps(a, b, h3) - simps(a, b, h2)) / 15)

    print()
    print("Погрешность Грегори")
    print('Погрешность для 0.1')
    print((gregori(a, b, h2) - gregori(a, b, h1)) / 3)
    print('Погрешность для 0.05')
    print((gregori(a, b, h3) - gregori(a, b, h2)) / 3)
