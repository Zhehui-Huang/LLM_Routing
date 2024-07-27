import math
import networkx as nx

# Coordinates of the cities
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50),
    4: (21, 23), 5: (88, 59), 6: (79, 77), 7: (63, 23),
    8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create complete graph from the cities
G = nx.Graph()

# Add edges between every pair of nodes with their Euclidean distance as the weight
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=calculate_distance(cities[i], cities[j]))

# Find the Minimum Spanning Tree (MST)
MST = nx.minimum_spanning_tree(G)

# Identify vertices of odd degree in the MST to form a subgraph
odd_degree_nodes = [v for v, d in MST.degree() if d % 2 == 1]
subgraph = G.subgraph(odd_degree_nodes)

# Find Minimum-Cost Perfect Matching among odd degree nodes
matches = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add matched edges to the MST resulting in an Eulerian graph
MST.add_edges_from(matches)

# Find an Eulerian circuit in the graph
eulerian_circuit = list(nx.eulerian_circuit(MST, source=0))

# Convert Eulerian circuit to a Hamiltonian path (tsp tour)
visited = set()
tour = []
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        tour.append(v)
        visited.add(v)
tour.append(0)  # to return to the starting point

# Calculate the total travel cost of the tour
total_cost = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Results output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")