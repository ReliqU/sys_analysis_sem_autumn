from typing import List, Tuple
import csv
import math
from collections import defaultdict

def read_csv_data(input_string: str) -> List[Tuple[str, str]]:
    csv_reader = csv.reader(input_string.splitlines())
    return [(items[0].strip(), items[1].strip()) for items in csv_reader]

def create_tree_structure(connections: List[Tuple[str, str]]) -> dict:
    tree = defaultdict(list)
    for parent_node, child_node in connections:
        tree[parent_node].append(child_node)
    return tree

def compute_tree_entropy(tree_structure: dict, start_node: str) -> float:
    if start_node not in tree_structure:
        return 0.0

    def count_nodes(current_node: str) -> int:
        if current_node not in tree_structure or not tree_structure[current_node]:
            return 1
        total = 1
        for descendant in tree_structure[current_node]:
            total += count_nodes(descendant)
        return total

    sizes_list = []
    for node in tree_structure:
        sizes_list.append(count_nodes(node))

    all_nodes_count = sum(sizes_list)
    probs = [size_val / all_nodes_count for size_val in sizes_list]

    entropy_value = -sum(prob * math.log2(prob) for prob in probs if prob > 0)
    return entropy_value

def compute_normalized_complexity(tree_structure: dict) -> float:
    total_edges = sum(len(children_list) for children_list in tree_structure.values())
    total_nodes = len(tree_structure)
    if total_nodes <= 1:
        return 0.0

    normalized_complexity = total_edges / (total_nodes * (total_nodes - 1))
    return normalized_complexity

def analyze_tree(input_string: str, root_node: str) -> Tuple[float, float]:
    connections_list = read_csv_data(input_string)

    tree_dict = create_tree_structure(connections_list)

    entropy_result = compute_tree_entropy(tree_dict, root_node)

    complexity_result = compute_normalized_complexity(tree_dict)

    return (round(entropy_result, 1), round(complexity_result, 1))