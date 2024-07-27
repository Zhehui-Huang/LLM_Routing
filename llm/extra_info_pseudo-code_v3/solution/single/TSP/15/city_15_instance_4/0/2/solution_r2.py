import numpy as np
import networkx as nx
from networkx.algorithms.approximation import christofides

# Coordinates of cities, with the depot city as city 0
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Create a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            # Euclidean distance as edge weight
            dist = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))
            G.add_edge(i, j, weight=dist)

# Using Christofides' algorithm to find a near-optimal solution to the TSP
tour = christofides(G, weight='weight')

# Compute the total cost of the tour
total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))
total_cost += G[tour[-1]][tour[0]]['weight']  # Adding the cost to return to the depot

# Append the return to the depot to complete the circuit
tour.append(tour[0])

# Output the findings
print("Tour:", tour)
print("Total travel cost:", total_cost)