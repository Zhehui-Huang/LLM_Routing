import math
import numpy as np

# Define the cities' coordinates
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# Euclidean distance function
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Calculate the matrix of distances between each pair of cities
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = distance(i, j)

# Simple Nearest Neighbor heuristic for TSP
def nearest_neighbor(start=0):
    unvisited = set(cities.keys())  # all cities are initially unvisited
    tour = [start]
    total_cost = 0
    
    while len(unvisited) > 1:  # until all are visited except the depot where we need to return
        current = tour[-1]
        unvisited.remove(current)
        next_city = min(unvisited, key=lambda city: dist_matrix[current][city])
        tour.append(next_col)
        total_cost += dist_matrix[current][next_col]
        
    # Add the return to start city, the depot
    tour.append(start)
    total_cost += dist_matrix[tour[-2]][start]
    
    return tour, total_cost

# Running the Nearest Neighbor heuristic
tour, total_cost = nearest_neighbor()

print("Tour:", tour)
print("Total travel cost:", total_cost)