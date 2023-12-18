def yacobi():       # Метод Якоби
    eps = 0.00005
    x1_prev = 0
    x2_prev = 0
    x3_prev = 0
    x1_0 = 2.32 / 1.7
    x2_0 = 2.7 / 0.8
    x3_0 = 2.2 / 0.5
    iteration = 0

    while abs(x1_0 - x1_prev) > eps and abs(x2_0 - x2_prev) > eps and abs(x3_0 - x3_prev) > eps:
        x1_prev = x1_0
        x2_prev = x2_0
        x3_prev = x3_0
        x1_0 = (2.32 - 0.01 * x2_prev - 0.2 * x3_prev) / 1.7
        x2_0 = (2.7 + 0.1 * x1_prev - 0.4 * x3_prev) / 0.8
        x3_0 = (2.2 - 0.1 * x1_prev - 0.3 * x2_prev) / 0.5
        iteration += 1

    print(f'x1: {x1_0}\nx2: {x2_0}\nx3: {x3_0}\nn = {iteration}')


def gauss_zeydel():     # Метод Гаусса-Зейделя
    eps = 0.00005
    x1_prev = 0
    x2_prev = 0
    x3_prev = 0
    x1_0 = 2.32 / 1.7
    x2_0 = 2.7 / 0.8
    x3_0 = 2.2 / 0.5
    iteration = 0

    while abs(x1_0 - x1_prev) > eps and abs(x2_0 - x2_prev) > eps and abs(x3_0 - x3_prev) > eps:
        x1_prev = x1_0
        x2_prev = x2_0
        x3_prev = x3_0
        x1_0 = (2.32 - 0.01 * x2_prev - 0.2 * x3_prev) / 1.7
        x2_0 = (2.7 + 0.1 * x1_0 - 0.4 * x3_prev) / 0.8
        x3_0 = (2.2 - 0.1 * x1_0 - 0.3 * x2_0) / 0.5
        iteration += 1

    print(f'x1: {x1_0}\nx2: {x2_0}\nx3: {x3_0}\nn = {iteration}')


if __name__ == '__main__':
    print('Решение методом Якоби:')
    yacobi()
    print('Решение методом Гаусса-Зейделя:')
    gauss_zeydel()
