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

# Building the graph with respective weights (distances)
G = nx.Graph()
number_of_cities = len(city_coordinates)

for i in range(number_of_cities):
    for j in range(i + 1, number_of_cities):
        distance = euclidean_distance(city_coordinates[i], city_coordinates[j])
        G.add_edge(i, j, weight=distance)

# Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Finding odd degree vertices from MST
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Graph induced by odd_degree_nodes
subgraph = G.subgraph(odd_degree_nodes)

# Minimum weight perfect matching
# As not all algorithms support providing this natively, we use the networkx.algorithms.matching
# Here we need to use the method "max_weight_matching" and get the minimum by negating weights
min_weight_matching = nx.algorithms.matching.max_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Adding the edges of the minimum weight perfect matching to the MST
mst.add_edges_from(min_weight_matching)

# Forming an Eulerian circuit from the MST with added edges (which should be Eulerian now)
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Making the circuit Hamiltonian by visiting each node only once
visited = set()
hamiltonian_circuit = [0]

for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
    if len(visited) == number_of_cities - 1:
        break
    
# Completing the tour at the depot
hamiltonian_circuit.append(0)

# Calculating the total cost of the Hamiltonian circuit
total_cost = sum(euclidean_distance(city_coordinates[hamiltonian_circuit[i]], city_coordinates[hamiltonian_circuit[i + 1]]) for i in range(len(hamiltonian_circuit) - 1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", round(total_cost, 2))