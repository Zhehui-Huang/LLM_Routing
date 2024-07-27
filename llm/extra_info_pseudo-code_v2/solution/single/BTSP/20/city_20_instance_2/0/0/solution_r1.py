import math
import networkx as nx

# Helper function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Cities coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Generate a complete graph with edge weights as Euclidean distances
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G[i][j]['weight'] = euclidean_distance(cities[i], cities[j])
        G[j][i]['weight'] = G[i][j]['weight']  # Ensure the graph is undirected

# Sort edges by weight
sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Bottleneck-optimal Biconnected Subgraph Construction using Kruskal's approach
subgraph = nx.Graph()
subgraph.add_nodes_from(G.nodes())
for edge in sorted_edges:
    subgraph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    if nx.is_biconnected(subgraph):
        break

# Construct Hamiltonian cycle from the biconnected subgraph
# Since finding a Hamiltonian cycle in a general graph is NP-hard,
# we will find a minimum weight Hamiltonian cycle approximation using nx.approximation.traveling_salesman
# Rather than using the square graph of the biconnected subgraph, since that is non-trivial to compute efficiently
tour = nx.approximation.traveling_salesman_problem(subgraph, cycle=True, weight='weight')

# Calculate total travel cost and max distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(len(tour) - 1):
    distance = G[tour[i]][tour[i + 1]]['weight']
    total_cost += distance
    if distance > max_distance:
        max_distance = distance
distance = G[tour[-1]][tour[0]]['weight']  # Closing the loop back to the start
total_cost += distance
if distance > max_distance:
    max_distance = distance

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")