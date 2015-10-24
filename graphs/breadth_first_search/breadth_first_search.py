# https://en.wikipedia.org/wiki/Depth-first_search
graph = {'A': set(['B', 'C', 'E']),
         'B': set(['A', 'D', 'F']),
         'C': set(['A', 'G']),
         'D': set(['B']),
         'E': set(['A', 'F']),
         'F': set(['B', 'E']),
         'G': set(['C'])}

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

print bfs(graph, 'A')
