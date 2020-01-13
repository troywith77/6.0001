epsilon = 0.00000001


def square_root(x):
    g = 0.1

    def guess(g):
        if (abs(x - g ** 2) <= epsilon):
            return g
        else:
            return guess((g + (x / g)) / 2)

    result = guess(g)
    print(result)


square_root(4)
