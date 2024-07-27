import math
import networkx as nx

# City coordinates (index corresponds to city number)
city_coordinates = [
    (79, 15),  # City 0: Depot
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities given their coordinates. """
    return math.hypot(city1[0] - city2[0], city1[1] - city2[1])

# Build graph with weights being the Euclidean distances
G = nx.Graph()
number_of_cities = len(city_coordinates)

for i in range(number_of_cities):
    for j in range(i + 1, number_of_cities):
        distance = euclidean_distance(city_coordinates[i], city_coordinates[j])
        G.add_edge(i, j, weight=distance)

# Compute Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Identify nodes of odd degree in the MST
odd_degree_nodes = [node for node, degree in mst.degree() if degree % 2 == 1]

# Minimum Cost Perfect Matching on the induced subgraph by odd-degree nodes
subgraph = G.subgraph(odd_degree_nodes)
min_cost_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Combine edges from MST and Min Cost Matching to make it Eulerian
mst.add_edges_from(min_cost_matching)

# Eulerian circuit from the Eulerian graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert this to a Hamiltonian circuit by visiting each node exactly once
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Calculate total travel cost
total_cost = sum(euclidean_distance(city_coordinates[hamiltonian_circuit[i]], city_coordinates[hamiltonian_circuit[i + 1]]) for i in range(len(hamiltonian_circuit) - 1))

# Output results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", round(total_cost, 2))