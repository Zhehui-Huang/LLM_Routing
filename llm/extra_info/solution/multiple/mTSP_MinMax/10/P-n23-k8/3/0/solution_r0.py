import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates of all cities including the depot
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
])

def calculate_distance(a, b):
    return euclidean(a, b)

def solve_tsp_brute_force(cities):
    min_tour = None
    min_cost = float('inf')
    all_tours = permutations(cities)
    for tour in all_tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(tour[i], tour[i + 1])
        # Adding the cost from the last city back to the depot
        cost += calculate_distance(tour[-1], coordinates[0])
        if cost < min_cost:
            min_cost = cost
            min_tour = tour
    return min_cost, min_tour

num_robots = 8
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:]) # excluding the depot city
labels = kmeans.labels_

robots_routes = {i: [0] for i in range(num_robots)}  # initialize routes starting at the depot
for city_index, label in enumerate(labels, start=1):
    robots_routes[label].append(city_index)

# Solving TSP for each robot's assigned cities
max_travel_cost = 0
for robot_id, cities in robots_routes.items():
    cities.append(0)  # returning to the depot
    travel_cost, tour = solve_tsp_brute_force([coordinates[city] for city in cities])
    robots_routes[robot_id] = [coordinates.tolist().index(loc) for loc in tour]  # convert locations back to indices
    print(f"Robot {robot_id} Tour: {robots_routes[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {travel_cost}")
    if travel_cost > max_travel_max:
        max_travel_cost = travel_cost

print(f"Maximum Travel Cost: {max_travel_cost}")