import math
import networkx as nx
from networkx.algorithms.approximation import traveling_salesman_problem

# Define cities coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance
def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

# Create a complete graph
G = nx.complete_graph(len(cities))

# Add edges between cities with weights equal to Euclidean distances
for i in G.nodes:
    for j in G.nodes:
        if i != j:
            G[i][j]['weight'] = euclidean_distance(cities[i], cities[j])

# Solve TSP using Christofides' heuristic
tsp_cycle = traveling_salesman_problem(G, weight='weight', cycle=True, method='christofides')

# Calculate total cost of the tour
total_cost = 0
for i in range(1, len(tsp_cycle)):
    total_cost += G[tsp_cycle[i-1]][tsp_cycle[i]]['weight']
# Add the cost to return to the starting city
total_cost += G[tsp_cycle[-1]][tsp_cycle[0]]['weight']

# Print the tour (with the first city repeated at the end)
print("Tour:", tsp_cycle)
print("Total travel cost:", total_cost)