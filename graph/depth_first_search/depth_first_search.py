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
