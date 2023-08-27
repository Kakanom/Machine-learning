# min heap
class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def siftup(self, ind):
        while (ind >> 1) > 0:
            if self.heap[ind] < self.heap[ind >> 1]:
                self.heap[ind >> 1], self.heap[ind] = self.heap[ind], self.heap[ind >> 1]

            ind >>= 1

    def insert(self, k):
        self.heap.append(k)
        self.size = self.size + 1
        self.siftup(self.size)

    def siftdown(self, ind):
        while (ind << 1) <= self.size:
            mc = self.min_child(ind)
            if self.heap[ind] > self.heap[mc]:
                self.heap[ind], self.heap[mc] = self.heap[mc], self.heap[ind]

            ind = mc

    def min_child(self, ind):
        if (ind << 1) >= self.size:
            return ind << 1
        else:
            if self.heap[ind << 1] < self.heap[ind << 1 | 1]:
                return ind << 1
            else:
                return ind << 1 | 1

    def pop(self):
        mini = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.size = self.size - 1
        self.siftdown(1)

        return mini

    def build(self, arr):
        ind = len(arr) // 2
        self.size = len(arr)
        self.heap = [0] + arr[:]

        while ind > 0:
            self.siftdown(ind)
            ind = ind - 1


# segment tree
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        tree = [0] * 2 * self.n

        for i in range(self.n):
            tree[self.n + i] = arr[i]

        for i in range(self.n - 1, 0, -1):
            tree[i] = tree[i << 1] + tree[i << 1 | 1]

        self.tree = tree

    def update(self, ind, value):
        self.tree[ind + self.n] = value
        i = ind + self.n

        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]

            i >>= 1

    def query(self, l, r):
        res = 0

        l += self.n
        r += self.n

        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1

            if r & 1:
                r -= 1
                res += self.tree[r]

            l >>= 1
            r >>= 1

        return res

#under construction
# # heap based on map
# class MapHeap:
#     def __init__(self, d):
#         self.n = len(arr)
#         tree = [0] * 2 * self.n
#
#         for i in range(self.n):
#             tree[self.n + i] = arr[i]
#
#         for i in range(self.n - 1, 0, -1):
#             tree[i] = min(tree[i << 1], tree[i << 1 | 1])
#
#         self.tree = tree
#
#     def update(self, ind: int, val: int) -> None:
#         self.tree[ind + self.n] = val
#         ind = ind + self.n
#
#         i = ind
#
#         while i > 1:
#             self.tree[i >> 1] = min(self.tree[i], self.tree[i ^ 1])
#
#             i >>= 1
#
#     def get_min(self):
#         return self.tree[1]
