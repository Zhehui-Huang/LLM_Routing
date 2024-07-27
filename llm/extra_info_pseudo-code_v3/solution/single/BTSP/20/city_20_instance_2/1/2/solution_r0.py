from math import sqrt
import itertools

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Function to check Hamiltonian cycle in the Bottleneck graph
def has_hamiltonian_cycle(perm, distances, threshold):
    total_cost = 0
    max_leg = 0
    n = len(perm)
    
    for i in range(n):
        dist = distances[perm[i]][perm[(i + 1) % n]]
        if dist > threshold:
            return False, None, None
        total_cost += dist
        max_leg = max(max_leg, dist)
    
    return True, total_cost, max_leg

# Initial city coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Calculate distances
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]
edges = []

for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = euclidean_distance(cities[i], cities[j])
        distances[i][j] = dist
        distances[j][i] = dist
        edges.append((dist, i, j))

# Sort edges by distance
edges.sort()

# Main BTSP algorithm
for threshold, _, _ in edges:
    # Generate all permutations for Hamiltonian cycle checking, skipping city 0 initially
    for perm in itertools.permutations(range(1, num_cities)):
        # Add city 0 at start and end
        tour = [0] + list(perm) + [0]
        has_cycle, total_cost, max_leg = has_hamiltonian_cycle(tour, distances, threshold)
        
        if has_cycle:
            print(f"Tour: {tour}\nTotal travel cost: {total_cost}\nMaximum distance between consecutive cities: {max_leg}")
            break
    else:
        continue
    break