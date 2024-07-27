import math
import networkx as nx

# City coordinates
coords = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a complete graph with edge weights computed from distances
G = nx.Graph()
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        G.add_edge(i, j, weight=distance(coords[i], coords[j]))

# Generate Minimum Spanning Tree (MST) initially
T = nx.minimum_spanning_tree(G)

# Make graph biconnected by adding edges with smallest weight until it is biconnected
while not nx.is_biconnected(T):
    for edge in sorted(G.edges(data=True), key=lambda x: x[2]['weight']):
        if not T.has_edge(edge[0], edge[1]):
            T.add_edge(edge[0], edge[1], **edge[2])
            if nx.is_biconnected(T):
                break

# Construct potential Hamiltonian cycle
# Building the approximate Hamiltonian cycle (tour) based on MST + additional edges
tour = list(nx.approximation.traveling_salesman_problem(T, cycle=True, weight='weight'))

# Calculate maximum distance and total travel cost in the tour
total_cost = sum(T.edges[tour[i], tour[i+1]]['weight'] for i in range(len(tour) - 1))
max_distance = max(T.edges[tour[i], tour[i+1]]['weight'] for i in range(len(tour) - 1))

# Outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")