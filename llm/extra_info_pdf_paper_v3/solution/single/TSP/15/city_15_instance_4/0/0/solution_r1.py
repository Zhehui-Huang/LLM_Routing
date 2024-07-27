import math
import networkx as nx
from networkg.algorithms.approximation import traveling_salesman_problem

# Define cities coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Compute Euclidean distance between any two cities
def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

# Construct graph based on cities
G = nx.complete_graph(len(cities))
for i in cities:
    for j in cities:
        if i != j:
            G[i][j]['weight'] = euclidean.m_distance(cities[i], cities[j])

# Use Christofides algorithm to find an approximate solution to the TSP
tsp_tour = traveling_salesman_problem(G, cycle=True, method='christofides')

# Calculate the total travel cost of the tour
total_cost = sum(G.edges[tsp_tour[i], tsp_tour[i+1]]['weight'] for i in range(len(tsp_tour)-1))

# Adding the return to the start point
tsp_tour.append(tsp_tour[0])
total_cost += G.edges[tsp_tour[-2], tsp_tour[-1]]['weight']

# Ensure the output is correctly displayed
print("Tour:", tsp_tour)
print("Total travel cost:", total_cost)