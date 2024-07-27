import math
from itertools import combinations
import networkx as nx

# Define cities coordinates
cities = [
    (90, 3),     # City 0: Depot
    (11, 17),    # City 1
    (7, 27),     # City 2
    (95, 81),    # City 3
    (41, 54),    # City 4
    (31, 35),    # City 5
    (23, 95),    # City 6
    (20, 56),    # City 7
    (49, 29),    # City 8
    (13, 17)     # City 9
]

# Calculate Euclidean distance between two cities
def distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

# Create graph and compute all pairs distances
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=distance(cities[i], cities[j]))

# Step 1: Calculate the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in the MST
odd_degree_nodes = [node for node, degree in mst.degree if degree % 2 == 1]

# Create subgraph induced by vertices with odd degree
odd_graph = G.subgraph(odd_degree_nodes)

# Step 3: Minimum-Cost Perfect Matching (MCPM)
min_cost_perfect_matching = nx.algorithms.matching.max_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Step 4: Combine the MST and the MCPM to create an Eulerian multigraph
multi_graph = nx.MultiGraph(mst)
for u, v in min_cost_perfect_matching:
    multi_graph.add_edge(u, v, weight=G[u][v]['weight'])  # Add edges from MCPM to MST 

# Step 5: Find an Eulerian circuit in the augmented graph
euler_tour = list(nx.eulerian_circuit(multi_graph, source=0))

# Step 6: Convert Eulerian Circuit to Hamiltonian Circuit
visited = set()
hamiltonian_circuit = [0]
for u, v in euler_tour:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)

# Calculate total distance of the tour
total_distance = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the tour and total distance
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_distance)