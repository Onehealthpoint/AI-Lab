graph = {
    'a': [],
    'b': [],
    'c': [],
    'd': [],
    'e': []
}

visited = []


def dfsSearch(node):
    if node not in visited:
        visited.append(node)
        print(node, end=' ')
        for neighbor in graph[node]:
            dfsSearch(neighbor)


print('DFS search from \'a\'')
dfsSearch('a')
