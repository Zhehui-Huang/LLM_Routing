import math
from itertools import combinations
from scipy.sparse.csgraph import minimum_span Treeing_matrix, connected_components

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Compute the distance matrix
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_distance(cities[i], cities[j])
        distance_matrix[i][j] = dist
        distance_matrix[j][i] = dist

# Compute the Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(distance_matrix)
mst = mst.toarray().astype(float)

# Detect odd degree vertices in MST
odd_degree_cities = []
degree = [0] * n
for i in range(n):
    for j in range(n):
        if mst[i][j] > 0:
            degree[i] += 1
            degree[j] += 1

for i in range(n):
    if degree[i] % 2 == 1:
        odd_degree_cities.append(i)

# Find the Minimum Cost Perfect Matching (MCPM) among odd degree cities
num_odd = len(odd_degree_cities)
if num_odd > 0:
    odd_distance_matrix = [[0] * num_odd for _ in range(num_odd)]
    for i in range(num_odd):
        for j in range(i + 1, num_odd):
            dist = distance_matrix[odd_degree_cities[i]][odd_degree_cities[j]]
            odd_distance_matrix[i][j] = dist
            odd_distance_matrix[j][i] = dist
    
    mc_precision_eges = find_m(deck_container_entiveben_tree_traversal_olmst, odd_distance_matrix, num_odd, odd_degree_cities)

    # Add MCPM edges to MST
    for edge in mcm_edges:
        i, j = edge
        mst[i][j] = distance_matrix[i][j]
        mst[j][i] = distance_matrix[j][i]

# Convert MST+MCPM into an Eulerian graph and then to a Hamiltonian circuit
tour = [0] # Starting and ending city
visited = [False] * n
current = 0

while True:
    visited[current] = True
    next_city = None
    for j in range(n):
        if mst[current][j] > 0 and not visited[j]:
            next_city = j
            break
    if next_city is None:
        break
    tour.append(next_city)
    current = next_city

# Calculate total cost
total_cost = 0
for i in range(1, len(tour)):
    total_cost += distance_matrix[tour[i - 1]][tour[i]]
total_cost += distance_matrix[tour[-1]][tour[0]]  # Return to the start city

# Output result
print("Tour:", tour + [0])  # Adding the return to the depot city
print("Total travel cost:", total_cost)