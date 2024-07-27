import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
import random

# Coordinates of the cities including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Parameters
num_robots = 4

# Helper function to compute the Euclidean distance
def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Divide cities using K-Means clustering (simplified approach for FCM)
def cluster_cities(coordinates, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(coordinates)
    labels = kmeans.labels_
    clusters = {i: [] for i in range(num_clusters)}
    for i, label in enumerate(labels):
        clusters[label].append(i)
    return clusters

# Initializing robots tours via random greedy heuristic
def initialize_tours(clusters, num_robots):
    tours = {i: [0] for i in range(num_robots)}  # starting with the depot
    available_cities = set(range(1, len(coordinates)))  # city 0 is depot

    # Distribute cities to robots based on clusters
    for k, cities in clusters.items():
        for city in cities:
            if city in available_cities:
                chosen_robot = random.choice(list(range(num_robots)))
                tours[chosen_robot].append(city)
                available_cities.remove(city)
        
    # Ensure all robot tours end at the depot
    for i in range(num_robots):
        tours[i].append(0)
    
    return tours

# Calculate tour cost
def calculate_tour_cost(tour, coordinates):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return cost

# Execute ITSHA
clusters = cluster_cities(coordinates, num_robots)
tours = initialize_tours(clusters, num_robots)

# Calculate initial solution costs
costs = {robot: calculate_tour_cost(tours[robot], coordinates) for robot in range(num_robots)}

# Print results
max_cost = max(costs.values())
for robot, tour in tours.items():
    tour_cost = calculate_tour_cost(tour, coordinates)
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Process: Efficiency {tour_cost}")

print(f"Maximum Travel Cost: {max_cost}")