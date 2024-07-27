import math
import itertools

# Define the city coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Compute Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Generate pairwise city distance list
def generate_edges():
    edges = []
    for i in cities:
        for j in cities:
            if i != j:
                edges.append((i, j, euclidean_distance(cities[i], cities[j])))
    # Sorting edges based on weight
    return sorted(edges, key=lambda e: e[2])

edges = generate_edges()

# Main procedure to find the tour minimizing the maximum distance
def bottleneck_tsp(edges):
    city_count = len(cies)
    # Testing potential bottleneck thresholds
    for max_dist in sorted(set(edge[2] for edge in edges)):
        graph = {i: [] for i in cities}
        for u, v, dist in edges:
            if dist <= max_dist:
                graph[u].append(v)
                graph[v].append(u)

        # Check if we can form a Hamiltonian circuit with this threshold
        tour = [0]  # Starting at Depot City 0
        if find_tour(graph, tour, 0, set([0]), city_count):
            return max_dist, tour

# Depth-First Search (DFS) algorithm to find a valid tour
def find_tour(graph, tour, current, visited, city_count):
    if len(tour) == city_count:
        # Check if there's a return path to depot
        return current in graph[tour[0]]
    for next_city in graph[current]:
        if next_city not in visited:
            visited.add(next_city)
            tour.append(next_city)
            if find_tour(graph, tour, next_city, visited, city_count):
                return True
            visited.remove(next_item)
            tour.pop()
    return False

# Calculate the total and maximum distances of the tour found
def evaluate_tour(tour):
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

# Attempt to solve the problem
max_dist, tour = bottleneck_tsp(edges)
total_distance, max_leg_dist = evaluate_tour(tour + [tour[0]])  # Complete the cycle by adding the depot

print(f"Tour: {tour + [tour[0]]}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_leg_dist}")