import itertools

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Function to check if a tour is a Hamiltonian cycle under the threshold distance
def is_valid_tour(tour, distances, threshold):
    n = len(tour)
    total_cost = 0
    max_distance = 0
    
    for i in range(1, n):
        dist = distances[tour[i-1]][tour[i]]
        if dist > threshold:
            return False, 0, 0
        total_cost += dist
        max_distance = max(max_distance, dist)
    
    return True, total_cost, max_distance

# Inputs
cities = {0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56), 6: (2, 65), 7: (38, 68),
          8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41),
          16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)}

# Calculate distances matrix
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]
edges = []

for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = euclidean_distance(cities[i], cities[j])
        distances[i][j] = dist
        distances[j][i] = dist
        edges.append((dist, i, j))

# Sort edges by their distance
edges = sorted(edges)

# Trying to find the feasible tour with minimum maximum leg distance
best_tour, best_cost, best_leg = None, float('inf'), float('inf')

for threshold, _, _ in edges:
    # Approach: Attempt to formulate a valid tour under the current threshold
    for perm in itertools.permutations(range(1, num_cities)):
        tour = [0] + list(perm) + [0]
        valid, cost, max_leg = is_valid_tour(tour, distances, threshold)
        if valid:
            if max_leg < best_leg or (max_leg == best_leg and cost < best_cost):
                best_tour = tour
                best_cost = cost
                best_leg = max_leg
    if best_tour:
        break

if best_tour:
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {best_cost}")
    print(f"Maximum distance between consecutive cities: {best_leg}")
else:
qu    print("No valid tour found.")