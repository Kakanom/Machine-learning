import time
from random import randint

# timer
def timer(ret=False):
    def wrapper(func):
        def wrapped(*args):
            start_time = time.perf_counter_ns()
            res = func(*args)
            ms = (time.perf_counter_ns() - start_time) * 1e-6

            if ret:
                return res, ms

            print(ms, "ms")
            return res

        return wrapped

    return wrapper


# finds average sort's execution time
def test_sort(mini=0, maxi=1000000, tests=50, length=100000, ret=False):
    def wrapper(sort):
        def wrapped():
            av = 0
            for _ in range(tests):
                arr = [randint(mini, maxi) for _ in range(length)]
                start_time = time.perf_counter_ns()
                sort(arr)
                av += (time.perf_counter_ns() - start_time) * 1e-6

            if ret:
                return av / tests

            print(av / tests, 'ms average')

            return None

        return wrapped

    return wrapper


"""usage example

@test_sort(0, 1000000, 10, 100000)
def sort(arr):
    return quick_sort(arr)

sort()
"""
