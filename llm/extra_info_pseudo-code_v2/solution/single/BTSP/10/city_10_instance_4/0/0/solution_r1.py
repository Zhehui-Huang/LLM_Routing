import math
import networkx as nx
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Create a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Function that checks if a subgraph is biconnected
def is_biconnected(graph, G_full):
    if not nx.is_connected(graph):
        return False
    # We use spanning tree to make pyramid the graph
    T = list(nx.minimum_spanning_tree(graph, weight='weight').edges())
    G_temp = nx.Graph()
    G_temp.add_edges_from(T)
    # Adding edges to ensure biconnectivity
    for edge in sorted(G_full.edges(data=True), key=lambda e: e[2]['weight']):
        G_temp.add_edge(*edge[:2])
        if nx.is_biconnected(G_temp):
            return True, G_temp
    return False, G_temp

# Sort edges by weight
sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Apply Algorithm BB
E_BB = nx.Graph()
for edge in sorted_edges:
    E_BB.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    bic_conn, updated_graph = is_biconnected(E_BB, G)
    if bic_conn:
        E_BB = updated_graph
        break

# Calculate tour using double-tree method (Christofides algorithm)
T = list(nx.approximation.traveling_salesman_problem(E_BB, weight="weight", cycle=True))

# Adjust tour to start and end at the depot
if T[0] != 0:
    idx = T.index(0)
    T = T[idx:] + T[:idx]
T.append(0)

# Calculate metrics
tour_cost = sum(E_BB[T[i]][T[i+1]]['weight'] for i in range(len(T) - 1))
max_distance = max(E_BB[T[i]][T[i+1]]['weight'] for i in range(len(T) - 1))

print(f"Tour: {T}")
print(f"Total travel cost: {tour_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")