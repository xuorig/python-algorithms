import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def __contains__(self, item):
        return item in self.elements

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]
