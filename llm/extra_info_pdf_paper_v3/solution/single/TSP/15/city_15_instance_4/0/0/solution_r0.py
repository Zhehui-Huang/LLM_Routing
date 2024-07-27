import math
import networkx as nx
from networkx.algorithms.approximation import traveling_salesman_problem

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
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.edges[i, j]['weight'] = euclidean_distance(cities[i], cities[j])

# Using Christofides algorithm to approximate a solution to the TSP
tsp_tour = traveling_salesman_problem(G, cycle=True, method='christofides')

# Calculating the total cost of the tour
total_cost = sum(G.edges[tsp_tour[i], tsp_tour[i+1]]['weight'] for i in range(len(tsp_tour)-1))

# Print the tour and the total cost
tour = [tsp_tour[i] for i in range(len(tsp_tour))]
print("Tour:", tour)
print("Total travel cost:", total_cost)