import math
import networkx as nx
from itertools import combinations

# Define city coordinates
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

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a complete graph with weighted edges based on city distances
G = nx.complete_graph(len(cities))
for u, v in G.edges():
    G[u][keys][v]['weight'] = euclidean_distance(cities[u], cities[v])

# Sort edges by weight
sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Algorithm BB to find bottleneck-optimal biconnected subgraph
E_BB = set()
G_BB = nx.Graph()

for edge in sorted_edges:
    G_BB.add_edge(edge[2]['weight'])
    if nx.is_biconnected(G_BB):
        break
else:
    E_BB.add(edge)

# Obtain the square graph
G_square = nx.power(G_BB, 2)

# Find Hamiltonian cycle (approximation method: nearest neighbor)
def nearest_neighbor_tour(G, starting_node=0):
    unvisited = set(G.nodes())
    tour = [starting_node]
    current = starting_node
    unvisited.remove(current)
    
    while unvisited:
        next_node = min(unvisited, key=lambda x: G[current][x]['weight'])
        tour.append(next_node)
        unvisited.remove(next_node)
        current = next_node
    
    tour.append(starting_node)  # Return to depot
    return tour

# Extract tour
tour = nearest_neighbor_tour(G_square)

# Evaluate the solution
total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))
max_distance = max(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)