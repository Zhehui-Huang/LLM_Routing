import numpy as np
from scipy.spatial.distance import euclidean

# Define the cities with coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Euclidean distance function
def calculate_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Simple greedy algorithm for TSP
def tsp_tour(start_city, cities_to_visit):
    unvisited = cities_to_visit[:]
    tour = [start_city]
    while unvisited:
        last_city = tour[-1]
        next_city = min(unvisited, key=lambda city: calculate_distance(last_city, city))
        unvisited.remove(next_city)
        tour.append(next_city)
    tour.append(start_city)  # return to the starting city
    return tour

# Assigning cities to robots (naive split, can be adjusted to KMeans or other method)
num_cities = len(cities) - 1  # excluding the depot
num_robots = 8
city_indices = list(cities.keys())[1:]  # excluding depot
split_size = num_cities // num_robots

# Split cities amongst robots assumming roughly equal distribution
robot_tours = {}
for i in range(num_robots):
    start_index = i * split_size
    if i == num_robots - 1:
        assigned_cities = city_indices[start_index:]  # last robot takes all remaining cities
    else:
        assigned_cities = city_indices[start_index:start_index + split_size]
    # Calculate TSP tour for the assigned cities
    robot_tours[i] = tsp_tour(0, assigned_cities)

# Calculate costs and find the maximum
max_travel_cost = 0
costs = {}

for robot_id, tour in robot_tours.items():
    cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    costs[robot_id] = cost
    max_travel_cost = max(max_travel_cost, cost)
    print(f'Robot {robot_id} Tour: {tour}')
    print(f'Robot {robot_id} Total Travel Cost: {cost:.2f}')

print(f'Maximum Travel Cost: {max_travel_cost:.2f}')