import math
import networkx as nx
from itertools import combinations
from networkx.algorithms.matching import max_weight_matching

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities and their coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Number of cities 
n = len(cities)

# Create a complete graph with cities as nodes and distances as edge weights
G = nx.Graph()
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 1: Create a minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in the MST
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Step 3: Create a subgraph induced by vertices with odd degree
odd_subgraph = G.subgraph(odd_degree_nodes)

# Step 4: Find a minimum weight perfect matching in the induced subgraph
matching = max_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Step 5: Combine MST and the matching to get an Eulerian graph
mst.add_edges_from(matching)

# Step 6: Find an Eulerian tour
eulerian_tour = list(nx.eulerian_circuit(mst, source=0))

# Step 7: Make it a Hamiltonian path (remove repeated nodes keeping the first occurrence)
visited = set()
tour = []
for u, v in eulerian_tour:
    if u not in visited:
        tour.append(u)
        visited.add(u)
    if v not in visited:
        tour.append(v)
        visited.add(v)

# Ensure the tour starts and ends at the depot
tour.append(0)

# Step 8: Calculate the total travel cost of the tour
total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))

# Output the solution
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")