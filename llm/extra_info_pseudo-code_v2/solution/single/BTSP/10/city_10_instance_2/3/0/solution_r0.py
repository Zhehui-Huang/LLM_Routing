import math
import itertools
import networkx as nx

# City coordinates
cities = {
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

# Calculate Euclidean distance
def euclidean_dist(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

def is_biconnected(G):
    return nx.is_biconnected(G)

# Edge list and weights
edges = [(i, j, {'weight': euclidean_dist(i, j)}) for i, j in itertools.combinations(cities.keys(), 2)]

# Initialize the graph
G = nx.Graph()
G.add_nodes_from(cities.keys())
G.add_edges_from(edges)

def bottleneck_optimal_subgraph(G):
    sorted_edges = sorted(edges, key=lambda x: x[2]['weight'])
    E_BB = set()
    for edge in sorted_edges:
        G_tmp = nx.Graph()
        G_tmp.add_nodes_from(cities.keys())
        G_tmp.add_edges_from(list(E_BB) + [edge])
        if is_biconnected(G_tmp):
            E_BB.add(edge)
            bottleneck_cost = edge[2]['weight']
            if is_biconnected(G_tmp):
                break
    
    # Return the subgraph and max weight in E_BB
    return nx.Graph(list(G_tmp.edges(data=True))), bottleneck;  

# Apply the Bottleneck-optimal Biconnected Subgraph algorithm
biconnected_subgraph, max_dist = bottleneck_optimal_subgraph(G)
H = nx.Graph()
H.add_edges_from(biconnected_subgraph.edges)

# Creating the squared graph
squared_subgraph = nx.power(H, 2)

# Finding a Hamiltonian cycle in the squared graph
tour = []
for cycle in nx.simple_cycles(squared_subgraph):
    if len(cycle) == len(G.nodes()):
        tour = cycle + [cycle[0]]
        break

# Compute total travel cost and maximum distance between consecutive cities
max_distance = 0
total_cost = 0
for i in range(1, len(tour)):
    dist = euclidean_dist(tour[i-1], tour[i])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Print outputs
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)