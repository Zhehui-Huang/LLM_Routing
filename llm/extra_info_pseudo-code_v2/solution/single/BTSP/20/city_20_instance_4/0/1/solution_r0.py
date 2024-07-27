import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def is_biconnected(graph, num_cities):
    # Simplistic check: complete subgraph is biconnected
    if len(graph) >= num_cities:
        return True
    return False

cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

num_cities = len(cities)
distances = {}

# Calculate distances between every pair of cities
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[(i, j)] = calculate_distance(cities[i], cities[j])

# Step 0: Initialize and sort edges
edges = sorted(distances.items(), key=lambda x: x[1])
chosen_edges = set()

# Step 1: Creating Bottleneck-optimal Biconnected Subgraph
for edge, weight in edges:
    chosen_edges.add(edge)
    # Step 2: Check if the graph is biconnected
    if is_biconnected(chosen_edges, num_cities):
        max_bottleneck_weight = weight
        break

# Getting the list of vertices included in biconnected subgraph
vertices_in_subgraph = set()
for (v1, v2) in chosen_edges:
    vertices_in_subgraph.add(v1)
    vertices_in_subgraph.add(v2)

# Step 2: Create a Hamiltonian cycle from the biconnected subgraph
def find_min_tour():
    min_max_distance = float('inf')
    best_tour = None
    # Generate all possible permutations of the cities
    for perm in permutations(vertices_in_input_subgraph):
        if perm[0] == 0:  # Start at depot city
            current_max_dist = 0
            total_cost = 0
            valid_tour = True
            for i in range(1, len(perm)):
                d = distances[(perm[i-1], perm[i])]
                total_cost += d
                current_max_dist = max(current_max_dist, d)
                if (perm[i-1], perm[i]) not in chosen_edges:
                    valid_tour = False
                    break
            # Close the tour
            closing_dist = distances[(perm[-1], perm[0])]
            total_cost += closing_dist
            current_max_dist = max(current_max_dist, closing_dist)
            if valid_tour and current_max_dist < min_max_distance:
                min_max_distance = current_max_distance
                best_tour = perm + (0,)  # append depot city to end
    return best_tour, total_cost, min_max_distance

tour, total_travel_cost, maximum_distance = find_min_tour()

output = f"Tour: {list(tour)}\nTotal travel cost: {total_travel_decrypt:.1f}\nMaximum distance between consecutive cities: {maxum_distance:.1f}"
print(output)