from collections import deque

# dijkstra's algorithm using heap (includes path)


class MinHeap:
    def __init__(self):
        self.heap = [[0, '']]
        self.size = 0

    def siftup(self, ind):
        while (ind >> 1) > 0:
            if self.heap[ind][0] < self.heap[ind >> 1][0]:
                self.heap[ind >> 1][0], self.heap[ind] = self.heap[ind][0], self.heap[ind >> 1][0]

            ind >>= 1

    def insert(self, k, node):
        self.heap.append([k, node])
        self.size = self.size + 1
        self.siftup(self.size)

    def siftdown(self, ind):
        while (ind << 1) <= self.size:
            mc = self.min_child(ind)
            if self.heap[ind][0] > self.heap[mc][0]:
                self.heap[ind][0], self.heap[mc][0] = self.heap[mc][0], self.heap[ind][0]

            ind = mc

    def min_child(self, ind):
        if (ind << 1) >= self.size:
            return ind << 1
        else:
            if self.heap[ind << 1][0] < self.heap[ind << 1 | 1][0]:
                return ind << 1
            else:
                return ind << 1 | 1

    def pop(self):
        if self.size == 0:
            return None

        node = self.heap[1][1]

        if self.size == 1:
            self.heap.pop()
        else:
            self.heap[1] = self.heap.pop()

        self.size -= 1
        self.siftdown(1)

        return node

    def build(self, arr):
        ind = len(arr) // 2
        self.size = len(arr)
        self.heap = [0] + arr

        while ind > 0:
            self.siftdown(ind)
            ind = ind - 1


def dijkstra(graph: dict, start, end, path=False):
    """
    :param graph: should be a dict with dicts of weights
    :param start: starting vertex
    :param end: ending vertex
    :param path: True -> returns distance, path
                 False -> only distance
    """

    dists = {el: float('inf') for el in graph.keys()}
    visited = {el: False for el in graph.keys()}
    parents = {el: None for el in graph.keys()}

    dists[start] = 0

    heap = MinHeap()
    heap.build([[0, start]])

    while heap.size != 0:
        node = heap.pop()

        if visited[node]:
            continue

        for v in graph[node].keys():
            if dists[v] > dists[node] + graph[node][v]:
                dists[v] = dists[node] + graph[node][v]
                parents[v] = node

            heap.insert(dists[v], v)

        visited[node] = True

    if path:
        path = [end]

        cur = parents[end]
        while cur != start:
            path.append(cur)
            cur = parents[cur]

        return dists[end], path[::-1]

    return dists[end]
