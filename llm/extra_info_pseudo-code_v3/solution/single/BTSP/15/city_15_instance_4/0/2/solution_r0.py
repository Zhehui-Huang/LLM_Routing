import numpy as np
from itertools import permutations

def calculate_distance(coord1, coord2):
    """ Calculate the Euclidean distance between two points. """
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def get_edges_and_weights(coords):
    """ Generate all edges with their weights from given coordinates. """
    num_cities = len(coords)
    edges = []
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = calculate_distance(coords[i], coords[j])
            edges.append(((i, j), distance))
            edges.append(((j, i), distance))
    return edges

def find_tour(coords):
    num_cities = len(coords)
    edges = get_edges_and_weights(coords)
    sorted_edges = sorted(edges, key=lambda x: x[1])
    
    # Test all weight thresholds from the smallest to the largest edge
    for cutoff in [edge[1] for edge in sorted_edges]:
        adjacency = {i: [] for i in range(num_cities)}
        
        # Construct a graph with the current cutoff
        for ((u, v), weight) in sorted_edges:
            if weight <= cutoff:
                adjacency[u].append(v)
                adjacency[v].append(u)
        
        # Try to find a Hamiltonian path
        for permutation in permutations(range(num_cities)):
            valid = True
            max_distance = -1
            path_cost = 0
            
            # Check if permutation forms a valid tour
            for i in range(len(permutation) - 1):
                if permutation[i+1] not in adjacency[permutation[i]]:
                    valid = False
                    break
                distance = calculate_distance(coords[permutation[i]], coords[permutation[i+1]])
                path_cost += distance
                if distance > max_distance:
                    max_distance = distance
            
            if valid:
                start_to_first = calculate_distance(coords[0], coords[permutation[0]])
                end_to_start = calculate_distance(coords[permutation[-1]], coords[0])
                path_cost += start_to_first + end_to_start
                if max(start_to_first, end_to_start) > max_distance:
                    max_distance = max(start_to_first, end_to_start)
                
                if permutation[0] == 0 and valid:
                    final_path = list(permutation) + [0]
                    return final_path, path_cost, max_distance

    return [], 0, 0

# Coordinates of each city
coords = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

tour, total_cost, max_distance = find_tour(coords)
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")