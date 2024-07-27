import numpy as np
import random

# Function to calculate the Euclidean distance between two points
def euclidean_distance(pt1, pt2):
    return np.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# Define the cities with their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Define the robots and depot assignments
depots = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7
}
robots = list(depots.keys())

# Separate non-depot cities
non_depot_cities = [city for city in cities if city not in depots.values()]

# Initialize tours for each robot: trivial tours where each robot goes to one city and back
tours = {robot: [depots[robot], city, depots[robot]] for robot, city in zip(robots, non_depot_cities[:len(robots)])}

# Assign remaining cities to tours randomly
remaining_cities = non_depot_cities[len(robots):]
random.shuffle(remaining_cities)
for city in remaining_cities:
    chosen_robot = random.choice(robots)  # Choose a random robot
    insert_position = random.randint(1, len(tours[chosen_robot]) - 1)  # Choose a position to insert city
    tours[chosen_robot].insert(insert_position, city)

# Function to calculate total cost of a tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Calculate total costs
total_costs = {robot: calculate_tour_cost(tours[robot]) for robot in robots}
overall_cost = sum(total_costs.values())

# Print results
for robot in robots:
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {total_costs[robot]}")

print(f"Overall Total Travel Cost: {overall_cost}")