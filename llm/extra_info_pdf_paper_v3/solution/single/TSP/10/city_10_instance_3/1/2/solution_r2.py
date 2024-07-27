import math
import networkx as nx

# Define the cities and their coordinates
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

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a graph to represent cities and distances
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find nodes with odd degrees in MST to perform perfect matching
odd_degree_nodes = [node for node in mst.nodes if mst.degree(node) % 2 == 1]

# Build subgraph of nodes with odd degrees
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add the minimum weight matching edges to MST
mst.add_edges_from(min_weight_matching)

# Create an Eulerian circuit from the augmented MST
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert the Eulerian circuit to a Hamiltonian circuit (visiting each city once)
visited = set()
hamiltonian_circuit = [0]  # start from the depot
last_city = 0
total_cost = 0

for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
        total_cost += G[u][v]['weight']
        last_city = v

# Add the return to the depot city
total_cost += G[last_city][0]['weight']
hamiltonian_circuit.append(0)  # return to the depot

# Output the final tour and the total travel cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)