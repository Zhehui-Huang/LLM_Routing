import math
from itertools import combinations
import networkx as nx

# Define cities
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# Create the complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(cities[i], cities[j]))

# Function to find minimum cost perfect matching in the odd degrees vertices
def min_cost_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    min_cost_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight="weight")
    return min_cost_matching

# Christofides Algorithm
def christofides(G):
    # 1. Create minimum spanning tree
    T = nx.minimum_spanning_tree(G, weight="weight")
    
    # 2. Find vertices with odd degree
    odd_degree_vertices = [v for v in T.nodes if T.degree(v) % 2 == 1]
    
    # 3. Find minimum cost perfect matching on the odd degree subgraph
    matching = min_cost_perfect_matching(G, odd_degree_vertices)
    T.add_edges_from(matching)
    
    # 4. Create an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(T))
    
    # 5. Convert Eulerian circuit to Hamiltonian circuit (shortcutting repeated cities)
    path = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # return to start to form a cycle
    
    return path

# Get the tour using Christofides Algorithm
tour = christofides(G)

# Calculate the total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:]))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")