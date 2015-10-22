from collections import deque, defaultdict
from utils.priority_queue import PriorityQueue

# https://en.wikipedia.org/wiki/Depth-first_search
graph = {'A': set(['B', 'C', 'E']),
         'B': set(['A', 'D', 'F']),
         'C': set(['A', 'G']),
         'D': set(['B']),
         'E': set(['A', 'F']),
         'F': set(['B', 'E']),
         'G': set(['C'])}

graph_with_weights = {
  'A': set([('B', 2),('C', 4),('D', 1)]),
  'B': set([('A', 2),('E', 4),('F', 6)]),
  'C': set([('A', 4),('F',3)]),
  'D': set([('A', 1),('G', 8)]),
  'E': set([('B', 4)]),
  'F': set([('B',6),('C',3),('G',2)]),
  'G': set([('F',2),('G', 8)])
}


class GraphAlgorithms(object):
    @staticmethod
    def dfs(graph, start):
        marked = set()
        stack = [start]
        while stack:
            top = stack.pop()
            if top not in marked:
                marked.add(top)
                for v in graph[top]:
                    stack.append(v)
        return marked

    @staticmethod
    def bfs(graph, start):
        marked = set()
        queue = deque([start]) # deque for fast popleft
        while queue:
            vertex = queue.popleft()
            if vertex not in marked:
                marked.add(vertex)
                for v in graph[vertex]:
                    queue.append(v)
        return marked

    @staticmethod
    def a_star(graph, start, goal):

        def heuristic(start, goal):
            return 1

        def reconstruct_path(came_from, goal):
            # do it
            return []

        def dist_between(node, node):
            # do it
            return 1

        open_queue = PriorityQueue()
        closed = set()

        came_from = {}
        g_score = defaultdict(inf)
        g_score[start] = 0

        f_score = defaultdict(inf)
        f_score[start] = g_score[start] + heuristic(start, goal)

        while not open_queue.empty():
            current = open_queue.get()
            if current is goal:
                return reconstruct_path(came_from, goal)

            close_set.add(current)
            for neighbor in graph[current]:
                if neighbor in closed:
                    continue
                tentative_g_score = g_score[current] + dist_between(current, neighbor)
                if neighbor not in open_queue or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                    open_queue.put(f_score[neighbor], neighbor)
        return None









    @staticmethod
    def dijkstra(graph):
        # TODO

print GraphAlgorithms.dfs(graph, 'A')
print GraphAlgorithms.bfs(graph, 'A')
