#Problem 2


def fibonacci():
    a = 1
    b = 1
    total = 0
    while total <= 4000000:
        if not b % 2:
            total += b
        a, b = b, a + b
    return total

if __name__ == '__main__':
    print fibonacci()
