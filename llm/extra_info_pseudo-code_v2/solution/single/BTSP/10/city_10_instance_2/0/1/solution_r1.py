import math
import networkx as nx

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Initialize cities and their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Creating graph and adding edges with weights
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            dist = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)

# Step 0: NetworkX complete graph and sort edges by weight for minimal bottleneck span
edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Using NetworkX to create a Minimum Spanning Tree as a subgraph base
mst = nx.minimum_spanning_tree(G, weight='weight')
H = nx.Graph()
H.add_nodes_from(G.nodes(data=True))

# Step 1: Augmentation to achieve biconnection
H.add_edges_from(mst.edges(data=True))
while not nx.is_biconnected(H):
    for edge in edges_sorted:
        if not H.has_edge(edge[0], edge[1]):
            H.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
            if nx.is_biconnected(H):
                break

# Step 2: Generating approximate TSP tour using the double tree algorithm.
# Translate H to H^2 if needed
T = list(nx.approximation.traveling_salesman_problem(H, cycle=True, weight='weight', method='christofides'))

# Calculate Tour specifications
total_cost = 0.0
max_edge_weight_in_tour = 0.0
prev_city = T[0]

for city in T[1:]:
    dist = G[prev_city][city]['weight']
    total_cost += dist
    if dist > max_edge_weight_in_tour:
        max_edge_weight_in_tour = dist
    prev_city = city

# Close the tour
last_leg_to_end = G[T[-1]][T[0]]['weight']
total_cost += last_leg_to_end
if last_leg_to_end > max_edge_weight_in_tour:
    max_edge_weight_in_tour = last_leg_to_end

# Output
print(f"Tour: {T}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_edge_pain:.2f}")