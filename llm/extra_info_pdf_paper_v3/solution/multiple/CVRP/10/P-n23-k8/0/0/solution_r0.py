import math
from itertools import permutations

# City coordinates and demands
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robot parameters
num_robots = 8
robot_capacity = 40

# Helper function to calculate the Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initialization of robots' tours
tours = [[] for _ in range(num_robots)]
current_capacity = [0] * num_robots
tour_costs = [0] * num_robots

def find_closest_city(current_city, remaining_cities, current_load):
    min_distance = float('inf')
    closest_city = None
    for idx in remaining_cities:
        if demands[idx] + current_load <= robot_capacity:
            dist = distance(cities[current_city], cities[idx])
            if dist < min_distance:
                min_distance = dist
                closest_city = idx
    return closest_city, min_distance

# Assign cities to robots
remaining_cities = set(range(1, len(cities)))  # Skip the depot which is city 0

robot_index = 0
while remaining_cities:
    current_city = 0  # always start at depot
    tours[robot_index].append(current_city)

    while True:
        next_city, travel_cost = find_closest_city(current_city, remaining_cities, current_capacity[robot_index])
        if next_city is None:
            break
        tours[robot_index].append(next_city)
        tour_costs[robot_index] += travel_cost
        current_capacity[robot_index] += demands[next_city]
        current_city = next_city
        remaining_cities.remove(next_city)

    # Close the loop back to the depot
    return_to_depot_cost = distance(cities[current_city], cities[0])
    tours[robot_index].append(0)
    tour_costs[robot_index] += return_to_depot_cost

    if not remaining_cities:
        break
    robot_index = (robot_index + 1) % num_robots  # move to the next robot

# Calculate the overall total cost
overall_total_cost = sum(tour_costs)

# Print the output
for i, tour in enumerate(tours):
    if tour:
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")