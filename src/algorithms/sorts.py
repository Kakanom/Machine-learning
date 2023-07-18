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
