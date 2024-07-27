import math
from itertools import permutations

# Coordinates of the cities, indexed from 0 to 19
coordinates = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Creating dictionary to hold distances
distances = {}
for i in coordinates:
    for j in coordinates:
        if i != j:
            distances[(i, j)] = euclidean_distance(coordinates[i], coordinates[j])

def find_hamiltonian_path(max_distance):
    # Generating all permutations of cities except the depot to avoid a combinatorially explosive number of checks
    for perm in permutations(range(1, len(coordinates))):
        perm = (0,) + perm + (0,)
        valid = True
        max_edge_length = 0
        tour_cost = 0
        
        # Check this permutation's distance constraints
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

# Refine the bounding procedure with binary search
def bottleneck_tsp():
    low, high = 0, max(distances.values())
    best_path = []
    best_cost = 10000  # large number to start with
    best_max_dist = high

    while low < high - 1e-5:  # A small epsilon for floating point comparison
        mid = (low + high) / 2
        has_path, path, cost, max_dist = find_hamiltonian_path(mid)
        if has_path:
            if max_dist < best_max_dist:
                best_path = path
                best_cost = cost
                best_max_dist = max_dist
            high = mid  # search for a potentially smaller max distance
        else:
            low = mid  # allow a larger max distance

    return best_path, best_cost, best_max_color

# Execute the revised bottleneck TSP function
tour, total_cost, max_consecutive_distance = bottleneck_tep()

# Output the result
print("Tour:", list(tour))
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_consecutive_distance, 2))