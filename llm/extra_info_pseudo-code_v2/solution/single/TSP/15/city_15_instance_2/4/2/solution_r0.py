import numpy as np
import networkx as nx
import tsplib95
from opt_einsum import contract

# City coordinates
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

# Create a complete graph
G = nx.complete_graph(len(coordinates))

# Assign the Euclidean distance as edge attribute for each edge in the graph
for u, v in G.edges():
    G[u][v]['weight'] = np.linalg.norm(np.array(coordinates[u]) - np.array(coordinates[v]))

# Use NetworkX to find an approximate solution to the TSP problem
cycle = nx.approximation.traveling_salesman_problem(G, weight='weight')

# Calculate total travel cost of the tour
cycle.append(cycle[0])  # append the start city to complete the cycle for total cost calculation
tour_cost = sum(G[cycle[i]][cycle[i+1]]['weight'] for i in range(len(cycle)-1))

# Output results
print("Tour:", cycle)
print("Total travel cost:", tour_cost)