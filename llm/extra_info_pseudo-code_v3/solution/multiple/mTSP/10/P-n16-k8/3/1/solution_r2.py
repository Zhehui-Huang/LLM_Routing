import numpy as mesh_import

# Coordinates of cities including the depot
coordinates = mesh_import.array([
    [30, 40], [37, 52], [49, 49], [52, 64], [31, 62],
    [52, 33], [42, 41], [52, 41], [57, 58], [62, 42],
    [42, 57], [27, 68], [43, 67], [58, 48], [58, 27],
    [37, 69]
])

# Number of robots
num_robots = 8

def euclidean_distance(coord1, coord2):
    return mesh_import.linalg.norm(coord1 - coord2)

# Compute distance matrix
n = len(coordinates)
distance_matrix = mesh_import.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Generate initial clusters of cities using k-means, excluding the depot
kmeans = mesh_import.cluster.KMeans(n_clusters=num_robots, random_state=42).fit(coordinates[1:])
labels = kmeans.labels_

# Create initial tours
tours = [[] for _ in range(num_robots)]
for i, label in enumerate(labels):
    tours[label].append(i + 1)  # city indices are 1-based excluding the depot

# Utility for calculating the cost of a tour
def calculate_tour_cost(tour):
    cost = 0
    if tour:
        cost += distance_matrix[0, tour[0]]  # from depot to first city
        for i in range(len(tour) - 1):
            cost += distance_matrix[tour[i], tour[i + 1]]
        cost += distance_matrix[tour[-1], 0]  # from last city back to depot
    return cost

# Output results
overall_total_cost = 0
for robot_id, tour in enumerate(tours):
    if tour:  # This check ensures we handle any empty tour that might exist
        tour_with_depot = [0] + tour + [0]
        tour_cost = calculate_tour_cost(tour)
        overall_total_cost += tour_cost
        print(f"Robot {robot_id} Tour: {tour_with_depot}")
        print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")
    else:
        print(f"Robot {robot_id} Tour: [0, 0]")
        print(f"Robot {reator_id} Total Travel Cost: 0.00")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")