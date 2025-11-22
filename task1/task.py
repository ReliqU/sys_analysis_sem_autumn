from typing import List


def create_graph(data: str) -> List[List]:
    lines = data.split("\n")
    connections = [line.split(",") for line in lines]
    neighbors_map = {}
    nodes = set()
    for connection in connections:
        nodes.add(connection[0])
        nodes.add(connection[1])
        if neighbors_map.get(connection[0]):
            neighbors_map[connection[0]].append(connection[1])
        else:
            neighbors_map[connection[0]] = [connection[1]]
    matrix = []
    for source in sorted(list(nodes)):
        new_row = [0] * len(nodes)
        adjacent = (
            neighbors_map.get(source)
            if neighbors_map.get(source)
            else []
        )
        for target in sorted(adjacent):
            new_row[int(target) - 1] = 1 if target in adjacent else False
        matrix.append(new_row)
    return matrix


def find_start(data: str):
    return int([line.split(",") for line in data.split("\n")][0][0])


def traverse(graph, visited, current):
    visited[current] = 1
    for neighbor_index in range(len(graph[current])):
        if not visited[neighbor_index]:
            if graph[current][neighbor_index]:
                traverse(graph, visited, neighbor_index)
    return visited


def analyze(data: str):
    adj_matrix = create_graph(data)
    size = len(adj_matrix[0])
    zeros = [[0 for _ in range(size)] for _ in range(size)]
    start_node = find_start(data)
    result1 = adj_matrix
    result2 = []
    for col in range(size):
        result2.append([r[col] for r in adj_matrix])
    result3 = [traverse(adj_matrix, [0 for i in range(size)], node) for node in range(size)]
    result4 = []
    for col in range(size):
        result4.append([r[col] for r in result3])
    result5 = zeros.copy()
    for i in range(size):
        for j in range(size):
            result5[i][j] = 1 if result3[i][j] and result3[j][i] else 0
    return (result1, result2, result3, result4, result5)


for matrix in analyze("1,2\n1,3\n3,4\n3,5\n5,6\n6,7"):
    for row in matrix:
        print(row)
    print()