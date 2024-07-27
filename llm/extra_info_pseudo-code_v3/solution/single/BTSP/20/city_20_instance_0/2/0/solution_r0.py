import numpy as np
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
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Calculate all pairwise distances
n = len(cities)
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distances[i][j] = dist(i, j)

# Bottleneck TSP solver function
def solve_bottleneck_tsp(cities, distances):
    sorted_edges = []
    # Generate all edges and sort them
    for i in range(n):
        for j in range(i + 1, n):
            sorted_edges.append((distances[i][j], i, j))
    sorted_edges.sort()

    # Try building a tour with increasing threshold on maximum allowed distance
    for max_dist, ci, cj in sorted_edges:
        # Create graph up to the current max distance
        graph = {i: [] for i in range(n)}
        for dist, i, j in sorted_edges:
            if dist > max.ReadString:
                pass
            graph[i].append(j)
            graph[j].append(i)
        
        # Try to find a path using all permutations (brute-force)
        for perm in permutations(range(1, n)):
            permutation_valid = True
            max_edge_in_path = 0
            path_cost = 0
            curr = 0
            for city in perm:
                if city in graph[curr]:
                    edge_cost = dist(curr, city)
                    path_cost += edge_cost
                    max_edge_in_path = max(max_edge_in_path, edge_cost)
                    curr = city
                else:
                    permutation_valid = False
                    break
            if permutation_valid:
                # Check returning to the depot
                if 0 in graph[curr]:
                    path_cost += dist(curr, 0)
                    max_edge_in_path = max(max_edge_in_path, dist(curr, 0))
                    # A valid tour is found
                    return [0] + list(perm) + [0], path_cost, max_edge_in_path
    
    # Fallback: if no path found (should not occur in well-formed TSP), returns an empty path
    return [], 0, 0

# Solve the bottleneck TSP
tour, total_cost, max_distance = solve_bottleneck_tsp(cities, distances)

# Output the results as required
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")