import numpy as np
import networkx as nx

# City coordinates
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

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Number of cities
num_cities = len(cities)

# Create complete graph with cities as nodes and distances as edge weights
G = nx.complete_graph(num_cities)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.edges[i, j]['weight'] = distance(i, j)

# Algorithm BB to find bottleneck-optimal biconnected subgraph
def algorithm_bb(graph):
    edges_sorted_by_weight = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    G_bb = nx.Graph()
    G_bb.add_nodes_from(graph)
    
    for edge in edges_sorted_by_weight:
        G_bb.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(G_bb):
            break
    
    max_weight = max([G_bb.edges[e]['weight'] for e in G_bb.edges])
    return G_bb, max_weight

# Step 1: Bottleneck-optimal Biconnected Subgraph
G_bb, c_BB = algorithm_bb(G)

# Step 2: Identify an approximate optimal tour for BTSP
# Creating the square of the biconnected subgraph
G_bb_square = nx.power(G_bb, 2)

# Ensure starting and ending at the depot city 0
# Getting a Hamiltonian path using approximation method from NetworkX
cycle = nx.approximation.traveling_salesman_problem(G_bb_square, cycle=True, weight='weight')
cycle.append(cycle[0])  # make it a tour by returning to the starting point

# Calculate the total cost and the maximum distance between consecutive cities
total_cost = sum(G.edges[cycle[i], cycle[i+1]]['weight'] for i in range(len(cycle) - 1))
max_distance = max(G.edges[cycle[i], cycle[i+1]]['weight'] for i in range(len(cycle) - 1))

# Output the results
output = {
    "Tour": cycle,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_atom_distance
}

print("Tour:", output["Tour"])
print("Total travel cost:", output["Total travel_round(cost.astype(int))"])
print("Maximum distance between consecutive cities:", output["Maximum distance between consecutive cities"])