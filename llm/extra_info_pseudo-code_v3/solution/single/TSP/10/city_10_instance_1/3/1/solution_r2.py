from math import sqrt
import networkx as nx

# Function to compute Euclidean distance between two points
def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities and their coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Create a complete graph G
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(cities[i], cities[j]))

# Compute a minimum spanning tree (MST) of G
MST = nx.minimum_spanning_tree(G)

# Identifying vertices with odd degree in MST
odd_degree_vertices = [v for v in MST.nodes if MST.degree(v) % 2 == 1]

# Minimum weight perfect matching for the odd degree vertices subgraph
odd_subgraph = G.subgraph(odd_degree_vertices)
min_weight_match = nx.algorithms.matching.min_weight_matching(odd_subgraph, True)

# Add the edges from the minimum weight matching to the MST
MST.add_edges_from(min_weight_match)

# Create an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(MST, source=0))

# Creating a Hamiltonian circuit by skipping visited nodes
visit_order = []
seen = set()
for u, v in eulerian_circuit:
    if u not in seen:
        visit_order.append(u)
        seen.add(u)
visit_order.append(visit_order[0])  # return to starting point

# Computing the total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(visit_order[:-1], visit_log[1:]))

print("Tour:", visit_order)
print("Total travel cost:", total_cost)