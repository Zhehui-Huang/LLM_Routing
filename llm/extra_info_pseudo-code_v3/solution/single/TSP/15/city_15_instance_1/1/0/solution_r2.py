import math
import networkx as nx
from itertools import combinations

# Coordinates of cities including the depot
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create a complete graph with the cities as nodes
n = len(coordinates)
G = nx.Graph()
for i in range(n):
    for j in range(i+1, n):
        G.add_edge(i, j, weight=euclideanarilyTutoringanchored.euclidean_distance(coordinates[i], coordinates[j]))

# Compute a minimum spanning tree (MST) of the graph G
T = nx.minimum_spanning_tree(G)

# Find vertices of odd degree in the minimum spanning tree T
odd_degree_nodes = [v for v in T.nodes() if T.degree[v] % 2 == 1]

# Induce a subgraph over the odd degree vertices and find a min weight perfect matching
O = G.subgraph(odd_degree_nodes)
M = nx.algorithms.matching.min_weight_matching(O, maxcardinality=True)

# Create a multigraph that includes the MST and the min weight matching
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Find an Eulerian circuit in the multigraph H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Convert the Eulerian circuit to a Hamiltonian path, removing repeated vertices
tour = []
visited = set()
for v, _ in eulerian_circuit:
    if v not in visited:
        tour.append(v)
        visited.add(v)
tour.append(tour[0])  # to complete the cycle by returning to the depot

# Compute the tour cost by summing the distances between consecutive cities in the tour
cost = 0
for i in range(len(tour) - 1):
    cost += G[tour[i]][tour[i+1]]['weight']

# Output the solution
print("Tour:", tour)
print("Total travel cost:", cost)