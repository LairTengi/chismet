import warnings

import numpy as np
import math
import matplotlib.pyplot as plt


def f(x):
    return 3 * math.sqrt(x) / 2


def f_integr(x):
    return pow(x, 3 / 2) - 3


def func_for_eyler(x_values, y_values, h):
    for i in range(len(x_values)):
        if i == 0:
            y_values[0] = -3
        else:
            y_values[i] = y_values[i - 1] + (3 * math.sqrt(x_values[i - 1]) / 2) * h


def func_for_teylor(x_values, y_values, h):
    for i in range(len(x_values)):
        warnings.filterwarnings("error", category=RuntimeWarning)
        if i == 0:
            y_values[0] = -3
        else:
            try:
                y_values[i] = y_values[i - 1] + h * 3 * math.sqrt(x_values[i - 1]) / 2 + 3 * h * h / (
                            8 * math.sqrt(x_values[i - 1])) - pow(h, 3) / 16 * pow((x_values[i - 1]), -3 / 2)
            except Exception as e:
                print("Caught a RuntimeWarning:", e)


def func_for_trapez(x_values, y_values, h):
    for i in range(len(x_values)):
        if i == 0:
            y_values[0] = -3
        else:
            y_values[i] = y_values[i - 1] + h / 2 * (
                    3 / 2 * math.sqrt(x_values[i]) + 3 / 2 * math.sqrt(x_values[i - 1]))


def analytics(N10, N20, N30):
    x_values10 = np.linspace(0, 1, N10)
    y_values10 = f_integr(x_values10)
    x_values20 = np.linspace(0, 1, N20)
    y_values20 = f_integr(x_values20)
    x_values30 = np.linspace(0, 1, N30)
    y_values30 = f_integr(x_values30)

    plt.plot(x_values10, y_values10, label="N=10")
    plt.plot(x_values20, y_values20, label="N=20")
    plt.plot(x_values30, y_values30, label="N=30")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Аналитическое решение')
    plt.xticks(x_values10, [f'{val:.2f}' for val in x_values10])
    plt.grid(True)
    plt.legend()
    plt.show()


def eyler(x_values10, x_values20, x_values30, y_values10, y_values20, y_values30, h10, h20, h30):
    func_for_eyler(x_values10, y_values10, h10)
    func_for_eyler(x_values20, y_values20, h20)
    func_for_eyler(x_values30, y_values30, h30)

    plt.plot(x_values10, y_values10, label="N=10")
    plt.plot(x_values20, y_values20, label="N=20")
    plt.plot(x_values30, y_values30, label="N=30")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Явный метод Эйлера')
    plt.xticks(x_values10, [f'{val:.2f}' for val in x_values10])
    plt.grid(True)
    plt.legend()
    plt.show()


def teylor(x_values10, x_values20, x_values30, y_values10, y_values20, y_values30, h10, h20, h30):
    func_for_teylor(x_values10, y_values10, h10)
    func_for_teylor(x_values20, y_values20, h20)
    func_for_teylor(x_values30, y_values30, h30)

    plt.plot(x_values10, y_values10, label="N=10")
    plt.plot(x_values20, y_values20, label="N=20")
    plt.plot(x_values30, y_values30, label="N=30")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Метод Тейлора 3-го порядка')
    plt.xticks(x_values10, [f'{val:.2f}' for val in x_values10])
    plt.grid(True)
    plt.legend()
    plt.show()


def trapezoid(x_values10, x_values20, x_values30, y_values10, y_values20, y_values30, h10, h20, h30):
    func_for_trapez(x_values10, y_values10, h10)
    func_for_trapez(x_values20, y_values20, h20)
    func_for_trapez(x_values30, y_values30, h30)

    plt.plot(x_values10, y_values10, label="N=10")
    plt.plot(x_values20, y_values20, label="N=20")
    plt.plot(x_values30, y_values30, label="N=30")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Метод Трапеций')
    plt.xticks(x_values10, [f'{val:.2f}' for val in x_values10])
    plt.grid(True)
    plt.legend()
    plt.show()


def all_func(h, N):
    x_values = np.linspace(0, 1, N)
    y_values = f_integr(x_values)
    plt.plot(x_values, y_values, label="Аналитический")
    func_for_eyler(x_values, y_values, h)
    plt.plot(x_values, y_values, label="Эйлер")
    func_for_teylor(x_values, y_values, h)
    plt.plot(x_values, y_values, label="Тейлор")
    func_for_trapez(x_values, y_values, h)
    plt.plot(x_values, y_values, label="Трапеций")

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Сравнение для N = ' + str(N))
    plt.xticks(x_values10, [f'{val:.2f}' for val in x_values10])
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    N10 = 10
    N20 = 20
    N30 = 30

    y_values10 = np.empty(N10)
    y_values20 = np.empty(N20)
    y_values30 = np.empty(N30)
    x_values10 = np.linspace(0, 1, N10)
    h10 = abs(x_values10[0] - x_values10[1])
    x_values20 = np.linspace(0, 1, N20)
    h20 = abs(x_values20[0] - x_values20[1])
    x_values30 = np.linspace(0, 1, N30)
    h30 = abs(x_values30[0] - x_values30[1])

    # Раскомментируйте, чтобы запустить
    # Аналитический метод
    # analytics(N10, N20, N30)

    # Метод Эйлера
    # eyler(x_values10, x_values20, x_values30, y_values10, y_values20, y_values30, h10, h20, h30)

    # Метод Тейлора
    # teylor(x_values10, x_values20, x_values30, y_values10, y_values20, y_values30, h10, h20, h30)

    # Метод трапеций
    # trapezoid(x_values10, x_values20, x_values30, y_values10, y_values20, y_values30, h10, h20, h30)

    # Функции для сравнения при N = 10,20,30
    # all_func(h10, N10)
    # all_func(h20, N20)
    # all_func(h30, N30)
