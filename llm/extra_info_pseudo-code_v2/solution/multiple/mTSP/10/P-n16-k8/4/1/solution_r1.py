import math
import numpy as np

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Coordinates for each city including the depot city
cities = [
    (30, 40),  # Depot city 0
    (37, 52), 
    (49, 49), 
    (52, 64), 
    (31, 62), 
    (52, 33), 
    (42, 41), 
    (52, 41), 
    (57, 58), 
    (62, 42), 
    (42, 57), 
    (27, 68), 
    (43, 67), 
    (58, 48), 
    (58, 27), 
    (37, 69)
]

num_robots = 8
num_cities = len(cities)

# Distance matrix calculation
dist_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Nearest neighbor heuristic to assign cities to each robot
def nearest_neighbor(current_city, unvisited_cities):
    nearest = min(unvisited_cities, key=lambda x: dist_matrix[current_city][x])
    return nearest

# Split cities among robots approximately evenly
city_indices = list(range(1, num_cities))  # Exclude depot (0)
city_chunks = [city_indices[i::num_robots] for i in range(num_robots)]

tours = []
total_costs = []

for i in range(num_robots):
    tour = [0]  # start at depot
    current_city = 0
    assigned_cities = city_chunks[i]
    unvisited = assigned_cities.copy()

    while unvisited:
        next_city = nearest_neighbor(current_city, unvisited)
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(0)  # return to depot
    tours.append(tour)

    # Calculate tour cost
    tour_cost = sum(dist_matrix[tour[j]][tour[j + 1]] for j in range(len(tour) - 1))
    total_costs.append(tour_cost)

# Print results
overall_total_cost = sum(total_costs)
for idx, (tour, cost) in enumerate(zip(tours, total_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")