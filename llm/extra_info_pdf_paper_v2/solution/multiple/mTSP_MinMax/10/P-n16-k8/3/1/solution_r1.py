import math
import random

# Definition of cities and their coordinates
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of cities and robots
num_cities = len(cities_coordinates)
num_robots = 8

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Distribute cities to robots, each tour starting and ending at the depot
tours = [[] for _ in range(num_robots)]
cities_to_visit = list(range(1, num_cities)) # exclude the depot when distributing cities
random.shuffle(cities_to_visit)

for index, city in enumerate(cities_to_visit):
    robot_index = index % num_robots
    tours[robot_index].append(city)

# Compute the complete tour cost including return to the starting depot
def calculate_tour_cost(tour):
    current_location = 0  # start at the depot
    total_cost = 0
    for city in tour:
        total_cost += distance(current_location, city)
        current_location = city
    total_cost += distance(current_location, 0)  # return to depot
    return total_cost

# Output initial tours and costs
tour_costs = [calculate_tour_cost(tours[i]) for i in range(num_robots)]
max_cost = max(tour_costs)

for robot_id in range(num_robots):
    full_tour = [0] + tours[robot_id] + [0]
    print(f"Robot {robot_id} Tour: {full_tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_costs[robot_id]}")

print(f"Maximum Travel Example of Traveling for a Robot: {max_cost}")