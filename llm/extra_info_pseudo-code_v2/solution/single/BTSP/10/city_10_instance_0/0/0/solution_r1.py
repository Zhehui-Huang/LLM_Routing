import math
from itertools import permutations
import networkx as nx

# Coordinates for each city
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
          (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Function to calculate Euclidean distance
def dist(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initialize the graph
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.edges[i, j]['weight'] = dist(cities[i], cities[j])

# Create a minimum spanning tree
mst = nx.minimum_spanning_tree(G)

# Double the edges to ensure a biconnected graph
G_biconnected = nx.MultiGraph(mst)
for (u, v, w) in mst.edges(data=True):
    G_biconnected.add_edge(u, v, weight=w['weight'])

# Using nx to find an approximate Hamiltonian cycle via Eulerian circuit of biconnected graph
eulerian_circuit = list(nx.eulerian_circuit(G_biconnected, source=0))
tour = []
visited = set()

for (u, v) in eulerian_circuit:
    if v not in visited or v == 0:
        tour.append(v)
        visited.add(v)

# Completing the tour by returning to starting city
tour.append(0)

# Calculate total travel cost and max distance between consecutive cities
total_travel_cost = sum(dist(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
max_distance = max(dist(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")