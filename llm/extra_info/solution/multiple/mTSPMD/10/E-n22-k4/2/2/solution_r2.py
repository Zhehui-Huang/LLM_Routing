import numpy as np
from scipy.spatial.distance import euclidean

# City coordinates are given directly
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Robots initial depot assignments
robot_info = {0: 0, 1: 1, 2: 2, 3: 3}

# Function to calculate Euclidean distance
def calculate_distance(i, j):
    return euclidean(cities[i], cities[j])

# Assign cities to robots using a simple nearest neighbor heuristic for simplicity.
def assign_cities_to_robots():
    robots_assignment = {robot: [depot] for robot, depot in robot_info.items()}
    available_cities = set(cities.keys()) - set(robot_info.values())

    while available_cities:
        for robot in robots_assignment:
            if available_cities:
                current_city = robots_assignment[robot][-1]
                next_city = min(available_cities, key=lambda x: calculate_distance(current_city, x))
                robots_assignment[robot].append(next_city)
                available_cities.remove(next_city)

    # Closing the loop by returning to the starting depot
    for robot in robot_info:
        robots_assignment[robot].append(robot_info[robot])

    return robots_assignment

# Calculate the travel cost for each robot's tour
def calculate_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

robots_assignment = assign_cities_to_robots()
overall_total_cost = 0

# Print out the information for each robot
for robot_id, tour in robots_assignment.items():
    tour_cost = calculate_tour_cost(tour)
    overall_total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

# Print overall total cost
print(f"Overall Total Travel Cost: {overall_total_cost}")