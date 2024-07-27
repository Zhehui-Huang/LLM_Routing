import math
from itertools import permutations

# Coordinates of the cities, indexed from 0 to 19
coordinates = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate distances between all pairs of cities
distances = {(i, j): euclidean_escape_distance(coordinates[i], coordinates[j]) for i in coordinates for j in coordinates if i != j}
sorted_edges = sorted(distances.items(), key=lambda item: item[1])

# Define function to find Hamiltonian path
def find_hamiltonian_path(max_distance):
    nodes = list(coordinates.keys())
    for perm in permutations(nodes[1:]):  # start from 1 to exclude the depot initially for permutations
        perm = tuple([0]) + perm + tuple([0])  # Ensuring start and end at the depot 0
        valid = True
        max_edge_length = 0
        tour_cost = 0
        
        for i in range(len(perm) - 1):
            dist = distances[(perm[i], perm[i+1])]
            if dist > max_distance:
                valid = False
                break
            tour_cost += dist
            max_edge_length = max(max_edge_length, dist)
        
        if valid:
            return True, perm, tour_cost, max_edge_length
    return False, [], 0, 0

# Use binary searching to find minimal maximum edge
def bottleneck_tsp():
    low, high = 0, max(distance.values())  # Maximum possible distance as the initial high
    best_path, best_cost, best_max_dist = [], float('inf'), float('inf')
    
    while low <= high:
        mid = (low + high) / 2
        found, path, cost, max_dist = find_hamiltonian_path(mid)
        if found:
            if max_dist < best_max_dist:
                best_path, best_cost, best_max_dist = path, cost, max_dist
            high = mid - 0.01  # Narrow down with the expectation to reduce the maximum distance
        else:
            low = mid + 0.01  # Increase to allow for a feasible solution
    
    return best_path, best_cost, best_max_dist

# Execute function
tour, total_cost, max_consecutive_distance = bottleneck_tsp()

# Print results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_consecutive_distance, 2))