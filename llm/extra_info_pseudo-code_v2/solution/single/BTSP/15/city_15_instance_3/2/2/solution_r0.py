import math
from itertools import combinations
import networkx as nx

# Coordinates of each city, index represents the city number
cities = [
    (16, 90),  # Depot City 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Compute Euclidean distance between two points
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initializing full graph
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=distance(i, j))

# Sort edges based on their weight
edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Bottleneck-optimal Biconnected Subgraph algorithm (Step 1)
def find_biconnected_subgraph():
    E_BB = set()
    G_BB = nx.Graph()
    G_BB.add_nodes_from(G.nodes())
    for (u, v, data) in edges_sorted:
        G_BB.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(G_BB):
            return G_BB, data['weight']
    return None, None

# Construct biconnected subgraph (Initialization)
G_BB, c_BB = find_biconnected_subgraph()

# Find a Approximate optimal Hamiltonian cycle (Step 2)
def find_approximate_hamiltonian(G_BB):
    # Create 2-factor of biconnected subgraph
    edges = list(nx.minimum_weighted_edge_cover(G_BB))
    HG = nx.Graph()
    HG.add_edges_from(edges)
    WG = nx.Graph()

    # Checking if a Hamiltonian circuit exists
    cycle = nx.approximation.traveling_salesman_problem(HG, cycle=True, weight='weight')
    if cycle[0] != cycle[-1]:
        cycle.append(cycle[0])
    path_length = sum(G.edges[cycle[i], cycle[i+1]]['weight'] for i in range(len(cycle)-1))
    max_distance = max(G.edges[cycle[i], cycle[i+1]][', for i in range(len(cycle)-1)])

    return cycle, path_length, max_distance

# Extracting the tour data
tour, total_cost, max_dist = find_approximate_hamiltonhubcycle(G_BB)

# Output final result as per format requirements
print(f'Tour: {tour}')
print(f'Total travel cost: {total_cost}')
print(f'Maximum distance between consecutive cities: {max_dist}')