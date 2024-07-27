import math
import networkx as nx

# Given city coordinates
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

# Calculate the Euclidean distance between two cities
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Creating a complete graph with weighted edges between cities
def create_complete_graph(cities):
    G = nx.Graph()
    for i in cities:
        for j in cities:
            if i != j:
                G.add_edge(i, j, weight=distance(cities[i], cities[j]))
    return G

# Function to check if the graph is biconnected
def is_biconnected(G):
    return nx.is_biconnected(G)

def algorithm_bb(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    G_bb = nx.Graph()
    G_bb.add_nodes_from(G.nodes())
    for edge in edges_sorted:
        G_bb.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if is_biconnected(G_bb):
            break
    return G_bb

# Create the initial complete graph
G = create_complete_graph(cities)

# Apply Algorithm BB
G_bb = algorithm_bb(G)

# Hamiltonian Cycle in G_bb²
tour = list(nx.approximation.traveling_salesman_problem(G_bb, cycle=True))

# Compute costs
total_cost = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))
max_distance = max(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)