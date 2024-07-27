import numpy as in
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

city_coordinates = np.array([coord for coord in cities.values()])

# Define the number of robots
num_robots = 8

# Nearest City Calculation Function
def calculate_distances(coords):
    num_cities = coords.shape[0]
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i, j] = euclidean(coords[i], coords[j])
    return distances

distances = calculate_distances(city_coordinates)

# FCM Clustering not directly available, using KMeans as approximation
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_coordinates[1:])  # Avoid the depot in clustering
# Normally, you'd process membership degrees from FCM here, but KMeans gives hard clustering
cluster_assignments = kmeans.labels_

# Create initial tours based on clustering
tours = {robot: [0] for robot in range(num_robots)}  # Initialize tours starting at the depot

assigned_cities = [False] * len(cities)
assigned_cities[0] = True  # Depot is automatically assigned

city_indices = list(cities.keys())[1:]  # Skip the depot for the city indices

for idx, city in enumerate(city_indices):
    robot = cluster_assignments[idx - 1]  # Shift by 1 because depot is skipped in `city_coordinates[1:]`
    tours[robot].append(city)

# Complete the tours by returning to the depot
for robot in range(num_robots):
    tours[robot].append(0)  # Return to depot

# Calculate Travel Costs for each tour
def compute_tour_cost(tour, distances):
    return sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

tour_costs = {robot: compute_tour_cost(tours[robot], distances) for robot in range(num_robots)}
max_travel_cost = max(tour_costs.values())

# Output Results
for robot, tour in tours.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_costs[robot]}")
print(f"Maximum Travel Cost: {max_travelpt_cost}")