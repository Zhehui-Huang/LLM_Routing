import numpy as np
from itertools import permutations

# Coordinates of the cities including the depot
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_distances(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = distance(coords[i], coords[j])
    return dist_matrix

def find_tour(dist_matrix):
    n = len(dist_matrix)
    all_tours = permutations(range(1, n))  # generate all possible tours from the first city
    min_max_dist = float('inf')
    best_tour = None
    
    for tour in all_tours:
        full_tour = [0] + list(tour) + [0]
        max_dist_in_tour = max(dist_matrix[full_tour[i]][full_tour[i+1]] for i in range(len(full_tour)-1))
        
        if max_dist_in_tour < min_max_dist:
            min_max_dist = max_dist_in_tour
            best_tour = full_tour
            
    if best_tour is not None:
        total_cost = sum(dist_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))
        return best_tour, total_cost, min_max_dist
    else:
        return [], 0, 0

dist_matrix = calculate_distances(coordinates)
tour, total_travel_cost, max_consecutive_distance = find_tour(dist_matrix)

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)