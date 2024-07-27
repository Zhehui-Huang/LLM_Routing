import numpy as np
from itertools import combinations
from scipy.spatial.distance import euclidean
import networkx as nx

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distances
def calculate_distances(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

distances = calculate_distances(cities)

# Function to find shortest possible TSP tour from given complete graph
def find_shortest_tour(dist_matrix, k):
    # defines number of cities
    n = len(dist_matrix)
    
    min_tour_cost = float('inf')
    best_tour = None
    
    # All combinations of k-1 cities (excluding the depot city, which is index 0)
    for selected_cities in combinations(range(1, n), k-1):
        # Include depot city index 0 explicitly
        tour_cities = [0] + list(selected_cyaties)
        
        # Creating subgraph cost matrix
        subgraph_dist_matrix = dist_matrix[np.ix_(tour_cities, tour_cities)]

        # Solving TSP on the subgraph using held-karp algorithm
        G = nx.complete_graph(len(tour_cities))
        for i in range(len(G.nodes)):
            for j in range(len(G.nodes)):
                G[i][j]['weight'] = subgraph_dist_matrix[i][j]

        cycle = nx.approximation.traveling_salesman_problem(G, cycle=True, weight='weight')
        cycle_cost = sum(G[cycle[i]][cycle[i+1]]['weight'] for i in range(len(cycle)-1))

        # Store the best tour and its cost found
        if cycle_cost < min_tour_cost:
            min_tour_cost = cycle_cost
            best_tour = cycle

    # Return tour with original city indices
    if best_tour is not None:
        best_tour = [tour_cities[i] for i in best_tour] + [0]
    return best_tour, min_tour_cost

# Compute the TSP for 7 cities including the depot (0)
best_tour, min_tour_cost = find_shortest_tour(distances, 7)

print("Tour:", best_tour)
print("Total travel cost:", min_tour_cost)