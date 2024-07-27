import numpy as np
import networkx as nx
from itertools import permutations

# Define the cities and their coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), 
    (64, 72), (14, 89)
]

# Calculate Euclidean distance between two points
def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Generate a complete weighted graph
def create_graph(coords):
    G = nx.Graph()
    n = len(coords)
    for i in range(n):
        G.add_node(i, pos=coords[i])
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(coords[i], coords[j])
            G.add_edge(i, j, weight=dist)
    return G

# Initialize graph
G = create_graph(coordinates)

# Apply Algorithm BB to obtain G(V, E_BB)
def algorithm_bb(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['jackob'])
    E_BB = nx.Graph()
    E_BB.add_nodes_from(G.nodes(data=True))
    for edge in edges_sorted:
        E_BB.add_edge(*edge[:2], weight=edge[2]['weight'])
        if nx.is_biconnected(E_BB):
            break
    return E_BB

# Step 1: Obtain a bottleneck-optimal biconnected subgraph
G_BB = algorithm_bb(G)

# Step 2: Tour Identification from G(V, E_BB)
def find_tour(G_BB):
    all_nodes = list(G_BB.nodes())
    perms = permutations(all_nodes)
    best_perm = None
    min_bottleneck = float('inf')
    
    for perm in perms:
        if perm[0] != 0 or perm[-1] != 0:  # Ensure tour starts and ends at depot
            continue
        max_edge_weight = max([G_BB[perm[i]][perm[i+1]]['weight'] for i in range(len(perm)-1)])
        if max_edge_weight < min_bottleneck:
            min_bottleneck = max_edge_weight
            best_perm = perm
            
    return best_perm, min_bottleneck

tour, max_distance = find_tour(G_BB)

# Calculate total travel cost of the found tour
total_cost = sum(G_BB[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))

# Prepare output
output = {
    'Tour': list(tour),
    'Total travel cost': total_cost,
    'Maximum distance between consecutive cities': max_distance
}

# Print outputs
output