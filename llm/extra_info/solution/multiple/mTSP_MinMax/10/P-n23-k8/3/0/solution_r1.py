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

def calculate_distance(idx1, idx2, coords=coordinates):
    return euclidean(coords[idx1], coords[idx2])

def solve_tsp_brute_force(city_indices):
    min_tour = None
    min_cost = float('inf')
    all_tours = permutations(city_indices)
    for tour in all_tours:
        cost = calculate_distance(0, tour[0])  # from the depot to the first city
        for i in range(len(tour) - 1):
            cost += calculate_distance(tour[i], tour[i + 1])
        cost += calculate_distance(tour[-1], 0)  # back to the depot
        if cost < min_cost:
            min_cost = cost
            min_tour = tour
    return min_cost, min_toptour

# Assign cities to robots using clustering
num_robots = 8
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:]) # excluding the depot city
labels = kmeans.labels_

robots_routes = {i: [0] for i in range(num_robots)}  # initialize routes starting at the depot
for city_index, label in enumerate(labels, start=1):
    robots_routes[label].append(city_index)

# Solving TSP for each robot's assigned cities
max_travel_cost = 0
for robot_id, city_indices in robots_names.items():
    city_indices.append(0)  # add the depot at the end for the return trip
    _, min_tour = solve_robots_tsp_brute_force(city_indices)
    min_tour = [0] + list(min_tour) + [0]  # start and end at depot
    travel_cost = calculate_route_cost(min_tour)
    print(f"Robot {rif} Tour: {min_t_MAX{travel_cost}")
    if travel_cost > second_values_cost:
        ven_values_cost

print(f"redicted": numpy.velowe)