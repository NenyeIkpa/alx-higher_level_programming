#!/usr/bin/python3
def pow(a, b):
    product = 1
    while (b != 0):
        if (b > 0):
            product *= a
            b = b - 1
        else:
            product /= a
            b = b + 1
    return round(product, 16)
