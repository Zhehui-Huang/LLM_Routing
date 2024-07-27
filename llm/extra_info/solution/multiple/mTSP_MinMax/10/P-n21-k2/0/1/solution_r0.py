import numpy as np
from pyconcorde import TSPSolver
from sklearn.cluster import KMeans

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Convert to numpy array for processing with TSP solver and K-means
coordinates = np.array([cities[i] for i in cities])

# Number of robots
num_robots = 2

# Deploy K-means to cluster cities based on their coordinates
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:]) # Exclude depot for clustering

# Create clusters
clusters = {i: [0] for i in range(num_robots)}  # each cluster must include the depot city at the start
for idx, label in enumerate(kmeans.labels_):
    clusters[label].append(idx + 1)  # adjust city index since clustering was done from city 1

# Solve TSP for each cluster
def calculate_euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

tour_costs = {}
max_distance = 0

for robot in clusters:
    points_order = [cities[i] for i in clusters[robot]]
    solver = TSPSolver.from_data(*zip(*points_order), norm="EUC_2D")
    solution = solver.solve(verbose=False)
    tour_indices = [clusters[robot][i] for i in solution.tour] + [clusters[robot][0]]
    tour_cost = sum(calculate_euclidean_distance(cities[tour_indices[i]], cities[tour_indices[i+1]]) for i in range(len(tour_indices) - 1))
    tour_costs[robot] = (tour_indices, tour_cost)
    max_distance = max(max_distance, tour_cost)

# Output results
for robot, (tour, cost) in tour_costs.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {round(cost, 2)}\n")

print(f"Maximum Travel and Cost: {round(max_distance, 2)}")