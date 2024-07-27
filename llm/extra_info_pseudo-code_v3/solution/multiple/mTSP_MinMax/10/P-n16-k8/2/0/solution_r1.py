import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

city_coordinates = np.array(list(cities.values()))

# Define the number of robots
num_robots = 8

# Calculate distances
def calculate_distances(coords):
    num_cities = coords.shape[0]
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i, j] = euclidean(coords[i], coords[j])
    return distances

distances = calculate_distances(city_coordinates)

# Clustering: KMeans is used due to unavailability of FCM
# Exclude the depot in initial clustering; `+1` to realign indices
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_coordinates[1:])
cluster_assignments = kmeans.labels_

# Create initial tours based on clustering
tours = {robot: [0] for robot in range(num_robots)}

# Organize cities into robots’ tours
for city_idx, cluster_id in enumerate(cluster_assignments, start=1):
    tours[cluster_id].append(city_idx)

# Ensure the robots return to the depot
for tour in tours.values():
    tour.append(0)

# Computing travel costs
def compute_tour_cost(tour, distances):
    return sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

tour_costs = {robot: compute_tour_cost(tours[robot], distances) for robot in tours}
max_travel_cost = max(tour_costs.values())

# Output the results
for robot, tour in tours.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_costs[robot]}")

print(f"Maximum Travel Travel Cost: {max_travel_cost}")