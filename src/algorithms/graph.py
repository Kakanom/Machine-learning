from collections import deque

# dijkstra's algorithm using heap (includes path it's fucking useless)


class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0
        self.dists = []

    def siftup(self, ind):
        while (ind >> 1) > 0:
            if self.dists[self.heap[ind]] < self.dists[self.heap[ind >> 1]]:
                self.heap[ind >> 1], self.heap[ind] = self.heap[ind], self.heap[ind >> 1]

            ind >>= 1

    def insert(self, node):
        self.heap.append(node)
        self.size = self.size + 1
        self.siftup(self.size)

    def siftdown(self, ind):
        while (ind << 1) <= self.size:
            mc = self.min_child(ind)
            if self.dists[self.heap[ind]] > self.dists[self.heap[mc]]:
                self.heap[ind], self.heap[mc] = self.heap[mc], self.heap[ind]

            ind = mc

    def min_child(self, ind):
        if (ind << 1) >= self.size:
            return ind << 1
        else:
            if self.dists[self.heap[ind << 1]] < self.dists[self.heap[ind << 1 | 1]]:
                return ind << 1
            else:
                return ind << 1 | 1

    def pop(self):
        if self.size == 0:
            return None

        node = self.heap[1]

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

    def setup(self, dists):
        self.dists = dists


def dijkstra(graph: dict, start, end, path=False):
    """
    :param graph: should be a dict with dicts of weights
    :param start: starting vertex
    :param end: ending vertex
    :param path: True -> returns distance, path
                 False -> only distance
    """
    dists = {el: float('inf') for el in graph.keys()}  # (dists now in the heap)
    visited = {el: False for el in graph.keys()}
    parents = {el: None for el in graph.keys()}

    heap = MinHeap()
    heap.build([start])
    heap.setup(dists)
    heap.dists[start] = 0

    while heap.size != 0:
        node = heap.pop()

        if visited[node]:
            continue

        for v in graph[node].keys():
            if heap.dists[v] > heap.dists[node] + graph[node][v]:
                heap.dists[v] = heap.dists[node] + graph[node][v]
                parents[v] = node

                heap.insert(v)

        visited[node] = True

    if path:
        path = [end]

        cur = parents[end]
        while cur != start:
            path.append(cur)
            cur = parents[cur]

        return dists[end], path[::-1]

    if dists[end] == float('inf'):
        return -1

    return dists[end]
