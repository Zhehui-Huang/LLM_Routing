import numpy as np
from scipy.spatial.distance import euclidean

# List of city coordinates including the depot
cities = [
    (30, 40),  # Depot (0)
    (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 48), (58, 27), (37, 69)
]

# Num of robots
num_robots = 8

# Function to compute the total distance of a given tour
def compute_tour_distance(tour, city_coordinates):
    distance = 0
    for i in range(len(tour) - 1):
        distance += euclidean(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    return distance

# Function to determine a simple tour (not an optimized solution)
def simple_tour(num_robots, cities):
    num_cities = len(cities)
    cities_per_robot = (num_cities - 1) // num_robots
    tours = []
    start = 1  # start from city 1 as city 0 is the depot
    for i in range(num_robots):
        end = start + cities_per_robot
        if i < (num_cities - 1) % num_robots:  # handle remainder
            end += 1
        tour = [0] + list(range(start, end)) + [0]
        tours.append(tour)
        start = end
    return tours

# Generate simple tours
tours = simple_tour(num_robots, cities)
total_costs = []
overall_total_cost = 0

for i, tour in enumerate(tours):
    cost = compute_tour_distance(tour, cities)
    total_costs.append(cost)
    overall_total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")