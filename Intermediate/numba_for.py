from timeit import timeit
from numba import jit


@jit(nopython=True)
def while_loop(n=100_000_000):
    i = 0
    sum = 0
    while i < n:
        sum += i
        i += 1
    return sum


print("While Loop \t\t", timeit(while_loop, number=1))
