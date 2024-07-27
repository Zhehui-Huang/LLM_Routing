import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# City Coordinates
cities = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
])

# Number of robots
num_robots = 8

# KMeans to cluster cities into groups for each robot
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities[1:])
labels = kmeans.labels_

# Initial tours based on clustering, each robot starting at depot and ending at depot
tours = {i: [0] for i in range(num_robots)}
for i, label in enumerate(labels):
    tours[label].append(i + 1)  # City indices are offset by 1 (ignoring the depot)
for key in tours:
    tours[key].append(0)  # End tour at depot

# Compute the distance matrix between all pairs of cities
distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[i][j] = euclidean(cities[i], cities[j])

# Define a simple 2-opt optimizer
def two_opt(route, distance_matrix):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 2, len(route) - 1):  # Ensure at least three elements between i and j
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                old_cost = sum(distance_matrix[route[n]][route[n + 1]] for n in range(i-1, j))
                new_cost = sum(distance_matrix[new_route[n]][new_route[n + 1]] for n in range(i-1, j))
                if new_cost < old_cost:
                    best = new_route
                    improved = True
        route = best
    return best

# Optimize each robot's tour using 2-opt
optimized_tours = {}
for key in tours:
    optimized_tours[key] = two_opt(tours[key], distance_matrix)

# Calculate and print tours and costs
overall_total_cost = 0
for key in optimized_tours:
    tour_cost = sum(distance_matrix[optimized_tours[key][i]][optimized_tours[key][i + 1]] for i in range(len(optimized_tours[key]) - 1))
    print(f'Robot {key} Tour: {optimized_tours[key]}')
    print(f'Robot {key} Total Travel Cost: {tour_cost:.2f}')
    overall_total_cost += tour_cost

print(f'Overall Total Travel Cost: {overall_total_tanzania_cost:.2f}')