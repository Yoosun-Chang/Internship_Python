def dijkstra(graph, start):
    # 각 노드로부터의 최단 거리를 저장할 딕셔너리 초기화
    # 초기 거리를 무한대(float('inf'))로 설정
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # 시작 노드의 거리는 0

    # 아직 방문하지 않은 노드들을 저장할 리스트 초기화
    unvisited_nodes = list(graph.keys())

    while unvisited_nodes:
        current_node = None

        # 아직 방문하지 않은 노드 중에서 거리가 가장 짧은 노드 선택
        for node in unvisited_nodes:
            if current_node is None:
                current_node = node
            elif distances[node] < distances[current_node]:
                current_node = node

        # 모든 노드를 방문했거나 모든 노드에 대한 최단 거리를 찾은 경우 종료
        if distances[current_node] == float('inf'):
            break

        unvisited_nodes.remove(current_node)

        # 선택한 노드를 경유해서 인접 노드들의 최단 거리 갱신
        for neighbor, weight in graph[current_node].items():
            candidate_distance = distances[current_node] + weight

            # 더 짧은 경로를 찾은 경우 최단 거리 갱신
            if candidate_distance < distances[neighbor]:
                distances[neighbor] = candidate_distance

    return distances

# 예제 그래프 정의
graph = {
    '1': {'2': 2, '4': 1},
    '2': {'3': 3, '4': 2},
    '3': {'2': 3, '5': 1, '6': 5},
    '4': {'2': 2, '5': 1},
    '5': {'3': 1, '4': 1, '6': 2},
    '6': {'3': 5, '5': 2}
}

# 다익스트라 알고리즘 실행 및 결과 출력
start_node = '1'
shortest_distances = dijkstra(graph, start_node)
print(shortest_distances)
