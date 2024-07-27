import math
import networkx as nx

# Define city coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
    (3, 21), (60, 55), (4, 39)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create graph
G = nx.Graph()
num_cities = len(cities)

# Add edges to the graph with weights
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = euclidean_distance(cities[i], cities[j])
        G.add_edge(i, j, weight=dist)

# Prim's algorithm to find the MST 
mst = nx.minimum_spanning_tree(G, algorithm='prim')

# Find vertices of odd degrees in the MST
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Create a subgraph of the MST containing only vertices of odd degree
subgraph = G.subgraph(odd_degree_nodes)

# Find minimum weight matching of the nodes with odd degree
from networkx.algorithms.matching import min_weight_matching
matching = min_weight_example_matching(subgraph, maxcardinality=True, weight='weight')

# Combine the matching and MST to form an Eulerian circuit
mst.add_edges_from(matching)

# Form an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Making a list of visited nodes from eulerian_circuit (Simple traversal, avoiding repeated cities except for return )
tour = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        tour.append(u)
    if v not in visited:
        visited.add(v)
        tour.append(v)

# Adding the start point to end of the tour to complete the cycle
tour.append(tour[0]) 

# Calculate tour cost
total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)