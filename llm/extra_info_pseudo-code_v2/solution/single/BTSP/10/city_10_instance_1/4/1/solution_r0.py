import math
from itertools import combinations
from networkx import Graph, is_biconnected
import networkx as nx

# Define cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a complete graph with distances
G = Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=calculate_distance(cities[i], cities[j]))

# Apply Algorithm BB
# Step 0: Initialization
edges_sorted_by_weight = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Initial empty biconnected subgraph
E_BB = Graph()
E_BB.add_nodes_from(cities.keys())

# Step 1 and 2: Augmentation and stopping condition
for edge in edges_sorted_by_weight:
    E_BB.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    if is_biconnected(E_BB):
        break

# Extract the bottleneck cost
max_edge_cost = max([d['weight'] for u, v, d in E_BB.edges(data=True)])

# Step 2: Tour Identification
# Utilize the biconnected subgraph to find a Hamiltonian circuit
# This step should attempt to find a tour that minimizes the maximum edge in the tour
# For simplicity, we're using NetworkX's approximation algorithm to find this circuit
tour = list(nx.approximation.traveling_salesman_problem(E_BB, cycle=True, method='greedy'))

# Calculate total travel cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0

for i in range(len(tour)):
    if i == len(tour)-1:
        dist = calculate_distance(cities[tour[i]], cities[tour[0]])
    else:
        dist = calculate_distance(cities[tour[i]], cities[tour[i+1]])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")