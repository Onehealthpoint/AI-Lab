import heapq


def astar_search(graph, start, goal):
    visited = set()
    priority_queue = [(0, start, [])]

    while priority_queue:
        cost, current_node, path = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        path = path + [current_node]

        if current_node == goal:
            print("Goal reached! Path:", path)
            return path

        visited.add(current_node)

        for neighbor, neighbor_cost in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + neighbor_cost + heuristic(neighbor), neighbor, path))

    print("Goal not reached.")
    return None


def heuristic(node):
    heuristic_values = {
        'A': 5,
        'B': 2,
        'C': 6,
        'D': 4,
        'E': 7
    }
    return heuristic_values[node]


graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('E', 3)],
    'C': [('A', 4), ('E', 5)],
    'D': [('B', 3)],
    'E': [('C', 5)]
}

start_node = 'A'
goal_node = 'E'
astar_search(graph, start_node, goal_node)
