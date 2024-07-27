import math
import networkx as nx

# Locations of the cities, including the depot
locations = [
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
    (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
]

# Euclidean distance calculator
def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

# Create the complete graph
G = nx.complete_graph(len(locations))
for u, v in G.edges():
    G[u][v]['weight'] = euclidean_distance(locations[u], locations[v])

# Sort edges by weight
edges_sorted = sorted(G.edges(data=True), key=lambda e: e[2]['weight'])

# Creating the graph with the BB algorithm
subgraph = nx.Graph()
for edge in edges_sorted:
    subgraph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    if nx.is_biconnected(subgraph) and len(subgraph.edges()) >= len(locations):
        break

# Check if the subgraph obtained is not enough to form a Hamiltonian circuit, continue adding edges
if not nx.is_biconnected(subgraph) or len(subgraph.edges()) < len(locations):
    # Additional edges are added to ensure we have a biconnected graph with the required number of edges
    for edge in edges_sorted:
        subgraph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnented(subgraph) and len(subgraph.edges()) >= len(locations):
            break

# Powering the subgraph to ensure it's easier to find a Hamiltonian cycle
subgraph_square = nx.power(subgraph, 2)

# Create the TSP tour
tour = nx.approximation.traveling_salesman_problem(subgraph_square, cycle=True, weight='weight')

# Recreate the list to start with depot city 0
tour = tour[tour.index(0):] + tour[:tour.index(0)] + [0]

# Calculate the necessary metrics
max_distance = max(subgraph_square[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))
total_cost = sum(subgraph_square[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)