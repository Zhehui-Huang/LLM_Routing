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
    14: (82, 49),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create a graph
G = nx.Graph()
for i in cities.keys():
    for j in cities.keys():
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(i, j))

# Construct a Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# We need to find a minimum-cost perfect matching on the odd-degree vertices
odd_degree_nodes = [node for node in mst.nodes if mst.degree(node) % 2 != 0]
odd_mst_subgraph = mst.subgraph(odd_degree_nodes)
min_cost_matching = nx.algorithms.matching.min_weight_matching(odd_mst_subgraph, maxcardinality=True, weight='weight')

# Add minimum cost matching edges to MST to make it Eulerian
mst.add_edges_from(min_cost_matching)

# Construct an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Make the circuit into a Hamiltonian circuit by skipping visited nodes (shortcutting)
tour = [0]
visited = set()
for u, v in eulerian_circuit:
    if v not in visited:
        tour.append(v)
        visited.add(v)
tour.append(0)  # Return to the starting city

# Calculate the total travel cost of the tour
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Resulting output
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")