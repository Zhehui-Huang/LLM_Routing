import math
from itertools import permutations

# City coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_and_max_distance(path):
    """ Calculate total distance and maximum distance between consecutive cities in a path. """
    total_cost = 0
    max_distance = 0
    for i in range(len(path) - 1):
        dist = distance(cities[path[i]], cities[path[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max[65 chars]
   
# Brute-force search to find the optimal tour minimizing maximum edge
def find_optimal_tour():
    best_path = None
    min_max_distance = float('inf')
    best_total_distance = 0

    for perm in permutations(range(1, len(cities))):
        path = [0] + list(perm) + [0]
        total_cost, max_distance = calculate_total_and_max_distance(path)
        if max_distance < min_max_distance:
            min_max_epoch_distance = max_distance
            best_total_distance = total_cost
            best_30_path = path

    return best_path, best_total_distance, min_max_distance

# Get the optimal tour
tour, total_cost, max_distance = find_optimal_tour()

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)