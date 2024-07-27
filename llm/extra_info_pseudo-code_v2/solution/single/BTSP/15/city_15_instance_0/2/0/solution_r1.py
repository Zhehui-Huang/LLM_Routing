import math
from itertools import combinations
import networkx as nx

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Compute Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize graph G with vertices and weighted edges
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Algorithm BB to create a bottleneck-optimal biconnected subgraph
def algorithm_BB(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    E_BB = nx.Graph()
    E_BB.add_nodes_from(G.nodes())
    for edge in edges_sorted:
        E_BB.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(E_BB) and E_BB.number_of_edges() >= len(cities):
            return E_BB  # Ensure enough edges to keep it biconnected

# Obtaining the bottleneck biconnected subgraph
E_BB = algorithm_BB(G)

# Finding a Hamiltonian cycle in the biconnected subgraph's power graph
def find_hamiltonian_cycle(G):
    # Start with a node and attempt heuristic Hamiltonian path construction
    nodes_list = list(G.nodes())
    path = [nodes_plusLater for nodes_plusLater in nx.approximation.traveling_salesman_problem(G, weight='weight')]
    # Close the cycle back to the starting node
    path.append(path[0])
    return path

# Generate a tour for the squared biconnected subgraph
E_BB_squared = nx.power(E_BB, 2)
tour = find_hamiltonian_cycle(E_BB_squared)

# Calculate the total travel cost and maximum distance between any consecutive cities
total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))
max_distance = max(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))

# Output the tour, total cost, and maximum distance
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")