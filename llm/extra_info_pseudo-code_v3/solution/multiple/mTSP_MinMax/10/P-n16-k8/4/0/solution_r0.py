import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean
import random

# Define the cities and their coordinates
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
    15: (37, 69)
}

# Total number of robots
num_robots = 8

# For clustering, extract only the client city coordinates excluding the depot
client_cities = [cities[i] for i in cities if i != 0]
city_ids = [i for i in cities if i != 0]

# Fuzzy C-Means Clustering (we'll approximate with KMeans for simplicity here)
kmeans = KMeans(n_clusters=num_robots, random_state=42)
clusters = kmeans.fit_predict(client_cities)

# Associate each city to each robot based on cluster
def assign_cities_to_robot(clusters):
    robot_routes = {r: [] for r in range(num_robots)}
    for city_index, cluster in enumerate(clusters):
        robot_routes[cluster].append(city_ids[city_index])
    return robot_routes

robot_routes = assign_cities_to_robot(clusters)

# Function to calculate travel cost for a given route
def calculate_travel_cost(route):
    return sum(euclidean(cities[route[i]], cities[route[i+1]]) for i in range(len(route)-1))

# Improve initialization using a simple greedy algorithm for each robot
def greedy_improvement(route):
    route = [0] + route # start at depot
    improved = False

    while not improved:
        improved = True
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue # these are consecutive, ignore
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if calculate_travel_cost(new_route) < calculate_travel_cost(route):
                    route = new_route
                    improved = False
    return route + [0] # return to depot

# Adjust each route to start and end at depot and perform local improvement
for robot_id in robot_routes:
    robot_routes[robot_id] = greedy_improvement(robot_routes[robot_id])

# Calculate the total distance for each robot's route and the maximum travel cost
distances = {}
max_distance = 0

for robot_id in robot_routes:
    route_with_depot = [0] + robot_routes[robot_id] + [0]
    distance = calculate_travel_cost(route_with_depot)
    distances[robot_id] = distance
    max_distance = max(max_distance, distance)
    print(f"Robot {robot_id} Tour: {route_with_depot}")
    print(f"Robot {robot_id} Total Travel Cost: {distance}")

print(f"\nMaximum Travel Cost: {max_distance}")