
from timeit import timeit
import numpy as np


def while_loop(n=100_000_000):
    i = 0
    sum = 0
    while i < n:
        sum += i
        i += 1
    return sum


def for_loop(n=100_000_000):
    sum = 0
    for i in range(n):
        sum += 1
    return sum


def for_loop_inc(n=100_000_000):
    """ FOR """
    sum = 0
    x = 0
    for i in range(n):
        sum += i
        x += 1
    return sum


def for_loop_test(n=100_000_000):
    sum = 0
    for i in range(n):
        if i < n:
            pass
        sum += i
    return sum


def for_loop_inc_test(n=100_000_000):
    sum = 0
    x = 0
    for i in range(n):
        if i < n:
            pass
        x += 1
        sum += i
    return sum


def sum_numpy(n=100_000_000):
    return np.sum(np.arange(n))


print("While Loop \t\t", timeit(while_loop, number=1))
print("For Loop \t\t", timeit(for_loop, number=1))
print('for + inc \t\t', timeit(for_loop_inc, number=1))
print('for + test\t\t', timeit(for_loop_test, number=1))
print('for inctest\t\t', timeit(for_loop_inc_test, number=1))
print('sum numpy\t\t', timeit(sum_numpy, number=1))
