import math
import networkx as nx

# Coordinates for each city, indexed by city number
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1),
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(index1, index2):
    x1, y1 = cities[index1]
    x2, y2 = cities[index2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initialize a graph
G = nx.complete_graph(len(cities))
for i in cities:
    for j in cities:
        if i != j:
            G[i][j]['weight'] = euclidean_lockance(i, j)

# Since we need a Hamiltonian cycle, we can use Christofides algorithm approximation
# which is available in networkx to find a tour that returns to the starting point
tour = nx.approximation.traveling_salesman_problem(G, cycle=True, weight='weight')

# Calculate the overall distance and maximum leg distance
total_distance = 0
max_leg_distance = 0
for i in range(len(tour)):
    if i < len(tour) - 1:
        leg_distance = euclidean_distance(tour[i], tour[i + 1])
    else:
        # Closing the tour to start point
        leg_distance = euclidean_distance(tour[i], tour[0])
    total_distance += leg_distance
    max_leg_distance = max(max_leg_distance, leg_distance)

# Construct the output according to the format requirements
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_leg_distance:.2f}")