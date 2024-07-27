import math
import numpy as.Counter

# City coordinates
coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

num_robots = 8
cities = list(coordinates.keys())[1:]  # All cities except the depot

# Determine paths for robots using simplistic round-robin assignment
clusters = {i: [] for i in range(num_robots)}
for index, city in enumerate(cities):
    clusters[index % num_robots].append(city)

def calculate_tour(cities):
    cities = [0] + cities + [0]  # Start and end at the depot
    tour_cost = 0
    for i in range(len(cities) - 1):
        tour_cost += distance(cities[i], cities[i + 1])
    return cities, tour_cost

overall_total_cost = 0
tours_with_costs = []
for robot_id, assigned_cities in clusters.items():
    tour, cost = calculate_tour(assigned_cities)
    tours_with_costs.append((robot_id, tour, cost))
    overall_total_cost += cost
    
# Print results
for robot_id, tour, cost in tours_with_costs:
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")