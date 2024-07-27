import math
from itertools import combinations
import networkx as nx

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26),
    11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25),
    16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Initializations
num_vertices = len(cities)
edges = [(i, j, {'weight': euclidean_distance(cities[i], cities[j])}) for i in range(num_vertices) for j in range(i + 1, num_vertices)]
G = nx.Graph()
G.add_nodes_from(range(num_vertices))
G.add_edges_from(edges)

# Algorithm BB to create Bottleneck Biconnected Subgraph
def algorithm_bb(graph):
    edges_sorted_by_weight = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    bb_subgraph = nx.Graph()
    bb_subgraph.add_nodes_from(graph.nodes())
    
    for u, v, data in edges_sorted_by_weight:
        bb_subgraph.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(bb_subgraph):
            break

    return bb_subgraph
  
# Apply Algorithm BB
bb_subgraph = algorithm_bb(G)

# Finding a Hamiltonian path in the square of the Bottleneck Biconnected Subgraph
bb_squared = nx.power(bb_subgraph, 2)
cycle = nx.approximation.traveling_salesman_problem(bb_squared, weight='weight', cycle=True)

# Calculate total cost and maximum consecutive distance
total_cost = 0
max_distance = 0
cycle.append(cycle[0])  # To return to the start for a full cycle

for i in range(len(cycle)-1):
    distance = euclidean_distance(cities[cycle[i]], cities[cycle[i+1]])
    total_cost += distance
    if distance > max_distance:
        max_distance = distance

cycle.pop()  # Remove the appended start node after calculations

# Output the results
print(f"Tour: {cycle}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")