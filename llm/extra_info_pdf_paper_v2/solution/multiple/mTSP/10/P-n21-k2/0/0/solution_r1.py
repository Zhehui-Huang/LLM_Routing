import numpy as np
from sklearn.cluster import KMeans
import math

# Define the cities coordinates
cities = {
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
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
}

# Function to calculate Euclidean distance
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to build a tour using the nearest neighbor heuristic
def build_tour(cities_indices):
    if not cities_indices:
        return [0, 0], 0  # Return to depot if no cities are assigned
    cities_indices = [0] + cities_indices  # Start from depot
    tour = [0]  # Start tour from depot
    total_cost = 0  # Initialize the total tour cost
    while len(tour) - 1 < len(cities_indices):
        current_city = tour[-1]
        if len(tour) == len(cities_indices):
            next_city = 0  # End the tour returning to the depot
        else:
            remaining_cities = [city for city in cities_indices if city not in tour and city != 0]
            next_city = min(remaining_cities, key=lambda city: calc_distance(current_city, city))
        total_cost += calc_distance(current_city, next_city)
        tour.append(next_city)
    return tour, total_cost

# Assign cities to robots using KMeans clustering
num_robots = 2
city_coords = np.array([cities[city] for city in cities if city != 0])  # Exclude depot for clustering
kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(city_coords)
clusters = kmeans.labels_

# Determine cities per robot
robot_cities = {i: [] for i in range(num_robots)}
for i, label in enumerate(clusters):
    robot_cities[label].append(i + 1)  # City indexed from 1

# Calculate tours and costs for each robot
overall_total_cost = 0

for robot in range(num_robots):
    tour, cost = build_tour(robot_cities[robot])
    overall_total_cost += cost
    print(f'Robot {robot} Tour: {tour}')
    print(f'Robot {robot} Total Travel Cost: {cost}')

print(f'Overall Total Travel Cost: {overall_total_cost}')