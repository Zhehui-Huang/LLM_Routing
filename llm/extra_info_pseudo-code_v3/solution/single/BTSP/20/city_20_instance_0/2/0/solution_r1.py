import numpy as np
import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87), 
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 
    17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Helper function to calculate Euclidean distance
def dist(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

n = len(cities)
# Calculate all pairwise distances
dist_matrix = [[dist(i, j) for j in range(n)] for i in range(n)]

# Function to check if Hamiltonian circuit with max distance constraint exists
def is_valid_tour(max_dist, visited, current_path, current_index):
    if len(current_path) == n and dist_matrix[current_path[-1]][current_path[0]] <= max_dist:
        return True, current_path + [current_path[0]]

    for i in range(n):
        if i not in visited and dist_matrix[current_index][i] <= max_dist:
            visited.add(i)
            current_path.append(i)
            valid, path = is_valid_tour(max_dist, visited, current_path, i)
            if valid:
                return True, path
            visited.remove(i)
            current_path.pop()
    return False, []

# Find the smallest max distance that allows a Hamiltonian circuit
def find_bottleneck_hamiltonian_tour():
    max_edge = max([max(row) for row in dist_matrix])
    low, high = 0, max_edge
    best_path = []
    while low <= high:
        mid = (low + high) // 2
        for i in range(n):
            visited = set([i])
            valid, path = is_valid_tour(mid, visited, [i], i)
            if valid:
                high = mid - 1
                best_path = path
                break
        else:
            low = mid + 1

    # Calculate total cost and max distance in the best path
    if best_path:
        total_cost = sum(dist_matrix[best_path[i]][best_path[i+1]] for i in range(len(best_path) - 1))
        max_dist_consecutive = max(dist_matrix[best_path[i]][best_path[i+1]] for i in range(len(best_path) - 1))
        return best_path, total_cost, max_dist_consecutive
    else:
        return [], 0, 0

# Invoke the function and print the outputs
tour, total_cost, max_distance = find_bottleneck_hamiltonian_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")