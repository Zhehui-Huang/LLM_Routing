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

# Sort the edges based on the distance in non-decreasing order
sorted_edges = sorted(distances.items(), key=lambda item: item[1])

def find_hamiltonian_path(max_distance):
    # Use permutations to check if a valid tour exists within the given max distance
    for perm in permutations(range(1, len(coordinates))):
        perm = (0,) + perm + (0,)  # start and end at the depot city 0
        valid = True
        max_edge_length = 0
        tour_cost = 0
        
        for i in range(len(perm) - 1):
            dist = distances[(perm[i], perm[i+1])]
            if dist > max_distance:
                valid = False
                break
            tour_cost += dist
            if dist > max_edge_length:
                max_edge_length = dist
        
        if valid:
            return True, perm, tour_cost, max_edge_length
    return False, [], 0, 0

# Main function to determine the minimal maximum distance Hamiltonian path
def bottleneck_tsp():
    low, high = 0, max(distances.values())
    best_path = []
    best_cost = 0
    best_max_dist = float('inf')
    
    while low <= high:
        mid = (low + high) / 2
        has_path, path, cost, max_dist = find_hamiltonian_path(mid)
        if has_path:
            best_path = path
            best_cost = cost
            best_max_dist = max_dist
            high = mid - 0.1  # decrement to search for a smaller max distance
        else:
            low = mid + 0.1  # increment to allow a larger max distance
    
    return best_path, best_cost, best_max_dist

# Execute the bottleneck TSP function
tour, total_cost, max_consecutive_distance = bottleneck_tsp()

# Output the result
print("Tour:", list(tour))
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_consecutive_distance, 2))