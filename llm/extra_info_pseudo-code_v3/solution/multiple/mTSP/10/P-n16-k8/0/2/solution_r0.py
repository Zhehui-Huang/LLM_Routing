import numpy as np
import random

# Input cities coordinates, including depot
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# Number of robots
num_robots = 8

# Euclidean distance calculator
def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Distance matrix
distance_matrix = [[calculate_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Function to find a basic solution with nearest neighbor algorithm
def nearest_neighbor_tour(start_city, cities_to_visit):
    tour = [start_city]
    current_city = start_city
    total_cost = 0

    while cities_to_visit:
        next_city = min(cities_to_visit, key=lambda c: distance_matrix[current_city][c])
        total_cost += distance_matrix[current_city][next_city]
        tour.append(next_city)
        cities_to_visit.remove(next_city)
        current_city = next_city

    total_cost += distance_matrix[current_city][start_city]
    tour.append(start_city)
    return tour, total_cost

# Simple way to split cities into clusters (not optimal)
def simple_city_distributor(cities_indices, num_robots):
    random.shuffle(cities_indices)
    return [cities_indices[i::num_robots] for i in range(num_robots)]

# Divide cities among robots, excluding the depot (city 0)
cities_indices = list(range(1, len(cities)))  # cities 1 to 15
clusters = simple_city_distributor(cities_indices, num_robots)

# Gathering the solutions for each robot
tours = []
total_costs = []
overall_cost = 0

for i in range(num_robots):
    cluster = clusters[i]
    tour, tour_cost = nearest_neighbor_tour(0, cluster.copy())
    tours.append(tour)
    total_costs.append(tour_cost)
    overall_cost += tour_cost

# Output results
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {total_costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")