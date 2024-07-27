import math
import itertools
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

# Define the cities and their coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Compute Euclidean distance between two cities
def euclidean_dist(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Create the graph with edge weights
edges = []
n = len(cities)
for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_dist(i, j)
        edges.append((i, j, dist))
        edges.append((j, i, dist))
edges.sort(key=lambda x: x[2])

# Main heuristic algorithm to minimize the max distance between consecutive cities
def find_bottleneck_tour():
    for threshold in map(lambda e: e[2], edges):
        # Build the bottleneck graph for the current threshold
        filtered_edges = [(u, v) for u, v, d in edges if d <= threshold]
        graph = csr_matrix((n, n))
        graph[filtered_edges] = 1
        num_components, labels = connected_components(csgraph=graph, directed=False)
        
        if num_components == 1:
            # Try to find Hamiltonian Cycle
            for perm in itertools.permutations(range(1, n)):
                tour = [0] + list(perm) + [0]
                valid_tour = True
                max_edge = 0
                total_cost = 0
                for k in range(len(tour) - 1):
                    weight = euclidean_dist(tour[k], tour[k+1])
                    if weight > threshold:
                        valid_tour = False
                        break
                    max_edge = max(max_edge, weight)
                    total_cost += weight

                if valid_tour:
                    return tour, total_cost, max_edge
    
    return None

# Get the tour, total cost, and the maximum edge distance
result = find_bottleneck_tour()
if result:
    tour, total_cost, max_dist = result
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_dist}")
else:
    print("No valid tour found")