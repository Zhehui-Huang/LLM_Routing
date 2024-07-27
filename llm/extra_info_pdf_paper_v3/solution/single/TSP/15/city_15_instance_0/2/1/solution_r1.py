import math
import networkx as nx

# Define city coordinates
cities = {
    0: (9, 93), 
    1: (8, 51), 
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Create graph
G = nx.Graph()

# Add edges between all pairs of cities with weights as their Euclidean distances
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(i, j))

# Use a heuristic from NetworkX to approximate the TSP solution
cycle = list(nx.approximation.traveling_salesman_problem(G, weight='weight', cycle=True))

# Calculate the total travel cost of the tour
total_cost = sum(euclidean_distance(cycle[i], cycle[i+1]) for i in range(len(cycle)-1))

# Output the result
print("Tour:", cycle)
print("Total travel cost:", total_cost)