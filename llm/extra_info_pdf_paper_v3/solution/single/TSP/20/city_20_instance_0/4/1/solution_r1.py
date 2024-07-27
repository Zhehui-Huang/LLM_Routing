import math
import networkx as nx

# Data coordinates for the cities
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Creating the complete graph with weighted edges between the cities
G = nx.Graph()
for i in cities.keys():
    for j in cities.keys():
        if i != j:
            G.add_edge(i, j, weight=distance(i, j))

# Generate a Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Finding vertices with odd degree in the MST to perform perfect matching
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Minimum Weight Perfect Matching in the subgraph of the MST with odd degree vertices
min_weight_matching = nx.algorithms.matching.min_weight_matching(G.subgraph(odd_degree_nodes), maxcardinality=True, weight='weight')

# Adding the perfect matching edges to the MST
mst.add_edges_from(min_weight_matching)

# Creating an Eulerian circuit from the improved MST
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Converting the Eulerian circuit to a Hamiltonian circuit by skipping repeated nodes
visited = set()
hamiltonian_circuit = [0]

for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Making sure to return to the starting city
hamiltonian_circuit.append(0)

# Calculating the total travel cost
total_cost = sum(distance(hamiltonian_circuit[i], hamiltonian_circuit[i+1]) for i in range(len(hamiltonian_circuit) - 1))

# Outputing the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)