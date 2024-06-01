import math
import matplotlib.pyplot as plt

import numpy as np


def analytics_func(x):
    return math.exp(-x) + math.exp(x) + 4 * pow(x, 2) - 4 * x - 2


def analytics(n):
    x_values = np.linspace(0, 1, n)
    y_values = np.array([analytics_func(x) for x in x_values])
    return y_values


def runge_kutta(nu, h, x_values, n):
    y_values = np.zeros(n)
    z_values = np.zeros(n)

    z_values[0] = nu
    for i, value in enumerate(x_values):
        k_1 = h * z_values[i]
        l_1 = h * (y_values[i] + 4 * x_values[i] - 4 * pow(x_values[i], 2) + 10)
        k_2 = (z_values[i] + l_1 / 2) * h
        l_2 = h * (y_values[i] + k_1 / 2 + 4 * (x_values[i] + h / 2) -
                   4 * pow((x_values[i] + h / 2), 2) + 10)
        k_3 = (z_values[i] + l_2 / 2) * h
        l_3 = h * (y_values[i] + k_2 / 2 + 4 * (x_values[i] + h / 2) -
                   4 * pow((x_values[i] + h / 2), 2) + 10)
        k_4 = (z_values[i] + l_3) * h
        l_4 = h * (y_values[i] + k_3 + 4 * (x_values[i] + h) -
                   4 * pow(x_values[i] + h, 2) + 10)
        y_values[i + 1] = y_values[i] + 1 / 6 * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
        z_values[i + 1] = z_values[i] + 1 / 6 * (l_1 + 2 * l_2 + 2 * l_3 + l_4)
    return y_values, z_values


def func_fi(y, z):
    return z + y - 2 * math.e - 2


def progonka(n):
    h = 1 / n
    data_lambda = []
    data_mu = []
    lamb = 0
    mu = 0
    data_lambda.append(lamb)
    data_mu.append(mu)
    for i in range(1, n + 1):
        lamb, mu = find_lambda_and_mu(lamb, mu, i, h)
        data_lambda.append(lamb)
        data_mu.append(mu)
    length = len(data_lambda)
    data_lambda[length - 1] = 0
    data_mu[length - 1] = (2 * (2 * math.e + 2) * h - 10 * pow(h, 2)) / (
            2 + 2 * h + h * h)
    data_mu[length - 1] = math.e + 1 / math.e - 2

    data_y = []
    y = data_mu[length - 1]
    for k in range(length, 0, -1):
        y = data_lambda[k - 1] * y + data_mu[k - 1]
        data_y.append(y)
    return list(reversed(data_y))


def find_lambda_and_mu(lamb, mu, i, h):
    temp = lamb
    lamb = 1 / (h * h + 2 - temp)
    mu = (mu - h * h * (4 * h * i * (1 - h * i) + 10)) / (h * h + 2 - temp)
    return lamb, mu


def shootting(n):
    x_values = np.linspace(0, 1, n)
    epsilon = math.pow(10, -5)
    step = 1 / n
    mu = -3
    mu_prev = -4
    y, z = runge_kutta(mu_prev, step, x_values, n + 1)
    fi_mu_prev = func_fi(y[n], z[n])
    while math.fabs(mu - mu_prev) > epsilon:
        y, z = runge_kutta(mu, step, x_values, n + 1)
        fi_mu = func_fi(y[n], z[n])
        temp = mu
        mu = mu - fi_mu / (fi_mu - fi_mu_prev) * (mu - mu_prev)
        mu_prev = temp
        fi_mu_prev = fi_mu
    return runge_kutta(mu, step, x_values, n + 1)[0]


if __name__ == "__main__":
    # n задаёт количество разбиений отрезка
    n = 10
    x_values = np.linspace(0, 1, n)

    # Аналитическое решение
    y_val2 = analytics(n)
    # Метод стрельбы
    y_shoot = shootting(n - 1)
    # Метод прогонки
    y_val = progonka(n - 1)

    plt.plot(x_values, y_val2, label="Аналитичесое", color='red')
    plt.plot(x_values, y_shoot, label="Стрельба", color='orange')
    plt.plot(x_values, y_val, label="Прогонка", color='green')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('N = ' + str(n))
    plt.grid(True)
    plt.legend()
    plt.show()