import math
import networkx as nx
from itertools import combinations

# Define cities coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate Euclidean distances
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Complete Graph
G = nx.Graph()

# Add edges with weights calculated by distance
for (u, v) in combinations(cities.keys(), 2):
    G.add_edge(u, v, weight=calc_distance(u, v))

# Minimum Spanning Tree
MST = nx.minimum_spanning_tree(G)

# Find vertices of odd degree in MST
odd_degree_nodes = [v for v, deg in MST.degree() if deg % 2 == 1]

# Create subgraph of these odd degree vertices
subgraph = G.subgraph(odd_degree_nodes)
# Find minimum weight perfect matching in this subgraph to get the even degree
min_weight_matching = nx.algorithms.max_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add the minimum weight matching edges to the MST
MST_with_matching = MST.copy()
for u, v in min_weight_matching:
    if not MST_with_matching.has_edge(u, v):
        MST_with_matching.add_edge(u, v, weight=calc_distance(u, v))

# Generate an Eulerian Circuit from the MST with added matching edges
eulerian_circuit = list(nx.eulerian_circuit(MST_with_matching, source=0))

# Convert the Eulerian circuit to a Hamiltonian cycle
visited = set()
hamiltonian_cycle = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_cycle.append(v)
        visited.add(v)
hamiltonian_cycle.append(0)  # returning to the depot

# Calculate total distance of the Hamiltonian cycle
total_cost = sum(G[hamiltonian_cycle[i]][hamiltonian_cycle[i+1]]['weight'] for i in range(len(hamiltonian_cycle) - 1))

# Print the results
print(f"Tour: {hamiltonian_cycle}")
print(f"Total travel cost: {total_cost}")