graph = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': [],
    'd': [],
    'e': []
}

visited = []
queue = []


def bfsSearch(node):
    queue.append(node)
    visited.append(node)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)


print('BFS search from \'a\'')
bfsSearch('a')
