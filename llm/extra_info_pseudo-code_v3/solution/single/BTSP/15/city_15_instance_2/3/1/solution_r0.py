import math
import itertools

# Coordinates for each city including depot
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82),
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Number of cities including the depot
n = len(coordinates)

# Function to calculate Euclidean distance between two cities
def euclidean_distance(idx1, idx2):
    x1, y1 = coordinates[idx1]
    x2, y2 = coordinates[idx2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Calculate all edge weights
edges = []
for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_distance(i, j)
        edges.append((dist, i, j))

# Sort edges based on weights (ascending order)
edges.sort()

# Function to check for Hamiltonian path in given graph G with vertices V
def hamiltonian_path_exists(V, G):
    # Using a simple heuristic of all permutations (not efficient and not for very large n)
    for perm in itertools.permutations(V):
        if perm[0] == 0:  # starting from the depot
            valid = True
            for i in range(len(perm) - 1):
                if (min(perm[i], perm[i+1]), max(perm[i], perm[i+1])) not in G:
                    valid = False
                    break
            if valid:
                return True, perm
    return False, []

# Attempt to construct the Hamiltonian cycle by increasing weights
best_path = []
min_max_edge = float('inf')
for weight, u, v in edges:
    G = set()
    # Include only those edges which are less than current threshold
    for e in edges:
        if e[0] <= weight:
            G.add((e[1], e[2]))
    
    # Check if we can find Hamiltonian path
    exists, path = hamiltonian_path_exists(list(range(n)), G)
    if exists:
        # Check if we can return to depot and calculate tour properties
        if (path[-1], 0) in G or (0, path[-1]) in G:
            path += (0,)  # Complete the cycle by returning to depot
            max_dist = 0
            total_cost = 0
            for i in range(len(path) - 1):
                dist = euclidean_distance(path[i], path[i+1])
                total_cost += dist
                if dist > max_dist:
                    max_dist = dist
            if max_dist < min_max_hamiltonian_weight:
                best_path = path
                min_max_hamiltonian_weight = max_dist
                total_hamiltonian_cost = total_cost

# Output results
print(f'Tour: {best_path}')
print(f'Total travel cost: {total_hamiltonian_cost}')
print(f'Maximum distance between consecutive cities: {min_max_hamiltonian_weight}')