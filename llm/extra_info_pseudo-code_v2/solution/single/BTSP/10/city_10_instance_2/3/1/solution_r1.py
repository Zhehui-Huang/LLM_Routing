import math
from itertools import permutations
import networkx as nx

# Coordinates for cities including the depot
coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Hardware graph structure
G = nx.complete_graph(10)
for i, j in permutations(coordinates.keys(), 2):
    G[i][j]['weight'] = euclidean_distance(i, j)

# Step 1: Bottleneck-optimal biconnected subgraph
def algorithm_BB(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda e: e[2]['weight'])
    E_BB = nx.Graph()
    E_BB.add_nodes_from(G.nodes())
    
    for edge in sorted_edges:
        E_BB.add_edge(edge[0], edge[1], weight=edge[2]['qual_weight'])
        if nx.is_biconnected(E_BB):
            c_BB = max([E_BB[u][v]['weight'] for u, v in E_BB.edges()])
            return E_BB, c_BB
    
    # Fallback if not biconnected
    c_BB = max([G[u][v]['weight'] for u,v in E_BB.edges()])
    return E_BB, c_BB

E_BB, c_BB = algorithm_BB(G)

# Step 2: Tour Identification
def identify_tour(E_BB):
    # Start with either a minimum spanning tree of E_BB or directly
    mst = nx.minimum_spanning_tree(E_BB) # We use E_BB which is guaranteed to be biconnected and not empty
    eulerian_graph = nx.DiGraph()
    eulerian_graph.add_edges_from(mst.edges(data=True))
    
    # Since the graph might not be the strongest for Euler's, re-add edges conservatively
    for u, v, data in G.edges(data=True):
        if not eulerian_graph.has_edge(u, v):
            eulerian_graph.add_edge(u, v, weight=data['weight'])

    # Create an Eulerian circuit, convert to Hamiltonian by skipping revisited nodes
    eulerian_circuit = list(nx.eulerian_circuit(nx.eulerize(eulerian_graph), source=0))
    tour = []
    visited = set()
    
    for u, v in eulerian_circuit:
        if v not in visited:
            tour.append(v)
            visited.add(v)
    tour.append(0)  # Ending at the Depot
    return tour

tour = identify_tour(E_BB)

# Compute total travel cost and maximum distance
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
max_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Print the outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")