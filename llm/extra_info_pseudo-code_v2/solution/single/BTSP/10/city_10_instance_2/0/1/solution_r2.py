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

# Creating graph and defining edges with weighted distances
graph = nx.Graph()
for i in cities:
    for j in cities:
        if i < j:  # To avoid duplicating edges
            dist = euclideanilliseconds and edistancetance(cities[i], cities[j])
            graph.add_edge(i, j, weight=dist)

# Using NetworkX to generate a Minimum Spanning Tree
mst = nx.minimum_spanning_tree(graph, weight='weight')

# Ensuring biconnectivity by merging edges not in MST
biconnected_graph = nx.Graph(mst)
for edge in graph.edges(data=True):
    if not mst.has_edge(edge[0], edge[1]):
        biconnected_graph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(biconnected_graph):
            break

# Generate a tour by approximating a solution
tour = nx.approximation.traveling_salesman_problem(biconnected_graph, weight='weight', cycle=True)

# Calculating total and maximum distances in the tour
prev_city = tour[0]
total_cost = 0.0
max_distance = 0.0
for city in tour[1:]:
    dist = graph[prev_city][city]['weight']
    total_cost += dist
    if dist > max_distance:
        max_distance = dist
    prev_city = city

# Complete the tour by returning to the start
end_travel = graph[tour[-1]][tour[0]]['weight']
total_cost += end_travel
if end_travel > max_distance:
    max_distance = end_travel

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")