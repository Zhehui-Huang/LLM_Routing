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

# Function to find the tour and its cost using the nearest neighbor heuristic
def find_tour(cities_indices):
    tour = [0]  # Start tour from the depot
    unvisited = set(cities_indices)
    current_city = 0
    total_cost = 0
    while unvisited:
        next_city = min(unvisited, key=lambda city: calc_distance(current_city, city))
        total_cost += calc_distance(current_city, next_city)
        current_city = next_city
        tour.append(current_city)
        unvisited.remove(current_city)
    # Return to depot
    total_cost += calc_distance(current_city, 0)
    tour.append(0)
    return tour, total_cost

# Number of robots (salesmen)
num_robots = 2

# Cluster the cities using their coordinates to divide them among robots
city_points = np.array([coord for coord in cities.values()])
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_points[1:])  # Exclude depot from clustering
labels = kmeans.labels_

# Assign cities to each robot based on clustering
robots_cities = {i: [] for i in range(num_robots)}
for idx, label in enumerate(labels):
    robots_cities[label].append(idx + 1)  # +1 to adjust for zero-indexed labels and considering depot

# Now find the tours for each robot
tours = []
total_travel_costs = []
overall_total_cost = 0

for i in range(num_robots):
    tour, total_cost = find_tour(robots_cities[i])
    tours.append(tour)
    total_travel_costs.append(total_cost)
    overall_total_cost += total cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {total_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")