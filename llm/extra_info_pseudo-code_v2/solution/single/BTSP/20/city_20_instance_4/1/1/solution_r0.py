import math
import networkx as nx
from itertools import permutations

# Define the cities coordinates
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

def bottleneck_tsp(graph):
    # Sort edges by weight
    edges_sorted = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    
    # Step 1 - Algorithm BB: Find bottleneck-optimal biconnected subgraph
    BB = nx.Graph()
    BB.add_nodes_from(graph.nodes())
    for u, v, d in edges_sorted:
        BB.add_edge(u, v, weight=d['weight'])
        if nx.is_biconnected(BB):
            break
            
    # Step 2: Identify the Approximate Optimal Tour
    # Tracing a hamiltonian path in the biconnected subgraph
    # We use a simple heuristic of trying to find the shortest path in the square of the graph
    biconnected_edges = [(u, v) for u, v in BB.edges()]
    GG = nx.Graph()
    GG.add_nodes_from(BB.nodes())
    for u, v in permutations(BB.nodes(), 2):
        path_length = nx.dijkstra_path_length(BB, u, v)
        GG.add_edge(u, v, weight=path_length)
    
    cycle = nx.approximation.traveling_salesman_problem(GG, cycle=True)
    # Ensure starting and ending at the depot city 0
    cycle = [0] + [c for c in cycle if c != 0] + [0]
    
    # Calculate the max distance and total cost
    max_distance = 0
    total_cost = 0
    for i in range(len(cycle)-1):
        dist = graph[cycle[i]][cycle[i+1]]['weight']
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    return cycle, total_cost, max_image

# Find the tour, total cost, and maximum distance
tour, total_cost, max_distance = bottleneck_tsp(G)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")