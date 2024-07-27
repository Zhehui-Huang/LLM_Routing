import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# Define the city coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Calculate Euclidean distance between two city indices
def calc_distance(i, j):
    return euclidean(cities[i], cities[j])

# Implement the 2-opt Swap to improve an existing route
def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # Skip adjacent cities (no change)
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if sum(calc_distance(new_route[k], new_route[k+1]) for k in range(len(new_route) - 1)) < \
                   sum(calc_distance(best[k], best[k+1]) for k in range(len(best) - 1)):
                    best = new_route
                    improved = True
        route = best
    return best

# Use KMeans clustering to divide the cities between two robots
def cluster_cities(n_robots=2):
    points = np.array([cities[i] for i in cities])
    kmeans = KMeans(n_clusters=n_robots, random_state=0).fit(points)
    clusters = {i: [] for i in range(n_robots)}
    for idx, label in enumerate(kmeans.labels_):
        if idx != 0:  # Exclude depot from clusters
            clusters[label].append(idx)
    return clusters

# Route calculation for each robot
def calculate_routes(clusters):
    robot_routes = {}
    for robot_id, cities_list in clusters.items():
        # Start and end at the depot
        route = [0] + cities_list + [0]
        optimized_route = two_opt(route)
        robot_routes[robot_id] = optimized_route
    return robot_routes

# Execution of functions
clusters = cluster_cities()
robot_routes = calculate_routes(clusters)
robot_costs = {robot_id: sum(calc_distance(robot_routes[robot_id][i], robot_routes[robot_id][i + 1]) for i in range(len(robot_routes[robot_id]) - 1)) for robot_id in robot_routes}
max_cost = max(robot_costs.values())

# Output results
for robot_id in robot_routes:
    print(f"Robot {robot_id} Tour: {robot_routes[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {robot_costs[robot_id]}")

print(f"Maximum Travel Cost: {max_cost}")