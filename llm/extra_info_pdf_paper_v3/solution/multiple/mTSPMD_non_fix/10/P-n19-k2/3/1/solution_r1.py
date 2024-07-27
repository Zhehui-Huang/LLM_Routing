import math
import random

# Define the coordinates of each depot and city by index
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Number of robots
num_robots = 2

# Initial depot assignments assuming each starts and ends at their respective depot
depots = {0: 0, 1: 1}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Randomly partitioning cities between robots, excluding their depots
def initialize_tours():
    non_depots = list(set(cities.keys()) - set(depots.values()))
    random.shuffle(non_depots)
    split_point = len(non_depots) // num_robots
    tours = {
        0: [depots[0]] + non_depots[:split_point] + [depots[0]],
        1: [depots[1]] + non_depots[split_point:] + [depots[1]]
    }
    return tours

# Calculate the total cost for a tour
def tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Initialize and calculate tours and costs
tours = initialize_tours()
total_costs = {robot: tour_cost(tours[robot]) for robot in tours}
overall_cost = sum(total_costs.values())

# Output results
for robot_id, tour in tours.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {total_costs[robot_id]}")

print(f"Overall Total Travel Cost: {overall_cost}")