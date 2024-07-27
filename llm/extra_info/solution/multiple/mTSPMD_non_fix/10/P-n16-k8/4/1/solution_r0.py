import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from itertools import permutations

# Define the cities coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots and their starting depots
num_robots = 8
depot = 0  # All starting at city 0

def calculate_cost(route):
    """Calculate travel cost based on Euclidean distance."""
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean(cities[route[i]], cities[route[i+1]])
    return cost

def solve_tsp_brute_force(points):
    """Solves TSP with a brute-force approach."""
    min_route = None
    min_cost = float('inf')
    for perm in permutations(points):
        cost = calculate_cost(perm)
        if cost < min_cost:
            min_cost = cost
            min_route = perm
    return min_route, min_cost

# Assign cities to robots using clustering
coords = np.array(list(cities.values()))
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coords)
labels = kmeans.labels_

# Organizing cities per robot
robot_tours = {i: [] for i in range(num_robots)}
for city, label in enumerate(labels):
    robot_tours[label].append(city)

# Solve TSP for each robot cluster and calculate costs
overall_total_cost = 0
for robot_id in range(num_robots):
    tour, cost = solve_tsp_brute_force(robot_tours[robot_id])
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")
    overall_total_cost += cost

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")