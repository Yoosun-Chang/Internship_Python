def dijkstra(graph, start):
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  

    unvisited_nodes = list(graph.keys())

    while unvisited_nodes:
        current_node = None

        for node in unvisited_nodes:
            if current_node is None:
                current_node = node
            elif distances[node] < distances[current_node]:
                current_node = node

        if distances[current_node] == float('inf'):
            break

        unvisited_nodes.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            candidate_distance = distances[current_node] + weight

            if candidate_distance < distances[neighbor]:
                distances[neighbor] = candidate_distance

    return distances

graph = {
    '1': {'2': 2, '4': 1},
    '2': {'3': 3, '4': 2},
    '3': {'2': 3, '5': 1, '6': 5},
    '4': {'2': 2, '5': 1},
    '5': {'3': 1, '4': 1, '6': 2},
    '6': {'3': 5, '5': 2}
}

start_node = '1'
shortest_distances = dijkstra(graph, start_node)
print(shortest_distances)
