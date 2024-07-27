import math
import networkx as nx

# Define the coordinates for each city
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

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create a Graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(i, j))

# Generate the Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G, weight='weight')

# Finding all vertices of odd degree in the MST
odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]

# Minimum Cost Perfect Matching
subgraph = mst.subgraph(odd_degree_nodes)
match = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Adding the matched edges to the MST
mst.add_edges_from(match)

# Constructing the Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Creating the Hamiltonian Circuit (tour)
tour = [0]
visited = set([0])
for u, v in eulerian_circuit:
    if v not in visited:
        tour.append(v)
        visited.add(v)
tour.append(0)

# Calculate the total distance
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")