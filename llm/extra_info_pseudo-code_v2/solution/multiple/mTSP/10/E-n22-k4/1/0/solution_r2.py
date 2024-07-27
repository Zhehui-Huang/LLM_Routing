import numpy as np
from scipy.spatial.distance import euclidean

# Coordinates of the cities (indexed by city ID)
cities = {
    0: (145, 215),  # Depot
    1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239),
    9: (163, 236), 10: (148, 232), 11: (128, 231), 12: (156, 217),
    13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206),
    17: (147, 193), 18: (164, 193), 19: (129, 189), 20: (155, 185),
    21: (139, 182)
}

# Number of robots
num_robots = 4

# Function to calculate the distance between two cities
def calculate_distance(city1_id, city2_id):
    return euclidean(cities[city1_id], cities[city2_id])

# Initialize tours lists
tours = {i: [0] for i in range(num_robots)}
additional_cities = list(cities.keys())[1:]  # exclude the depot

# Simple greedy assignment: assign cities based on nearest unassigned cities
while additional_cities:
    for robot_id in range(num_robots):
        if not additional_cities:
            break
        # Find nearest city to the last city in the current robot's tour
        last_city = tours[robot_id][-1]
        next_city = min(additional_cities, key=lambda city: calculate_distance(last_city, city))
        tours[robot_id].append(next_city)
        additional_cities.remove(next_city)

# Ensuring each robot returns to depot
for robot_id in range(num_robots):
    tours[robot_id].append(0)

# Calculate tour cost
def tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Display results and calculate the cost
overall_total_cost = 0
for robot_id in range(num_robots):
    cost = tour_cost(tours[robot_id])
    overall_total_cost += cost
    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot  id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")