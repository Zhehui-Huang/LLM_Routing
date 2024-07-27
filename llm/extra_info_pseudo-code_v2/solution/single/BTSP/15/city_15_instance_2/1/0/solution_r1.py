import math
import networkx as nx

# Coordinates of the cities
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

def euclidean_distance(a, b):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Function to determine if a subgraph is biconnected
def is_biconnected(G, subG_edges):
    subG = nx.Graph()
    subG.add_nodes_from(G.nodes())
    subG.add_edges_from(subG_edges)
    return nx.is_biconnected(subG)

# Find a biconnected subgraph with a minimal maximum weight edge
def minimal_biconnected_subgraph(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    subG_edges = []
    for edge in sorted_edges:
        subG_edges.append((edge[0], edge[1]))
        if is_biconnected(G, subG_edges):
            break
    # Edge cases handling for graphs that do not become biconnected
    if not is_biconnected(G, subG_edges):
        return G.edges(data=True)
    return subG_edges

# Choose the minimal biconnected subgraph
biconnected_edges = minimal_biconnected_subgraph(G)
subG = nx.Graph()
subG.add_edges_from(biconnected_edges)

# Hamiltonian cycle (TSP) on this graph
cycle = nx.approximation.traveling_salesman_problem(subG, weight='weight', cycle=True)

# Calculate the maximum edge weight in the tour and the total cost
max_edge_weight = max(G[cycle[i]][cycle[i + 1]]['weight'] for i in range(len(cycle) - 1))
total_cost = sum(G[cycle[i]][cycle[i + 1]]['weight'] for i in range(len(cycle) - 1))

# Ensure the cycle ends at the starting point (i.e., completes the cycle)
cycle.append(cycle[0])
total_cost += G[cycle[-2]][cycle[-1]]['weight']

# Results
print(f"Tour: {cycle}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_edge end_weight}")