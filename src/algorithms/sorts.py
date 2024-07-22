from random import randint


# merge sort
def merge(a, b):
    i, j = 0, 0
    c = []

    while i < len(a) or j < len(b):
        if j == len(b) or i < len(a) and a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    return c


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    l = merge_sort(arr[:n//2])
    r = merge_sort(arr[n//2:])

    return merge(l, r)


# quick sort

def quick_sort(arr):
    if len(arr) < 2:
        return arr

    base = arr[len(arr) // 2]
    c = arr.count(base) - 1

    a, b = [base] * (c // 2), [base] * ((c // 2) + c % 2)

    for i in range(len(arr) // 2):
        # if arr[i] == base:
        #     key = randint(1, 2)
        #
        #     if key == 1:
        #         a.append(arr[i])
        #     else:
        #         b.append(arr[i])

        if arr[i] < base:
            a.append(arr[i])
        elif arr[i] > base:
            b.append(arr[i])

    for i in range(len(arr) // 2 + 1, len(arr)):
        # if arr[i] == base:
        #     key = randint(1, 2)
        #
        #     if key == 1:
        #         a.append(arr[i])
        #     else:
        #         b.append(arr[i])

        if arr[i] < base:
            a.append(arr[i])
        elif arr[i] > base:
            b.append(arr[i])

    return quick_sort(a) + [base] + quick_sort(b)


# counting sort

def counting_sort(arr):
    mini, maxi = min(arr), max(arr)

    res = []
    nums = {num: 0 for num in range(mini, maxi + 1)}

    for num in arr:
        nums[num] += 1

    for num in range(mini, maxi):
        res += [num] * nums[num]

    return res
