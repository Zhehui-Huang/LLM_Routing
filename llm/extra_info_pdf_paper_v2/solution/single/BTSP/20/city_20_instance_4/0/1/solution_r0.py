import math
import itertools

# City coordinates as given
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# Function to calculate Euclidean distance between two cities
def dist(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Compute distances between all city pairs
distance_matrix = [[dist(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def mst_prim(num_cities, distance_matrix):
    # Prim's algorithm to find MST
    in_mst = [False] * num_cities
    min_edge = [float('inf')] * num_cities
    parent = [-1] * num_cities
    min_edge[0] = 0
    mst_cost = 0
    edges = []

    for _ in range(num_cities):
        u = min((min_edge[i], i) for i in range(num_cities) if not in_mst[i])[1]
        in_mst[u] = True
        mst_cost += min_edge[u]
        if parent[u] != -1:
            edges.append((parent[u], u))

        for v in range(num_cities):
            if distance_matrix[u][v] < min_edge[v] and not in_mst[v]:
                min_edge[v] = distance_matrix[u][v]
                parent[v] = u

    return edges, mst_cost

def find_tour_via_mst(num_cities, mst_edges):
    # Find an eulerian circuit in the MST doubled
    from collections import defaultdict, deque

    adj_list = defaultdict(list)
    for u, v in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Hierholzer's algorithm for Eulerian circuit
    tour = []
    stack = [0]
    while stack:
        u = stack[-1]
        if adj_list[u]:
            v = adj_list[u].pop()
            adj_list[v].remove(u)
            stack.append(v)
        else:
            tour.append(stack.pop())
    return tour

# Compute the Minimum Spanning Tree (MST)
mst_edges, mst_cost = mst_prim(len(cities), distance_matrix)

# Double the edges of the MST to ensure all nodes have even degree
doubled_edges = mst_edges + [(v, u) for u, v in mst_edges]

# Find a tour from the doubled edges
tour = find_tour_via_mst(len(cities), doubled_edges)

# Remove repeated visits by introducing shortcuts and making the tour Hamiltonian
tour = [city for i, city in enumerate(tour) if city not in tour[:i]]

# Append the starting city at the end to complete the cycle
tour.append(tour[0])

# Calculate total cost and maximum distance between consecutive cities
total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_dist = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output the tour, total travel cost, and maximum distance
output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_dist
}

print(output)