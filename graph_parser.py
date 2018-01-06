import numpy as np
from re import search

PATH = "split-0.dag"
GRAPH_DATA = "graph.txt"


def parse_file():
    with open(PATH, 'r') as f:
        with open(GRAPH_DATA, 'w') as f2:
            for line in f:
                if line.startswith(('PARENT', 'CHILD')):
                    f2.write(line)


def create_empty_matrix():
    graph_set = set()
    with open(GRAPH_DATA, 'r') as f:
        for line in f:
            data = line.split()
            graph_set.update(data)
    graph_set = remove_data(graph_set)
    sez_size = len(graph_set)
    return np.zeros((sez_size, sez_size)), graph_set


def create_adjacency_matrix(adjacency_matrix, dict_data):
    with open(GRAPH_DATA, 'r') as f:
        for line in f:
            parent = search(r'(?<=\bPARENT\s)(\s+\w+)', line).group()
            child = search(r'(?<=\bCHILD)(\s+\w+)', line).group()
            parent_id = dict_data.get(parent.strip())
            child_id = dict_data.get(child.strip())
            matrix[parent_id][child_id] = 1
    return adjacency_matrix


def remove_data(graph_set):
    graph_set.remove('PARENT')
    graph_set.remove('CHILD')
    return graph_set


def unique_dict_entry(graph_set):
    return {v: k for k, v in enumerate(graph_set)}


if __name__ == '__main__':
    parse_file()
    matrix, data = create_empty_matrix()
    data = unique_dict_entry(data)
    a_matrix = create_adjacency_matrix(matrix, data)
    print(a_matrix)