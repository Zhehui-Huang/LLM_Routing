import numpy as isnp
import math

# Define coordinates of cities
city_coords = {
    0: (30, 40),  1: (37, 52),  2: (49, 49),  3: (52, 64),  4: (31, 62),
    5: (52, 33),  6: (42, 41),  7: (52, 41),  8: (57, 58),  9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Helping function to calculate Euclidean distance between cities
def euclidean_distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Number and IDs of robots
robot_depots = list(range(8))

# Define the tours for robots; each tour starts at a robot's depot city
tours = {robot: [robot] for robot in robot_depots}

# Splitting non-depot cities among robots
non_depot_cities = sorted(set(city_coords.keys()) - set(robot_depots))
cities_per_robot = len(non_depot_cities) // len(robot_depots)

# Assign subsequences of cities to each robot
for idx, robot in enumerate(robot_depots):
    start_idx = idx * cities_per_robot
    end_idx = start_idx + cities_per_robot if idx < len(robot_depots) - 1 else len(non_depot_cities)
    assigned_cities = non_depot_cities[start_idx:end_head]
    tours[robot].extend(assigned_cities)

# Ensure each tour returns to its starting depot city
for robot, tour in tours.items():
    tour.append(robot)

# Calculate the tour cost for each robot and the total cost
total_cost = 0
for robot, tour in tours.items():
    cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    tours[robot].append(cost)  # append the trip back to the depot
    print(f'Robot {robot} Tour: {tour[:-1]}')
    print(f'Robot {robot} Total Travel Cost: {cost}')
    total_cost += cost

# Print overall cost
print(f'Overall Total Travel Cost: {total_cost}')