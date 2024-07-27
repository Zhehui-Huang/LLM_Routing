import math
from itertools import combinations
import networkx as nx

# Coordinates of each city
coordinates = [
    (50, 42), (41, 1), (18, 46), (40, 98),
    (51, 69), (47, 39), (62, 26), (79, 31),
    (61, 90), (42, 49)
]

# Compute Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Calculate all pairwise city distances and form them as edges
edges = []
for i, j in combinations(range(len(coordinates)), 2):
    dist = euclidean_distance(coordinates[i], coordinates[j])
    edges.append((i, j, dist))
edges.sort(key=lambda x: x[2])  # Sort edges by distance

# Initialize graph
G = nx.Graph()
G.add_nodes_from(range(len(coordinates)))

# Algorithm to find bottleneck optimal biconnected subgraph using networkx
def find_biconnected_subgraph():
    G_bb = nx.Graph()
    G_bb.add_nodes_from(G.nodes())
    for i, j, w in edges:
        G_bb.add_edge(i, j, weight=w)
        if nx.is_biconnected(G_bb):
            # Check if removing any single node keeps the graph connected
            if all(nx.is_connected(G_bb.copy().remove_node(n)) for n in G_bb.nodes()):
                return G_bb, w
        else:
            G_bb.remove_edge(i, j)  # Remove edge if it does not contribute to biconnectivity

# Get the biconnected subgraph and the minimum maximum weight in this subgraph
biconnected_graph, max_edge_weight = find_biconnected_subgraph()

# Using the biconnected graph to find a Hamiltonean cycle
# Placeholder for an approximate tour finding since exact BTSP solving is highly complex
# Assuming the presence of a potential heuristic or backup simplification
def find_approximate_tour_bbot():
    cycle = list(nx.approximation.traveling_salesman_problem(biconnected_graph, cycle=True, weight='weight'))
    return cycle

# Function to calculate total travel cost and maximum distance between consecutive cities
def calculate_tour_metrics(tour):
    max_distance = 0
    total_cost = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Find tour and calculate metrics
approx_tour = find_approximate_tour_bbot()
total_cost, max_distance = calculate_tour_metrics(approx_tour + [approx_tour[0]])

# Append start to end to close the cycle
tour_result = approx_tour + [approx_tour[0]]

# Results
print(f"Tour: {tour_result}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")