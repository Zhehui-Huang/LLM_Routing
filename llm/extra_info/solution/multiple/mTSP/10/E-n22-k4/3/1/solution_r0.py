import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans

# Define coordinates of depot city and other cities
coordinates = np.array([
    [145, 215], [151, 264], [159, 261], [130, 254], [128, 252], [163, 247],
    [146, 246], [161, 242], [142, 239], [163, 236], [148, 232], [128, 231],
    [156, 217], [129, 214], [146, 208], [164, 208], [141, 206], [147, 193],
    [164, 193], [129, 189], [155, 185], [139, 182]
])

# Calculate the distance matrix between cities
distances = distance_matrix(coordinates, coordinates)

# Function to calculate tour cost
def calculate_tour_cost(tour):
    return sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Using KMeans to divide cities into clusters for each robot
kmeans = KMeans(n_clusters=4, random_state=0).fit(coordinates[1:])
clusters = kmeans.labels_

# Creating routes for each robot
robots_routes = [[] for _ in range(4)]
for city_index, cluster_index in enumerate(clusters):
    robots_routes[cluster_index].append(city_index + 1)

# Function to build a simple round trip tour
def create_tour(route):
    return [0] + route + [0]

# Creating final routes and calculating costs
total_cost = 0
for i in range(len(robots_routes)):
    tour = create_tour(robots_routes[i])
    tour_cost = calculate_tour_cost(tour)
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {round(tour_cost, 2)}")

print(f"Overall Total Travel Cost: {round(total_cost, 2)}")