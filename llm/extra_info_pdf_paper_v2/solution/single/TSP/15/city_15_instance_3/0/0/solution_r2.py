import numpy as np
import networkx as nx

def calculate_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def construct_distance_matrix(cities):
    """ Construct a distance matrix for the given dictionary of cities """
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = calculate_distance(cities[i], cities[j])
    return dist_matrix

# Coordinates of the cities from the problem statement
cities_coords = [
    (16, 90),  # City 0 (Depot)
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Construct the distance matrix
distance_matrix = construct_distance_matrix(cities_coords)

# Using NetworkX to construct a graph from the distance matrix
G = nx.complete_graph(len(cities_coords))
for i in range(len(cities_coords)):
    for j in range(i + 1, len(cities_coords)):
        G[i][j]['weight'] = distance_matrix[i][j]

# Compute the TSP tour using a heuristic method (greedy approach) in NetworkX
tsp_tour = nx.approximation.traveling_salesman_problem(G, cycle=True, method='greedy')

# Calculate the total cost of the complete tour
total_cost = sum(distance_matrix[tsp_tour[i]][tsp_tour[(i + 1) % len(tsp_tour)]] for i in range(len(tsp_tour)))

# Output the results
tour_output = [tsp_tour[idx] for idx in range(len(tsp_tour))]
print(f"Tour: {tour_output}")
print(f"Total travel cost: {total_cost:.2f}")