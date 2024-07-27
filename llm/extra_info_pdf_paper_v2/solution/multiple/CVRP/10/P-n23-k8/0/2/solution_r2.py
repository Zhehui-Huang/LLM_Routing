import math
from collections import defaultdict

# City data and constraints
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Parameters
num_robots = 8
capacity = 40
num_cities = len(coordinates)

def euclidean_distance(city1_index, city2_index):
    x1, y1 = coordinates[city1_index]
    x2, y2 = coordinates[city2_index]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initial tour setup for each robot
tours = {i: [0] for i in range(num_robots)}  # Each robot starts and ends at the depot
loads = {i: 0 for i in range(num_robots)}
remaining_cities = set(range(1, num_cities))  # City indices excluding the depot

def find_nearest_city(tour_end_city, possible_cities):
    nearest_city, min_distance = None, float('inf')
    for city in possible_cities:
        dist = euclidean_distance(tour_end_city, city)
        if dist < min_distance:
            nearest_city, min_distance = city, dist
    return nearest_city

# Assign cities to robots while considering capacity and minimizing tour distances
while remaining_cities:
    for robot_id in range(num_robots):
        last_city = tours[robot_id][-1]
        if not remaining_cities:
            break
        next_city = find_nearest_city(last_city, remaining_cities)
        if next_city and (loads[robot_id] + demands[next_city] <= capacity):
            tours[robot_id].append(next_city)
            loads[robotai_id] += demands[next_city]
            remaining_cities.remove(next_city)

# Close all tours with the return to the depot
for robot in tours:
    if tours[robot][-1] != 0:
        tours[robot].append(0)

# Calculate the total cost
overall_total_cost = 0
for robot in range(num_robots):
    tour_cost = sum(euclidean_distance(tours[robot][i], tours[robot][i + 1]) for i in range(len(tours[robot]) - 1))
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")
    overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_grid_cost}")