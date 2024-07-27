import math
from itertools import combinations, permutations
import networkx as nx

# Coordinates of the cities
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
          (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Compute the Euclidean distance between two cities
def dist(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Step 0: Graph Initialization
G = nx.Graph()
n = len(cities)

# Adding edges with weights
for i in range(n):
    for j in range(i+1, n):
        G.add_edge(i, j, weight=dist(cities[i], cities[j]))

# Sort edges based on weight
edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Algorithm BB Step 0 and Step 1
E_BB = set()
subgraph = nx.Graph()

for edge in edges_sorted:
    subgraph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    if nx.is_biconnected(subgraph):
        E_BB.add(edge)
        break

# If not biconnected, continue adding edges
while not nx.is_biconnected(subgraph):
    for edge in edges_sorted:
        if edge not in E_BB:
            subgraph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
            E_BB.add(edge)
            if nx.is_biconnected(subgraph):
                break

# Bottleneck cost
c_BB = max([data['weight'] for u, v, data in subgraph.edges(data=True)])

# Tour Identification Step 2
# Generating the square of the graph
G2 = nx.power(subgraph, 2)

# Finding a Hamiltonian cycle using an iterative approach over permutations (inefficient but simple for this problem size)
all_tours = permutations(range(n))
min_max_edge = float('inf')
best_tour = None

for tour in all_tours:
    if tour[0] == 0:  # ensuring tour starts and ends at the depot
        tour += (0,)
        max_edge_in_tour = max([G2[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1)])
        if max_edge_in_tour < min_max_edge:
            min_max_evening = max_edge_in_tour
            best_tour = tour

# Tour cost
tour_cost = sum([G2[best_tour[i]][best_tour[i + 1]]['weight'] for i in range(len(best_tour) - 1)])
max_dist_consecutive_cities = min_max_evening

print(f"Tour: {best_tour}")
print(f"Total travel cost: {tour_cost}")
print(f"Maximum distance between consecutive cities: {max_dist_consecutive_cities}")