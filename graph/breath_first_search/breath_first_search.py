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
