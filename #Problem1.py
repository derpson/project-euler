#Problem 1


def natural_num():
    total = 0
    for num in range(1,1000):
        if (num % 3 == 0 | num % 5 == 0):
            total += num
    return total

if __name__ == '__main__':
    print natural_num()
