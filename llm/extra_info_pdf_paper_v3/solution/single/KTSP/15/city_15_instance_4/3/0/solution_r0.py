import numpy as np
from itertools import combinations
from scipy.spatial import distance_matrix

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate the Euclidean distance matrix
city_locations = np.array(list(cities.values()))
d_matrix = distance_matrix(city_locations, city_by_locations)

# Number of cities to be visited excluding the depot
k = 12

# Helper function to calculate total route cost
def route_cost(route):
    return sum(d_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))

# Greedy heuristic approach for k-TSP

def greedy_ktsp(start_city, num_cities):
    # Start from the depot, visit k cities and return to the depot
    unvisited = list(cities.keys())
    unvisited.remove(start_city)
    tour = [start_city]
    
    while len(tour) < num_cities:
        last = tour[-1]
        # Find nearest unvisited city
        next_city = min(unvisited, key=lambda x: d_matrix[last, x])
        tour.append(next_city)
        unvisited.remove(next_city)
    
    tour.append(start_city)  # return to the depot
    return tour

# Get a greedy tour for initial solution
solution = greedy_ktsp(0, k)

# Calculate the cost of the tour
total_cost = route_cost(solution)

# Output the tour and total cost
print("Tour:", solution)
print("Total travel cost:", total_cost)