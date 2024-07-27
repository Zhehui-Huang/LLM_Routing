import numpy as np
from itertools import permutations
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate the Euclidean distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean(cities[i], cities[j])

# Helper function to calculate total route cost
def route_cost(route):
    return sum(distance_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))

def greedy_ktsp(start_city, k):
    unvisited = list(cities.keys())
    unvisited.remove(start_city)
    tour = [start_city]

    current_city = start_city
    while len(tour) < k:
        next_city = min(unvisited, key=lambda x: distance_matrix[current_city][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # return to the depot
    return tour

# Use the greedy approach to get a good starting path
# Select 11 other cities plus the depot to visit (total 12 including the depot)
selected_cities = [0] + sorted(cities.keys())[1:12]  # This is a simplification: needs a better selection method in practice
best_tour = greedy_ktsp(0, len(selected_cities))
best_cost = route_cost(best_tour)

# Output the tour and total travel cost
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))