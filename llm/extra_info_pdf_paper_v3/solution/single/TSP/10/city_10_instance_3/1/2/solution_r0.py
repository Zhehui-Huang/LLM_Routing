import math
from itertools import combinations
import networkx as nx

# Provided cities with their coordinates
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

def euclidean_distance(c1, c2):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate the distances between each city pair
distances = {}
for (i, coord_i), (j, coord_j) in combinations(cities.items(), 2):
    dist = euclidean_distance(coord_i, coord_j)
    distances[i, j] = dist
    distances[j, i] = dist  # Symmetric distances

# Create a graph from the city distances
G = nx.Graph()
for (i, j), dist in distances.items():
    G.add_edge(i, j, weight=dist)

# Find the minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find vertices with odd degree in the MST
odd_degree_nodes = [v for v in mst.nodes if mst.degree[v] % 2 != 0]

# Find minimum weight perfect matching for odd degree nodes
odd_degree_subgraph = nx.Graph()
odd_degree_subgraph.add_nodes_from(odd_degree_nodes)
for u, v in combinations(odd_degree_nodes, 2):
    if u != v:
        odd_degree_subgraph.add_edge(u, v, weight=distances[u, v])

matching = nx.algorithms.matching.min_weight_matching(odd_degree_subgraph, maxcardinality=True)

# Add matching edges to the MST
mst_with_matching = mst.copy()
for u, v in matching:
    mst_with_matching.add_edge(u, v, weight=distances[u, v])

# Create an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst_with_matching))

# Convert Eulerian circuit to Hamiltonian circuit by skipping visited nodes
visited = set()
hamiltonian_circuit = []
total_cost = 0

for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    # Sum the travel cost
    total_cost += distances[u, v]
hamiltonian_circuit.append(hamiltonian_circuit[0])  # Return to the starting city
total_cost += distances[hamiltonian_circuit[-2], hamiltonian_circuit[-1]]  # Cost to return to start

print(f"Tour: {hamiltonian_circuit}\nTotal travel cost: {total_cost}")