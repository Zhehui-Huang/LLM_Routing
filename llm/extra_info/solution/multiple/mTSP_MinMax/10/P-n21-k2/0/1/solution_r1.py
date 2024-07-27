import numpy as np
import math

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Basic greedy approach to assign cities to each robot
city_indices = list(cities.keys())[1:]  # Exclude depot
num_robots = 2
cities_per_robot = len(city_indices) // num_robots
assignments = {i: [] for i in range(num_robots)}

for i, city_index in enumerate(sorted(city_indices, key=lambda x: calculate_euclidean_distance(cities[0], cities[x]))):
    assignments[i % num_robots].append(city_index)

# Each robot plans a simple round trip from the depot
def plan_tour(robot_cities):
    tour = [0]  # Start at the depot
    while robot_cities:
        # Find nearest city not yet visited; simple greedy approach
        last_city = tour[-1]
        next_city = min(robot_cities, key=lambda x: calculate_euclidean_distance(cities[last_city], cities[x]))
        tour.append(next_city)
        robot_cities.remove(next_city)
    tour.append(0)  # Return to depot
    return tour

# Determine the tours and calculate the cost
tour_costs = {}
max_travel_cost = 0

for robot, robot_cities in assignments.items():
    tour = plan_tour(robot_cities)
    tour_cost = sum(calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    tour_costs[robot] = (tour, tour_cost)
    max_travel_cost = max(max_travel_cost, tour_cost)

# Output results
for robot, (tour, cost) in tour_costs.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_travel_type_cost}")