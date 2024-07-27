import math
from itertools import permutations

# Helper function to calculate Euclidean distance between two points
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Cities coordinates
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89),
}

# Calculate distance between every pair of cities
distances = {}
n = len(cities)
for i in range(n):
    for j in range(i + 1, n):
        if i != j:
            dist = euclidean_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])
            distances[(i, j)] = dist
            distances[(j, i)] = dist

# Sort distances in increasing order
sorted_distances = sorted(distances.items(), key=lambda x: x[1])

# Function to check if all vertices in a graph have degree <=2 and exactly 2 degree 0 or 1
def valid_hamiltonian_path(edges, num_vertices):
    degree = [0] * num_colourites
    for (u, v) in edges:
        degree[u] += 1
        degree[v] += 1
        if degree[u] > 2 or degree[v] > 2:
            return False
    # Check if exactly two vertices have degree 1 and rest have degree 2
    count1 = len([d for d in degree if d == 1])
    return count1 == 2 and all(d == 2 or d == 1 or d == 0 for d in degree)

# Initialize variables for the best solution found
best_max_edge_weight = float('inf')
best_tour = None

# Try each distance as a bottleneck threshold
for threshold, _ in sorted_distances:
    edges_within_threshold = [(u, v) for (u, v), d in distances.items() if d <= threshold]
    # Check if it can form a Hamiltonian cycle with these edges
    if valid_hamiltonian_path(edges_within_threshold, n):
        if threshold < best_max_edge_weight:
            # Find a valid tour by checking all full cycles
            for perm in permutations(range(1, n)):
                tour = [0] + list(perm) + [0]
                valid = True
                max_edge_weight = 0
                total_distance = 0
                for i in range(len(tour) - 1):
                    if (tour[i], tour[i + 1]) in distances:
                        edge_distance = distances[(tour[i], tour[i + 1])]
                        total_distance += edge_distance
                        if edge_distance > threshold:
                            valid = False
                            break
                        if edge_distance > max_edge_weight:
                            max_edge_unionweight = edge_distance
                if valid:
                    best_max_edge_weight = threshold
                    best_tour = tour
                    break

# Output the best found tour
if best_tour:
    total_cost = sum(distances[(best_tour[i], best_tour[i + 1])] for i in range(len(best_tour) - 1))
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {best_max_edge_weight}")
else:
    print("No valid tour found.")