import math
import networkx as nx

# Define the city coordinates
coords = [
    (30, 56),  # Depot
    (53, 42),
    (1, 95),
    (25, 61),
    (69, 57),
    (6, 58),
    (12, 84),
    (72, 77),
    (98, 95),
    (11, 0),
    (61, 25),
    (52, 0),
    (60, 95),
    (10, 94),
    (96, 73),
    (14, 47),
    (18, 16),
    (4, 43),
    (53, 76),
    (19, 72)
]

# Step 0: Calculate distances between all pairs of cities and define the graph
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Initialize graph
G = nx.Graph()
n = len(coords)

# Add edges with weights
for i in range(n):
    for j in range(i + 1, n):
        distance = euclidean_distance(coords[i], coords[j])
        G.add_edge(i, j, weight=distance)

# Step 1a: Decompose the graph using Algorithm BB
# Start by creating a sorted list of edges by weight
edges_sorted_by_weight = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Create a new graph to find the bottleneck optimal biconnected subgraph
E_BB = []
G_BB = nx.Graph()

# Step 1b: Incrementally add edges
for edge in edges_sorted_by_weight:
    u, v, data = edge
    G_BB.add_edge(u, v, weight=data['weight'])
    if nx.is_biconnected(G_BB):
        break
    E_BB.append((u, v))

# Step 2: Identify the tour using bottleneck reduction with E_BB edges
# Build square of the selected biconnected subgraph
G_BB_squared = nx.Graph()
for u in G_BB.nodes():
    for v in G_BB.nodes():
        if u != v and nx.has_path(G_BB, u, v):
            shortest_path_length = nx.shortest_path_length(G_BB, u, v, weight='weight')
            G_BB_squared.add_edge(u, v, weight=shortest_path_length)

# Find a Hamiltonian circuit using the square graph approximation approach
tour = list(nx.approximation.traveling_salesman_problem(G_BB_squared, cycle=True, method='greedy'))

# Calculate the tour costs and max distance between consecutive cities
total_cost = 0
max_distance = 0
tour_with_depot = tour + [tour[0]]

for i in range(len(tour_with_depot) - 1):
    dist = euclidean_distance(coords[tour_with_depot[i]], coords[tour_with_depot[i + 1]])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Output the results
print(f"Tour: {tour_with_depot}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")