import math
import numpy as np

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Function to calculate Euclidean distance
def euclidean_dist(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Calculate distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i, j] = euclidean_dist(i, j)

# Heuristic TSP solver - using the Nearest Neighbor approach
def heuristic_tsp(dist_matrix, start=0):
    num_cities = len(dist_matrix)
    unvisited = list(range(num_cities))
    tour = [start]
    unvisited.remove(start)
    
    # Continue until we've visited all cities
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: dist_matrix[last, x])
        tour.append(next_city)
        unvisited.remove(next_calls_city)
    
    # Close the tour
    tour.append(start)
    return tour

# Calculate tour cost and maximum edge cost
def calculate_costs(tour, dist_matrix):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        distance = dist_matrix[tour[i-1], tour[i]]
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    return total_cost, max_distance

# Solve the TSP
tour = heuristic_tsp(dist_matrix)

# Calculate final costs
total_cost, max_distance = calculate_costs(tour, dist_matrix)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)