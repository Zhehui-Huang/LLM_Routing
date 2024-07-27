import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Specify the total number of robots and city coordinates
num_robots = 8
coordinates = np.array([
    [30, 40], [37, 52], [49, 49], [52, 64], [31, 62], [52, 33], [42, 41], [52, 41],
    [57, 58], [62, 42], [42, 57], [27, 68], [43, 67], [58, 48], [58, 27], [37, 69],
    [38, 46], [61, 33], [62, 63], [63, 69], [45, 35], [32, 39], [56, 37]
])

# Compute the distance matrix
dist_matrix = np.array([[euclidean(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))])

# Cluster cities without the depot
kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(coordinates[1:])
cluster_labels = kmeans.labels_

# Assign cities to robots
robot_tours = [[] for _ in range(num_robots)]
for city_idx, cluster_idx in enumerate(cluster_labels, start=1):
    robot_tours[cluster_idx].append(city_idx)

def solve_tsp(d_matrix):
    # Solve TSP using a naive nearest neighbor algorithm - can be replaced with more sophisticated methods
    n = len(d_matrix)
    visited = [False]*n
    tour = [0]  # start at the depot
    while len(tour) < n:
        last = tour[-1]
        next_city = min([(d_matrix[last][i], i) for i in range(n) if not visited[i] and i != last], default=(None, None))[1]
        if next_city is None:
            break
        visited[next_city] = True
        tour.append(next_city)
    tour.append(0)  # return to depot
    return tour

# Calculate tours and costs
overall_total_cost = 0
for i in range(num_robots):
    if robot_tours[i]:
        # Include the depot, solve TSP, and calculate tour cost
        local_tour = solve_tsp(dist_matrix[[0]+robot_tours[i]][:, [0]+robot_tours[i]])
        tour_cost = sum(dist_matrix[local_tour[j]][local_tour[j+1]] for j in range(len(local_tour)-1))
        overall_total_cost += tour_cost
        # Print results for this robot
        print(f"Robot {i} Tour: {[coordinates[idx] for idx in local_tour]}")
        print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Cost: {overall_total_cost:.2f}")