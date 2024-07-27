import numpy as np
import networkx as nx

# City coordinates
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

# Create a complete graph
G = nx.Graph()

# Add edges between all pairs of cities with Euclidean distance as weights
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        dist = np.linalg.norm(np.array(coordinates[i]) - np.array(coordinates[j]))
        G.add_edge(i, j, weight=dist)

# Find the shortest TSP tour using an approximation method
tsp_tour = list(nx.approximation.traveling_salesman_problem(G, weight='weight'))

# Since the starting point needs to be the depot city (index 0) and end at depot city, rearrange if necessary
if tsp_tour[0] != 0:
    # Rotate the list so that it starts with city 0
    zero_index = tsp_tour.index(0)
    tsp_tour = tsp_tour[zero_index:] + tsp_tour[:zero_index]

# Ensure the tour starts and ends at the depot city 0 by explicitly stating it
if tsp_tour[-1] != 0:
    tsp_tour.append(0)

# Calculate the total travel cost of the tour
total_cost = sum(G[tsp_tour[i]][tsp_tour[i + 1]]['weight'] for i in range(len(tsp_tour) - 1))

# Print output
print("Tour:", tsp_tour)
print("Total travel cost: {:.2f}".format(total_cost))