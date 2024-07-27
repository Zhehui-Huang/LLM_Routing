import math
import networkx as nx
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates for the depot and cities
coordinates = [
    (26, 60),  # Depot city 0
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 47),  # City 14
    (19, 25),  # City 15
    (75, 9),   # City 16
    (52, 54),  # City 17
    (64, 72),  # City 18
    (14, 89)   # City 19
]

num_cities = len(coordinates)

# Create the graph
G = nx.Graph()
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = euclidean_distance(coordinates[i], coordinates[j])
        G.add_edge(i, j, weight=dist)

# Create the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find all nodes with odd degree in the MST
odd_degree_nodes = [node for node, degree in mst.degree() if degree % 2 == 1]

# Create a complete graph with all odd degree nodes
subgraph = G.subgraph(odd_degree_nodes)
complete_graph = nx.complete_graph(subgraph.nodes, create_using=nx.Graph())

# Set weights in the complete graph to original distances
for u, v in complete_graph.edges:
    complete_graph[u][v]['weight'] = G[u][v]['weight']

# Compute the Minimum Cost Perfect Matching
matched_edges = nx.algorithms.matching.min_weight_matching(complete_graph, maxcardinality=True, weight='weight')

# Add matched edges to the MST to make it Eulerian
mst.add_edges_from(matched_edges)

# Find an Eulerian tour
eulerian_tour = list(nx.eulerian_circuit(mst, source=0))

# Convert the Eulerian tour to the final tour by removing repeated nodes, ensuring all nodes are visited once
final_tour = []
visited = set()
for u, v in eulerian_tour:
    if u not in visited:
        final_tour.append(u)
        visited.add(u)
final_tour.append(0)  # Complete the tour by going back to the start

# Calculate the total cost of the tour
total_cost = sum(G[final_tour[i]][final_tour[i+1]]['weight'] for i in range(len(final_tour)-1))

print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_cost:.2f}")