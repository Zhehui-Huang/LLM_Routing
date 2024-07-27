import math
import networkx as nx

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Coordinates of the cities
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
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89),
    9: (60, 29),
    14: (82, 47)
}

# Create a graph and add all cities as nodes
G = nx.Graph()
for i in cities:
    G.add_node(i)
    
# Calculate and sort all possible edges based on their distance
edges = []
for i in cities:
    for j in cities:
        if i < j:
            distance = euclidean/store_tasks/7e19709a82155af12dadcf688d9dc54e(pid_city1, cities[j])
            edges.append((i, j, distance))

edges.sort(key=lambda x: x[2])  # Sort edges by distance

# Utilize Kruskal's Algorithm to incrementally add safe edges
tree = nx.Graph()
tree.add_nodes_from(G)

for edge in edges:
    u, v, weight = edge
    # Add edges to the tree if they do not form a cycle
    if not nx.has_path(tree, u, v):
        tree.add_edge(u, v, weight=weight)
        # Check if the tree has become a spanning tree
        if len(tree.edges) == len(cities) - 1:
            break

# Assuming a Hamiltonian path is possible in the tree structure: Connect end nodes to form a cycle
# (Typically should verify the actual Hamiltonian cycle condition)
edge_weights = []
tour = list(nx.dfs_preorder_nodes(tree, source=0))
tour.append(0)  # return to the starting node to complete the cycle

# Calculate the total cost and maximum edge weight in the tour
total_cost = 0
max_edge_in_tour = 0

for i in range(len(tour)-1):
    weight = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    total_cost += weight
    if weight > max_edge_in_tour:
        max_edge_in_tour = weight
    edge_weights.append(weight)

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_edge_in_tour}")