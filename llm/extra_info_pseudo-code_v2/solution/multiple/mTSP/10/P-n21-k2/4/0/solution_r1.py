import numpy as np
from scipy.spatial.distance import euclidean

# Coordinates of each city including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Compute distances between all pairs of cities
n_cities = len(coordinates)
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(i, n_cities):
        d = euclidean(coordinates[i], coordinates[j])
        distance_matrix[i, j] = d
        distance_matrix[j, i] = d

# Number of robots (salesmen)
n_robots = 2

# Greedy helper function to find the nearest unvisited city
def find_nearest(current_city, unvisited):
    nearest_city = None
    min_distance = float('inf')
    for city in unvisited:
        if distance_matrix[current_city, city] < min_distance:
            nearest_city = city
            min_distance = distance_matrix[current_city, city]
    return nearest_city, min_distance

# Assign each robot a tour
robots_tours = [[] for _ in range(n_robots)]
robots_costs = [0] * n_robots

# Distribute cities (except the depot 0) to robots using a round-robin approach
unvisited = list(range(1, n_cities))
for i in range(len(unvisited)):
    robot_id = i % n_robots
    if robots_tours[robot_id]:
        current_city = robots_tours[robot_id][-1]
    else:
        current_city = 0  # start from depot

    next_city, travel_cost = find_nearest(current_city, unvisited)
    robots_tours[robot_id].append(next_city)
    robots_costs[robot_id] += travel_cost
    unvisited.remove(next_city)

# Return to the depot and calculate the return trip cost
for i in range(n_robots):
    last_city = robots_tours[i][-1]
    robots_tours[i].append(0)  # end at depot
    robots_costs[i] += distance_matrix[last_city, 0]

# Display the results
overall_travel_cost = 0
for i in range(n_robots):
    print(f"Robot {i} Tour: {[0] + robots_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {robots_costs[i]:.2f}")
    overall_travel_cost += robots_costs[i]

print(f"Overall Total Travel Cost: {overall_travel_cost:.2f}")