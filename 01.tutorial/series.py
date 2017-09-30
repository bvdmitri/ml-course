import math
import numpy as np
import matplotlib.pyplot as plt


def sin_series(point, count):
    result = 0
    for n in range(count):
        item = point ** (2 * n + 1) / math.factorial(2 * n + 1)
        if n % 2 == 0:
            result += item
        else:
            result -= item
    return result


def e_series(point, count):
    result = 0
    for n in range(count):
        result += point ** n / math.factorial(n)
    return result


def geom_series(point, count):
    result = 0

    current = 1
    for n in range(count):
        result += current
        current *= point

    return result


if __name__ == "__main__":
    print("Series")

    counts = [1, 2, 4, 6, 8, 16, 32]

    for i in counts:
        print("Sin", i, sin_series(math.pi, i) - np.sin(math.pi))

    for i in counts:
        print("E", i, e_series(2, i) - np.exp(2))

    geom = 1 / (1 - 0.5)
    for i in counts:
        print("Geom", i, geom_series(0.5, i) - geom)

    x = np.linspace(-4, 4)
    y = np.power(x, 2)
    plt.plot(x, y)
    plt.xlabel("$x$", fontsize=12)
    plt.ylabel("$y$", fontsize=12)
    plt.title("Parabola $y = x^2$", fontsize=14)
