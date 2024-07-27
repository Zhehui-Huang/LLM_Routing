import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix

# List all city coordinates
cities = [
    (8, 11), # Depot: city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97),
    (5, 59), (62, 88), (13, 43), (61, 25), (61, 28), (60, 63), (93, 15)
]

# Calculate the distance matrix
distance_matrix = distance.cdist(cities, cities, 'euclidean')

# Heuristic TSP function
def heuristic_tsp(distances):
    from scipy.sparse.csgraph import minimum_spanning_tree

    # Minimum Spanning Tree
    mst = minimum_spanning_tree(distances).toarray()
    num_cities = distances.shape[0]
    tour, visited = [0], set([0])
    total_cost = 0

    # Construct tour from MST
    def visit(city):
        nonlocal total_cost
        visited.add(city)
        for i in range(num_cities):
            if i not in visited and mst[city, i] > 0:
                total_cost += mst[city, i]
                tour.append(i)
                visit(i)
                tour.append(city) # return to starting city to simulate a tour

    visit(0)

    # Simplify tour: remove loops introduced by backtracking in DFS
    simplified_tour = []
    visited = set()
    for city in tour:
        if city not in visited:
            visited.add(city)
            simplified_tour.append(city)
    simplified_tour.append(0)  # Complete the tour
    
    # Compute the total travel cost
    cost = 0
    for i in range(len(simplified_tour) - 1):
        cost += distances[simplified_tour[i], simplified_tour[i + 1]]
    
    return simplified_tour, cost

# Get the tour and cost
tour, cost = heuristic_tsp(distance_matrix)
print("Tour:", tour)
print("Total travel cost:", cost)