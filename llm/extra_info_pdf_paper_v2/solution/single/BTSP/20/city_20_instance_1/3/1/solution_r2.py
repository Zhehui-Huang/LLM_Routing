import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

# Define city coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Generate distance matrix using Euclidean distances
locations = np.array(list(cities.values()))
dist_matrix = distance_matrix(locations, locations)

# Compute a Minimum Spanning Tree (MST)
mst_matrix = minimum_spanning_tree(dist_matrix).toarray()

# DFS to find Euler tour in the MST
def dfs(node, visited, graph, tour):
    visited[node] = True
    tour.append(node)
    for neighbor in range(len(graph)):
        if graph[node][neighbor] > 0 and not visited[neighbor]:
            dfs(neighbor, visited, graph, tour)
            tour.append(node)  # add node again to simulate Eulerian cycle

# Find the Eulerian cycle using MST
visit_state = [False] * len(cities)
eulerian_cycle = []
dfs(0, visit_state, mst_matrix, eulerian_cycle)

# Reduce Eulerian cycle to Hamiltonian cycle (shortcut non-repeating nodes)
hamiltonian_cycle = []
seen = set()
for city in eulerian_cycle:
    if city not in seen:
        seen.add(city)
        hamiltonian_cycle.append(city)
hamiltonian_cycle.append(hamiltonian_cycle[0])  # add depot to make it a cycle

# Calculate total cost and maximum edge distance
total_cost = 0
max_distance = 0
for i in range(len(hamiltonian_cycle) - 1):
    city_from = hamiltonian_cycle[i]
    city_to = hamiltonian_cycle[i + 1]
    travel_cost = dist_matrix[city_from][city_to]
    total_cost += travel_cost
    if travel_cost > max_distance:
        max_distance = travel_cost

# Output results
print(f"Tour: {hamiltonian_cycle}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")