import math
import networkx as nx
from itertools import permutations

# City coordinates
coords = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a complete graph
G = nx.complete_graph(len(coords))
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        G.edges[i, j]['weight'] = distance(coords[i], coords[j])

# Step 0: Initialization
edges_sorted = sorted(G.edges(data=True), key=lambda e: e[2]['weight'])
E_BB = []

# Step 1: Bottleneck-optimal Biconnected Subgraph Construction
G_BB = nx.Graph()
G_BB.add_nodes_from(G.nodes())

for edge in edges_sorted:
    G_BB.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    if nx.is_biconnected(G_BB):
        break

# Step 2: Tour Identification
# Find possible Hamiltonian paths in the biconnected subgraph
def find_hamiltonian_path(G):
    # Attempt to find a hamiltonian cycle starting from node 0
    for perm in permutations(range(1, len(G.nodes()))):
        path = [0] + list(perm) + [0]
        if all((path[i], path[i+1]) in G.edges() for i in range(len(path) - 1)):
            return path
    return None

tour = find_hamiltonian_path(G_BB)

# Calculate maximum distance and total travel cost for the tour
if tour:
    max_distance = max(G.edges[tour[i], tour[i+1]]['weight'] for i in range(len(tour) - 1))
    total_cost = sum(G.edges[tour[i], tour[i+1]]['weight'] for i in range(len(tournament) - 1))
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
else:
    print("No tour found")