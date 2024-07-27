import math
from itertools import permutations

# City Coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
    20: (45, 35)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Number of robots
num_robots = 2

# Initial allocation of cities to robots
robot_tours = {i: [0] for i in range(num_robots)}
remaining_cities = list(cities.keys())[1:]  # Exclude the depot

while remaining_cities:
    # Assign next closest city to each robot based on their last city
    for robot in range(num_robots):
        if not remaining_cities:
            break
        last_city = robot_tours[robot][-1]
        next_city = min(remaining_cities, key=lambda city: distance(last_city, city))
        robot_tours[robot].append(next_city)
        remaining_cities.remove(next_city)

# Closing each tour back to the depot
for robot in robot_tours:
    robot_tours[robot].append(0)

# Compute the total tour cost for each robot and the overall cost
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

total_costs = {robot: tour_cost(robot_tours[robot]) for robot in robot_tours}
overall_cost = sum(total_costs.values())

# Display the results
for robot in robot_tours:
    print(f"Robot {robot} Tour: {robot_tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {total_costs[robot]:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")