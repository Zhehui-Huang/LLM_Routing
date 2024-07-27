import math
import networkx as nx
from scipy.spatial import distance

# Coordinates of the cities including the depot city at index 0
city_coords = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph with cities as nodes
G = nx.Graph()
num_cities = len(city_coords)

for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.add_edge(i, j, weight=euclidean_distance(city_coords[i], city_coords[j]))

# Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find all vertices with odd degree in the MST
odd_vertices = [v for v, d in mst.degree() if d % 2 == 1]

# Build a complete graph on the odd degree vertices
odd_graph = nx.Graph()
for i in range(len(odd_vertices)):
    for j in range(i + 1, len(odd_vertices)):
        u, v = odd_vertices[i], odd_vertices[j]
        odd_graph.add_edge(u, v, weight=euclidean_distance(city_coords[u], city_coords[v]))

# Find the minimum weight perfect matching (MWPM) in the subgraph of odd degree vertices
matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Add the edges from MWPM to the MST to get an Eulerian circuit
mst.add_edges_from(matching)

# Find an Eulerian cycle on this augmented graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert the Eulerian cycle to a Hamiltonian cycle (shortcutting)
tour = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)
tour.append(0)  # return to the depot

# Calculate the total cost
total_cost = 0
for i in range(1, len(tour)):
    total_cost += euclidean_distance(city_coords[tour[i - 1]], city_coords[tour[i]])

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")