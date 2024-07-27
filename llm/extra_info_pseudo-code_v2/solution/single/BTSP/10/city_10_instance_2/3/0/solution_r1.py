import math
import networkx as nx

# Coordinates of the cities
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

# Calculate Euclidean distance between cities
def euclidean_dist(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Initialize the graph
G = nx.Graph()
for i in cities.keys():
    for j in cities.keys():
        if i != j:
            G.add_edge(i, j, weight=euclidean_dist(i, j))

# Generate a Minimum Spanning Tree
MST = nx.minimum_spanning_tree(G)

# Doubled edges MST (create an Eulerian graph)
edge_list = list(MST.edges(data=False))
doubled_edge_list = edge_list + [(j, i) for i, j in edge_list]

# Initialize the Eulerian graph with doubled edges
Eulerian_G = nx.Graph()
Eulerian_G.add_edges_from(doubled_edge_list)

# Finding an Eulerian tour
eulerian_tour = list(nx.eulerian_circuit(Eulerian_G, source=0))

# Creating a list of visited nodes to create a valid tour, avoiding repeated nodes
visited = set()
tour = []
for u, v in eulerian_tour:
    if u not in visited:
        tour.append(u)
        visited.add(u)
    if v not in visited:
        tour.append(v)
        visited.add(v)
tour.append(0)  # Complete the cycle back to the starting node

# Calculate the total travel cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    dist = euclidean_dist(tour[i-1], tour[i])
    total_cost += dist
    max_distance = max(max_distance, dist)

# Print outputs
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive severities:", max_distance)