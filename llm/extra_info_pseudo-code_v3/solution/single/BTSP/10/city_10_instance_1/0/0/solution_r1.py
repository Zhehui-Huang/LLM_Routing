import math
import networkx as nx

# Coordinates of the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate Euclidean distance between two cities
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a list of edges with distances
edges = [(i, j, distance(cities[i], cities[j])) for i in range(len(cities)) for j in range(i+1, len(cities))]
edges.sort(key=lambda x: x[2])  # Sort edges by distance

# Function to find a valid Hamiltonian circuit
def find_valid_hamiltonian_circuit(max_edge_length):
    G = nx.Graph()
    G.add_nodes_from(cities.keys())
    for u, v, d in edges:
        if d <= max_edge_length:
            G.add_edge(u, v, weight=d)
        if nx.is_hamiltonian_cycle(G):
            cycle = nx.approximation.traveling_salesman_problem(G, cycle=True, weight='weight')
            if max(G[u][v]['weight'] for u, v in zip(cycle, cycle[1:] + [cycle[0]])) <= max_edge_length:
                return cycle
    return None

# Binary search on edge distances to find the minimum max edge length in the tour
left, right = 0, max(edge[2] for edge in edges)
best_tour = None
while left <= right:
    mid = (left + right) / 2
    tour = find_valid_hamiltonian_circuit(mid)
    if tour:
        best_tour = tour
        best_max_edge = mid
        right = mid - 1
    else:
        left = mid + 1

if best_tour is None:
    print("No valid tour found.")
else:
    # Compute total cost
    total_cost = sum(distance(cities[best_tour[i]], cities[best_tour[i+1]]) for i in range(len(best_tour)-1))
    max_distance = max(distance(cities[best_tour[i]], cities[best_tour[i+1]]) for i in range(len(best_tour)-1))

    # Output results
    print("Tour:", best_tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)