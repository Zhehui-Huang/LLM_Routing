import numpy as from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt

# City coordinates
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
          (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
          (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
num_cities = len(cities)

# Number of robots available
num_robots = 8
assert num_robots <= num_cities - 1  # Ensure there are enough cities for the robots

# Compute the distance matrix
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = euclidean(cities[i], cities[j])

# Using k-means to cluster the cities for the initial solution assignment
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=num_robots, random_state=0)
assignments = kmeans.fit_predict(np.array(cities[1:]))  # Excluding the depot

# Local search function: 2-opt heuristic
def two_opt(route, dist_matrix):
    best = route
    best_cost = float('inf')
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 1):
            for j in range(i + 2, len(route) + (i > 0)):
                j_mod = j % len(route)  # wrap around
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                new_cost = sum(dist_matrix[new_route[k % len(route)], new_route[(k + 1) % len(route)]] for k in range(len(route)))
                if new_cost < best_cost:
                    best, best_cost, improved = new_route, new_cost, True
        route = best
    return best, best_cost

# Solve for each robot
overall_total_cost = 0
for robot_id in range(num_robots):
    robot_cities = [0] + [idx + 1 for idx, cluster_id in enumerate(assignments) if cluster_id == robot_id]
    if len(robot_cities) == 1:
        continue  # No cities assigned other than the depot
    initial_tour = robot_cities + [0]  # Include return to the depot
    improved_tour, tour_cost = two_opt(initial_tour, dist_matrix)
    overall_total_cost += tour_cost

    # Display the result per robot
    print(f"Robot {robot_id} Tour: {improved_tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")