# min heap
class MinHeap:
    def __init__(self, arr):
        self.n = len(arr)
        tree = [0] * 2 * self.n

        for i in range(self.n):
            tree[self.n + i] = arr[i]

        for i in range(self.n - 1, 0, -1):
            tree[i] = min(tree[i << 1], tree[i << 1 | 1])

        self.tree = tree

    def update(self, ind: int, val: int) -> None:
        self.tree[ind + self.n] = val
        ind = ind + self.n

        i = ind

        while i > 1:
            self.tree[i >> 1] = min(self.tree[i], self.tree[i ^ 1])

            i >>= 1

    def get_min(self):
        return self.tree[1]


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

    def updateTreeNode(self, ind, value):
        self.tree[ind + self.n] = value
        ind = ind + self.n

        i = ind

        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]

            i >>= 1

    def query(self, l, r):
        res = 0

        l += self.n
        r += self.n

        while l < r:
            if (l & 1):
                res += self.tree[l]
                l += 1

            if (r & 1):
                r -= 1
                res += self.tree[r]

            l >>= 1
            r >>= 1

        return res