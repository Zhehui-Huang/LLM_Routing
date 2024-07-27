import numpy as np
from sklearn.cluster import KMeans

# City coordinates with city index starting from Depot City 0
coordinates = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
])

# Function to calculate Euclidean Distance between two points
def euclidean_distance(point1, point2):
    return np.linalg.norm(point1 - point2)

# Step 1: Cluster cities excluding the depot using k-means
n_robots = 4
city_indices = np.arange(1, 22)  # Excluding Depot City 0
kmeans = KMeans(n_clusters=n_robots, random_state=0).fit(coordinates[1:])

# Step 2: Assign cities to robots based on clusters
clusters = {i: [0] for i in range(n_robots)}  # Initialize with depot city 0 in each tour
for idx, label in enumerate(kmeans.labels_):
    clusters[label].append(city_indices[idx])

def nearest_neighbor_tour(cities, coordinates):
    """ Construct a tour using the nearest neighbor heuristic starting from depot city 0 """
    unvisited = cities[1:]  # Excluding the depot at the beginning
    tour = [0]  # Start at depot
    current = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(coordinates[current], coordinates[city]))
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)

    tour.append(0)  # Return to depot
    return tour

def calculate_tour_cost(tour, coordinates):
    """ Calculate the total cost of a given tour """
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Step 3 & 4: Determine tours and calculate costs
overall_total_cost = 0
for robot_id in clusters:
    tour = nearest_neighbor_tour(clusters[robot_id], coordinates)
    tour_cost = calculate_tour_cost(tour, coordinates)
    overall_total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")