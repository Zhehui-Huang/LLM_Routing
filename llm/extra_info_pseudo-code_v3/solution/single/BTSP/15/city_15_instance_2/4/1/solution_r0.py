import numpy as np
from itertools import permutations

# City coordinates
city_coordinates = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
                    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
                    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99), (54, 87)]

def calculate_euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def create_distance_matrix(coords):
    num_cities = len(coords)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                matrix[i][j] = calculate_euclidean_distance(coords[i], coords[j])
    return matrix

def find_hamiltonian_path_bottleneck(graph, ci):
    n = len(graph)
    for perm in permutations(range(1, n)):
        path = [0] + list(perm) + [0]
        valid = True
        max_edge = 0
        for i in range(len(path) - 1):
            if graph[path[i]][path[i+1]] > ci:
                valid = False
                break
            max_edge = max(max_edge, graph[path[i]][path[i+1]])
        if valid:
            return path, max_edge
    return None, None

def bottleneck_tsp_algorithm(distance_matrix):
    edges = [(i, j, distance_matrix[i][j]) for i in range(len(distance_matrix)) for j in range(i+1, len(distance_matrix))]
    edges_sorted = sorted(edges, key=lambda x: x[2])
    
    for edge in edges_sorted:
        ci = edge[2]  # Current max weight considered
        graph_under_ci = [[0 if distance_matrix[i][j] > ci else distance_matrix[i][j] for j in range(len(distance_vector))] for i, distance_vector in enumerate(distance_matrix)]
        
        path, max_edge = find_hamiltonian_path_bottleneck(graph_under_ci, ci)
        if path is not None:
            return path, sum(distance_matrix[path[i]][path[i+1]] for i in range(len(path)-1)), max_edge
    
    return None

distance_matrix = create_distance_matrix(city_coordinates)
tour, total_cost, max_distance = bottleneck_tsp_algorithm(distance_matrix)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)