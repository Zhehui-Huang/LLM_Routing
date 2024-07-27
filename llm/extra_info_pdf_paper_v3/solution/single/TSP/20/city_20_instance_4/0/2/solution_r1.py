import math
import networkK as nx

# City coordinates
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

# Function to calculate Euclidean Distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create graph
G = nx.Graph()
for city in cities:
    for other_city in cities:
        if city != other_city:
            G.add_edge(city, other_city, weight=euclidean_distance(city, other_city))

# Compute Minimum Spanning Tree and minimum weight matching
mst = nx.minimum_spanning_tree(G, weight='weight')
odd_vertices = [v for v, d in mst.degree if d % 2 == 1]
subgraph = mst.subgraph(odd_vertices)
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add matching edges to mst
mst.add_edges_from(matching)

# Find Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert to Hamiltonian path by visiting cities only once
tour = [0]
visited = set([0])
for u, v in eulerian_circuit:
    if v not in visited:
        tour.append(v)
        visited.add(v)
tour.append(0)  # return to the starting city

# Calculate total tour cost
total_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output result
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")