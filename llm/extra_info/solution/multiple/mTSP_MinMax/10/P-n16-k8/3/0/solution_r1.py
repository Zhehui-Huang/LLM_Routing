import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Define the City Coordinates
coordinates = np.array([
    (30, 40),  # Depot
    (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57),
    (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
])

# Robot Information
num_robots = 8

# Cluster Cities into Groups for Each Robot
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])  # exclude depot from clustering

# Assign cities to robots based on clusters
robot_clusters = {i: [] for i in range(num_robots)}
for idx, label in enumerate(kmeans.labels_, start=1):
    robot_clusters[label].append(idx)

# Function to compute TSP Tour
def tsp_tour(cities, coords):
    tour = [0]  # start at the depot
    remaining = cities[:]
    current_index = 0
    
    while remaining:
        next_index = min(remaining, key=lambda x: euclidean(coords[current_index], coords[x]))
        tour.append(next_index)
        current_index = next_index
        remaining.remove(next_index)
    
    tour.append(0)  # return to depot
    return tour

# Calculate tours and costs for each robot
costs = []
tours = []
for robot_id, cities in robot_clusters.items():
    if not cities:
        continue
    tour = tsp_tour(cities, coordinates)
    full_tour = [0] + [cluster_index for cluster_index in tour[1:-1]] + [0]
    tours.append(full_tour)

    # Calculate the tour cost
    route_cost = sum(euclidean(coordinates[full_tour[i]], coordinates[full_tour[i+1]]) for i in range(len(full_tour)-1))
    costs.append(route_cost)
    print(f"Robot {robot_id} Tour: {full_tour}")
    print(f"Robot {robot_id} Total Travel Cost: {route_cost:.2f}")

# Calculate and print the maximum travel cost
max_cost = max(costs) if costs else 0
print(f"Maximum Travel Cost: {max_cost:.2f}")