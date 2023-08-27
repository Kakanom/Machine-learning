import time


# timer
def timer(func):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = func(*args)
        print((time.perf_counter_ns() - start_time) * 1e-6, "ms")
        return res

    return wrapped
