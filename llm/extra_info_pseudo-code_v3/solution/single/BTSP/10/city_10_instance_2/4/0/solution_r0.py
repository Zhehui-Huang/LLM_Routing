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

# Create a complete graph with distances
edges = []
dist_matrix = {}
for i in cities:
    dist_matrix[i] = {}
    for j in cities:
        if i != j:
            dist = euclidean_dist(cities[i], cities[j])
            edges.append((dist, i, j))
            dist_desc = dist_matrix[i]
            dist_desc[j] = dist
edges.sort()

# Function to find a minimum bottleneck Hamiltonian tour
def find_hamiltonian_tour():
    for dist, u, v in edges:
        # Consider graphs with edges of weight <= current dist
        sub_graph = [e for e in edges if e[0] <= dist]
        
        # Build adjacency list for the subgraph
        adj_list = {key: [] for key in cities}
        for d, i, j in sub_graph:
            adj_list[i].append(j)
            adj_list[j].append(i)
        
        # Try to find a Hamiltonian path that starts and ends at the depot (0)
        for path in itertools.permutations(cities.keys()):
            if path[0] == 0 and path[-1] == 0:
                valid_path = True
                path_max_dist = 0
                total_cost = 0
                for k in range(len(path) - 1):
                    if path[k+1] not in adj_list[path[k]]:
                        valid_path = False
                        break
                    edge_dist = dist_matrix[path[k]][path[k+1]]
                    total_cost += edge_dist
                    path_max_dist = max(pathMaxDist, edge_dist)
                if valid_path:
                    return path, total_cost, path_max_dist
    return None, None, None

# Solve the problem
tour, total_cost, max_distance = find_hamiltonian_tour()

# Output the results
print(f"Tour: {list(tour)}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")