import numpy as np
import networkx as nx

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

# Distance function
def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Compute all pairwise distances
n = len(cities)
distances = {}
edges = []
for i in range(n):
    for j in range(i+1, n):
        dist = euclidean_distance(cities[i], cities[j])
        distances[(i, j)] = dist
        distances[(j, i)] = dist
        edges.append((i, j, dist))

# Sort edges by distances
edges.sort(key=lambda x: x[2])

# Bottleneck Traveling Salesman Problem Algorithm
def has_hamiltonian_cycle(G, n):
    # Using NetworkX to check for Hamiltonian cycle
    try:
        cycle = nx.algorithms.approximation.traveling_salesman_problem(G, cycle=True, method='greedy')
        if len(cycle) == n + 1 and cycle[0] == cycle[-1]:
            return cycle
    except:
        return None
    return None

# Check for the smallest bottleneck graph with a Hamiltonian cycle
for _, _, dist in edges:
    # Create bottleneck graph up to the current distance
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for (i, j, d) in edges:
        if d <= dist:
            G.add_edge(i, j, weight=d)
    
    cycle = has_hamiltonian_cycle(G, n)
    if cycle:
        # Calculating maximum edge length in the cycle and total travel cost
        max_edge_length = max(distances[(cycle[i], cycle[i+1])] for i in range(len(cycle) - 1))
        total_cost = sum(distances[(cycle[i], cycle[i+1])] for i in range(len(cycle) - 1))
        print(f"Tour: {cycle}")
        print(f"Total travel cost: {total_cost:.2f}")
        print(f"Maximum distance between consecutive cities: {max_edge_length:.2f}")
        break