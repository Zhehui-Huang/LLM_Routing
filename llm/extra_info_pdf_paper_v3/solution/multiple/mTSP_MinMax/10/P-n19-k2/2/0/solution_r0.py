import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# Coordinates of the cities including the depot
coordinates = np.array([
    [30, 40], [37, 52], [49, 43], [52, 64], [31, 62],
    [52, 33], [42, 41], [52, 41], [57, 58], [62, 42],
    [42, 57], [27, 68], [43, 67], [58, 27], [37, 69],
    [61, 33], [62, 63], [63, 69], [45, 35]
])

# Number of robots
num_robots = 2

# Clustering using K-means
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])  # exclude depot
clusters = kmeans.labels_

# Utilize a basic 2-opt algorithm for path optimization
def two_opt(route, distance_matrix):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if sum(distance_matrix[best[k]][best[k + 1]] for k in range(len(best) - 1)) > sum(distance_matrix[new_route[k]][new_route[k + 1]] for k in range(len(new_route) - 1)):
                    best = new_route
                    improved = True
        route = best
    return best

# Generating the tours and calculating costs
tours = []
costs = []

# Distance matrix
distance_matrix = [[euclidean(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

for robot in range(num_robots):
    indices = np.where(clusters == robot)[0] + 1  # shift indices because depot was excluded
    tour = [0] + list(indices) + [0]  # from depot and back to depot
    optimized_tour = two_opt(tour, distance_matrix)
    tours.append(optimized_tour)
    cost = sum(distance_matrix[optimized_tour[i]][optimized_tour[i+1]] for i in range(len(optimized_tour)-1))
    costs.append(cost)

# Calculate max travel cost
max_cost = max(costs)

# Print output
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")