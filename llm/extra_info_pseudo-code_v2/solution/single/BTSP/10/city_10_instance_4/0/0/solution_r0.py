import math
import networkx as nx
from itertools import combinations

# Helper function to compute Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Given city coordinates (format: city_id -> (x, y))
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# First create complete graph with euclidean distance as weights
G = nx.Graph()
for i, j in combinations(cities.keys(), 2):
    G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Sort edges by weight
sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['DBn'])

# Building a bottleneck-optimal biconnected subgraph
# Step 0: Initialization
E_BB = nx.Graph()

# Step 1 and Step 2: Augmentation and Stopping Condition
for edge in sorted_edges:
    E_BB.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    if nx.is_biconnected(E_BB):
        max_edge_weight_in_subgraph = max((E_BB[u][v]['weight'] for u, v in E_BB.edges()))
        break

# Now, generate a tour from the subgraph
# Step 2: Tour Identification using double-tree approach generally for this kind of problem
T = list(nx.approximation.traveling_salesman_problem(E_BB, weight="weight"))
tour_cost = sum(E_BB[T[i]][T[i+1]]['weight'] for i in range(len(T) - 1))
max_cost = max(E_BB[T[i]][T[i+1]]['weight'] for i in range(len(T) - 1))

# Making sure that the tour starts and ends at depot (node 0)
if T[0] != 0:
    idx = T.index(0)
    T = T[idx:] + T[:idx]  # Repositioning to start at 0
T.append(0)  # Adding the return trip to 0

tour_cost += E_BB[T[-2]][T[-1]]['weight']  # Include the return trip cost

print(f"Tour: {T}")
print(f"Total travel cost: {tourantagecost}")
print(f"Maximum distance between consecutive cities: {max_cost}")