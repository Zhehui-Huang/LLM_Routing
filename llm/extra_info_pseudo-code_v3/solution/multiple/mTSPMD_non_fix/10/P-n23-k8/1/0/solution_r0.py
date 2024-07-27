import numpy as np
import math

def euclidean_distance(city1, city2):
    dist = math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
    return dist

# City coordinates, index 0 is the starting depot for all robots
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

num_robots = 8
num_cities = len(cities_coordinates)

# Initialization: assign the initial city to each robot which is the depot
tours = {i: [0] for i in range(num_robots)}

# Remaining cities to be allocated
remaining_cities = set(range(1, num_cities))

# Initial solution using NNS
# Each robot will start from the depot and pick nearest city until all cities are picked
while remaining_cities:
    for robot_id in tours:
        if not remaining_cities:
            break
        last_city_id = tours[robot_id][-1]
        next_city_id = min(remaining_cities, key=lambda city: euclidean_distance(cities_coordinates[last_city_id], cities_coordinates[city]))
        tours[robot_id].append(next_city_id)
        remaining_cities.remove(next_city_id)
        
# Calculate cost function for each tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])
    return cost

# Output tours and costs
overall_total_cost = 0
response_output = []

for robot_id, tour in tours.items():
    # For completing tour (not required to return to depot)
    tour_cost = calculate_tour_cost(tour)
    overall_total_cost += tour_cost
    response_output.append(f"Robot {robot_id} Tour: {tour}")
    response_output.append(f"Robot {robot_id} Total Travel Cost: {round(tour_cost, 2)}")

response_output.append(f"Overall Total Travel Cost: {round(overall_total_cost, 2)}")

# Print the output to see results in described format
for line in response_output:
    print(line)