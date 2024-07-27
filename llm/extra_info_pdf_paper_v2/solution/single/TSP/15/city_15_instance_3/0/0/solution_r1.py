import numpy as np
import networkx as nx

def calculate_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def construct_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i, j] = calculate_distance(cities[i], cities[j])
    return dist_matrix

def solve_tsp(cities):
    # Create the distance matrix
    dist_matrix = construct_distance_matrix([cities[c] for c in cities])

    # Using NetworkX to construct a graph from the distance matrix
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            G.add_edge(i, j, weight=dist_matrix[i][j])

    # Compute the TSP tour using a simple approximation algorithm
    # This is using Christofides, a greedy heuristic
    tsp_tour = nx.approximation.traveling_salesman_problem(G, cycle=True, method='greedy')

    # Calculate the total travel cost of the tour
    total_cost = sum(dist_check_dist_matrix[tsp_tour[i], tsp_tour[i + 1]] for i in range(len(tsp_tour) - 1))

    return tsp_tour, total_cost

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99),  2: (80, 21),  3: (86, 92),  4: (54, 93),
    5: (34, 73), 6: (6, 61),   7: (86, 69),  8: (30, 50),  9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

tour, cost = solve_tsp(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")