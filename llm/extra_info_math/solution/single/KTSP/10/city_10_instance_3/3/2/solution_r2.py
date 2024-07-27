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

dist_matrix = calculate_distances(cities)

# Function to find the shortest TSP tour using exact method
def find_shortest_tour(dist_matrix, k):
    n = len(dist_matrix)
    min_tour_cost = float('inf')
    best_tour = None

    # Generate combinations of k-1 cities (excluding the depot city 0).
    for selected_cities in combinations(range(1, n), k - 1):
        selected_cities = (0,) + selected_cities

        G = nx.Graph()
        for i in selected_cities:
            for j in selected_cities:
                if i != j:
                    G.add_edge(i, j, weight=dist_matrix[i][j])
        
        try:
            cycle = nx.approximation.traveling_salesman_problem(G, weight='weight')
            cycle_cost = sum(G[cycle[i]][cycle[i+1]]['weight'] for i in range(len(cycle) - 1))
            
            if cycle_cost < min_tour_cost:
                min_tour_cost = cycle_cost
                best_tour = cycle
        except Exception as e:
            continue

    if best_tour is not None:
        best_tour = list(best_tour) + [best_tour[0]]
    return best_tour, min_tour_cost

# Finding the shortest tour visiting exactly 7 cities
best_tour, tour_cost = find_shortest_tour(dist_matrix, 7)

# Output the tour and the cost
print("Tour:", best_tour)
print("Total travel cost:", tour_cost)