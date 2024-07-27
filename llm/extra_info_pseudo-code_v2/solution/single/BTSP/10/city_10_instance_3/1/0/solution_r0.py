import math
import networkx as nx
from itertools import combinations

# City Coordinates
cities = [
    (84, 67),  # Depot City 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76),
]

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Construct the complete graph with edge weights
n = len(cities)
G = nx.Graph()
for i, j in combinations(range(n), 2):
    G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Bottleneck-optimal Biconnected Subgraph construction (Algorithm BB)
sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
E_BB = []
G_BB = nx.Graph()
G_BB.add_nodes_from(G.nodes())

for edge in sorted_edges:
    G_BB.add_edge(*edge[:2])
    if nx.is_biconnected(G_BB):
        break
    E_BB.append(edge)

# Determine the edge with the maximum weight in the biconnected subgraph
max_edge_weight = max([edge[2]['weight'] for edge in E_BB])

# Tour Identification
# We can utilize `minimum_weighted_hamiltonian_path` function from NetworkX to identify an approximate optimal tour
# Since it's not directly available, we can use approximation method. NetworkX has traveling_salesman_problem method that can be modified.
from networkx.algorithms.approximation import traveling_salesman_problem

tour = traveling_salesman_problem(G_BB, cycle=True)

# Compute the tour costs
total_cost = 0
max_distance = 0
for i in range(len(tour)):
    j = (i + 1) % len(tour)
    dist = euclidean_distance(cities[tour[i]], cities[tour[j]])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Return the solution
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")