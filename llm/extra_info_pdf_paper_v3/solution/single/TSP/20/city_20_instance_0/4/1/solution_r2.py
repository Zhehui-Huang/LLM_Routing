import math
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

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
def euclidean_dist(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Creating a distance matrix
city_indices = list(cities.keys())
distances = distance_matrix([cities[i] for i in city_indices], [cities[i] for i in city_indices])

# Creating a complete graph from the cities
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i+1, len(cities)):
        G.edges[i, j]['weight'] = distances[i][j]

# Generate a Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Finding vertices with odd degree in the MST to perform perfect matching
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Minimum Weight Perfect Matching in the subgraph of the MST with odd degree vertices
odd_subgraph = nx.Graph(mst.subgraph(odd_degree_nodes))
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Adding the perfect matching edges to the MST
mst.add_edges_from(min_weight_matching)

# Creating an Eulerian circuit from the improved MST
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Converting the Eulerian circuit to a Hamiltonian circuit by skipping repeated nodes
visited = set()
hamiltonian_circuit = [0]

for _, v in eulerian_circuit:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Calculating the total travel cost
total_cost = sum(euclidean_dist(hamiltonian_circuit[i], hamiltonian_circuit[i+1]) for i in range(len(hamiltonian_circuit) - 1))

# Outputing the results
output_tour = "Tour: " + str(hamiltonian_circuit)
output_cost = "Total travel cost: " + str(total_cost)
print(output_tour)
print(output_cost)