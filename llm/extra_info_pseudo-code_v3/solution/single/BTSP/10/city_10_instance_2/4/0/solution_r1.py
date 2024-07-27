import math
import itertools

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to compute Euclidean distance
def euclidean_dist(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


# Create edges with distances
edges = []
for i in cities:
    for j in cities:
        if i != j:
            dist = euclidean_dist(cities[i], cities[j])
            edges.append((dist, i, j))
edges.sort()

# Function to find if a path connects all nodes exactly once and returns to start
def is_valid_hamiltonian_cycle(path, max_allowed_dist):
    start_city = path[0]
    if path[-1] != start_city:
        return False
    for i in range(len(path) - 1):
        if dist_matrix[path[i]][path[i+1]] > max_allowed_dist:
            return False
    return True

# Construct the distance matrix
dist_matrix = {i: {} for i in cities}
for dist, i, j in edges:
    dist_matrix[i][j] = dist
    dist_matrix[j][i] = dist

# Algorithm to solve the bottleneck TSP
def solve_bottleneck_tsp():
    for dist, u, v in edges:
        sub_graph = [(d, i, j) for d, i, j in edges if d <= dist]
        all_nodes = set(cities.keys())
        # Attempt to find a Hamiltonian Circuit in this sub_graph
        for path in itertools.permutations(all_nodes):
            if path[0] == 0 and is_valid_hamiltonian_cycle(path, dist):
                total_cost = sum(dist_matrix[path[k]][path[k+1]] for k in range(len(path) - 1))
                return path, total_cost, dist
    return None

# Solve the problem
solution = solve_bottleneck_tsp()
if solution:
    tour, total_cost, max_distance = solution
    print(f"Tour: {list(tour)}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
else:
    print("No solution found.")