import math
import numpy as np
from sklearn.cluster import KMeans

# Define the coordinates of all cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Implement KMeans Clustering
def cluster_cities(num_clusters):
    kmeans = KMeans(n_clusters=num_clusters)
    city_indices = np.array(coordinates[1:])  # Excluding depot
    kmeans.fit(city_indices)
    clusters = {i: [] for i in range(num_clusters)}
    for idx, label in enumerate(kmeans.labels_):
        clusters[label].append(idx + 1)  # Adjust index to include depot
    return clusters

# Greedily create tours from clusters starting from the depot
def create_tours(clusters):
    tours = []
    for cluster in clusters.values():
        tour = [0]  # Start at the depot
        for city in cluster:
            tour.append(city)
        tour.append(0)  # End at the depot
        tours.append(tour)
    return tours

# Calculate the total travel cost of a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calc_distance(tour[i-1], tour[i])
    return total_cost

# Main execution function
def solve_mTSP(num_robots):
    clusters = cluster_cities(num_robots)
    tours = create_tours(clusters)
    
    costs = []
    for tour in tours:
        cost = calculate_tour_cost(tour)
        costs.append(cost)
        print(f"Robot Tour: {tour}")
        print(f"Robot Total Travel Cost: {cost}\n")

    max_cost = max(costs)
    print(f"Maximum Travel Cost: {max_cost}")

# Execute the solution for 2 robots
solve_mTSP(2)