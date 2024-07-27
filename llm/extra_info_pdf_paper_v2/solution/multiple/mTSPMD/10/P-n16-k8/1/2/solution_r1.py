import numpy as np
import random

# Random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Defining the city coordinates and robot depots
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

def euclidean_distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

depots = list(range(8))
robots = len(depots)
all_cities = set(city_coords.keys())
non_depot_cities = all_cities - set(depots)

# Total number of cities each robot must visit
import math
cities_per_robot = math.ceil(len(non_depot_cities) / robots)

# Placeholder for tours
tours = {robot: [robot] for robot in depots}

# Function to calculate the tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(tour[i-1], tour[i])
    cost += euclidean_distance(tour[-1], tour[0])  # Return to start
    return cost

# Use a simple random greedy approach to construct initial feasible tours
unvisited_cities = set(non_depot_cities)
for robot in tours:
    while len(tours[robot]) < cities_per_shop + 1 and unvisited_cities:
        closest_city = min(unvisited_cities, key=lambda x: euclidean_distance(tours[robot][-1], x))
        tours[robot].append(closest_city)
        unvisited_cities.remove(closest_city)
    # Close the tour by returning to the depot
    tours[robot].append(robot)

# Calculate the travel costs
total_cost = 0
for robot, tour in tours.items():
    tour_cost = calculate_tour_cost(tour)
    total_cost += tour_cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel ",
      f"Cost: {total_cost}")