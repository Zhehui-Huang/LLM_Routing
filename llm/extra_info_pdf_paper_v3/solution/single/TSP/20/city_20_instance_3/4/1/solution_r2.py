import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Creating a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Constructing the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Finding vertices with odd degree in MST
odd_degree_vertices = [v for v, degree in mst.degree() if degree % 2 == 1]

# Create subgraph with odd degree vertices
odd_graph = G.subgraph(odd_degree_vertices)

# Minimum-Cost Perfect Matching on the odd degree subgraph
matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Create a multigraph by adding edges to MST
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(matching)

# Convert multigraph to a single, simple graph by merging multi-edges and selecting minimum weight
simple_graph = nx.Graph()
for u, v, data in multi_graph.edges(data=True):
    weight = min(data['weight'] for data in multi_graph.get_edge_data(u, v).values())
    if simple_graph.has_edge(u, v):
        if simple_graph[u][v]['weight'] > weight:
            simple_graph[u][v]['weight'] = weight
    else:
        simple_graph.add_edge(u, v, weight=weight)

# Constructing an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(simple_graph, source=0))

# Hamiltonian circuit conversion and finding tour cost
visited = set()
hamiltonian_circuit = [0]
last_visit = 0
total_cost = 0

for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
        total_cost += simple_graph[u][v]['weight']
        last_visit = v

# Returning to the start point
if last_visit != 0:
    hamiltonian_circuit.append(0)
    total_cost += simple_graph[last_visit][0]['weight']

# Display the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")