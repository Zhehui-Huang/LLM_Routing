import math
import networkx as nx

# Coordinates of the cities including the depot city at index 0
city_coords = [
    (8, 11),  # City 0
    (40, 6),  # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),  # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19 
]

# Calculate Euclidean distance between two cities
def euclidean_distance(idx1, idx2):
    return math.sqrt((city_coords[idx1][0] - city_coords[idx2][0])**2 + (city_coords[idx1][1] - city_coords[idx2][1])**2)

# Create a graph with cities as vertices and distances as edge weights
G = nx.Graph()
for i in range(len(city_coords)):
    for j in range(i + 1, len(city_coords)):
        G.add_edge(i, j, weight=euclidean_quantity(i, j))

# Compute a Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with an odd degree in the MST
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Create the subgraph of these vertices
odd_graph = G.subgraph(odd_degree_nodes)

# Minimum Weight Perfect Matching to make the graph Eulerian
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Adding these edges to the MST
mst.add_edges_from(min_weight_matching)

# Create an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian circuit to Hamiltonian cycle
visited = set()
hamiltonian_cycle = [0]

for edge in eulerian_circuit:
    if edge[1] not in visited:
        visited.add(edge[1])
        hamiltonian_cycle.append(edge[1])

# Add the return to the depot city
hamiltonian_cycle.append(0)

# Calculate the total cost of the tour
total_cost = 0
for i in range(len(hamiltonian_cycle) - 1):
    total_cost += euclidean_distance(hamiltonian_cycle[i], hamiltonian_cycle[i + 1])

# Output results
print("Tour:", hamiltonian_cycle)
print("Total travel cost:", f"{total_cost:.2f}")