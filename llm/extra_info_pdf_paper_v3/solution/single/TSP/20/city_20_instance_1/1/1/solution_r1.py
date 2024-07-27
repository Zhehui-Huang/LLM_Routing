import math
import networkx as nx

# Define cities with their coordinates
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

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create a complete graph of the cities
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(i, j))

# Compute the Minimum Spanning Tree (MST) of the graph
T = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices of odd degree in the MST
odd_degree_nodes = [v for v, degree in T.degree() if degree % 2 == 1]

# Function to find minimum cost perfect matching on subgraph of odd degree vertices
def min_cost_perfect_matching(G, nodes):
    subgraph = G.subgraph(nodes)
    min_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)
    return min_matching

# Get the minimum cost perfect matching for the odd_degree_nodes
matching = min_cost_perfect_matching(G, odd_degree_nodes)

# Add matching edges to the MST
T.add_edges_from(matching)

# Form an Eulerian circuit from the MST with added perfect matching edges
eulerian_circuit = list(nx.eulerian_circuit(T, source=0))

# Convert the Eulerian circuit to a Hamiltonian path (remove repeated vertices)
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v) 

# Ensure the tour returns to the starting point
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Compute the total cost of the tour
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")