import csv


def main(csv_file_path: str) -> list[list[int]]:
    """
    Преобразует граф из списка ребер в CSV-файле в матрицу смежности.

    Args:
      csv_file_path: Путь к файлу CSV, где каждая строка представляет ребро
                     в виде двух вершин, разделенных запятой.

    Returns:
      Двумерный массив (список списков), представляющий матрицу смежности графа.
    """
    edges = []
    max_node = 0

    with open(csv_file_path, mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if not row:
                continue
            u, v = int(row[0]), int(row[1])
            edges.append((u, v))
            if u > max_node:
                max_node = u
            if v > max_node:
                max_node = v

    size = max_node + 1

    adjacency_matrix = [[0] * size for _ in range(size)]
    for u, v in edges:
        adjacency_matrix[u][v] = 1
        adjacency_matrix[v][u] = 1

    return adjacency_matrix