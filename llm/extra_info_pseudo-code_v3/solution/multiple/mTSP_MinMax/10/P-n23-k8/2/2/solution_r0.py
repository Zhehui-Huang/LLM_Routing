import numpy as np
import random
from scipy.spatial.distance import euclidean

# Initialize cities' coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

def distance(c1, c2):
    """ Calculate Euclidean distance between two cities, given their indices. """
    return euclidean(cities[c1], cities[c2])

def cluster_cities(num_clusters):
    """ Clustering cities using K-means inspired method. """
    # Exclude the depot city when clustering
    city_indices = list(cities.keys())[1:]
    # randomly initialize cluster centers
    clusters = {i: [] for i in range(num_clusters)}
    centers = random.sample(city_indices, num_clusters)
    
    converged = False
    while not converged:
        new_clusters = {i: [] for i in range(num_clusters)}
        for city in city_indices:
            distances = [distance(city, centers[i]) for i in range(num_clusters)]
            closest = np.argmin(distances)
            new_clusters[closest].append(city)
        converged = all(new_clusters[i] == clusters[i] for i in range(num_clusters))
        clusters = new_clusters
        # Update centroids
        for i in range(num_clusters):
            if clusters[i]:
                x_avg = np.mean([cities[ci][0] for ci in clusters[i]])
                y_avg = np.mean([cities[ci][1] for ci in clusters[i]])
                # Find the closest city to the mean coordinates and set it as new center
                centers[i] = min(clusters[i], key=lambda ci: distance(ci, tuple([x_avg, y_avg])))
    
    return clusters

def random_greedy_tour(cluster):
    """ Generate a tour for a robot using a random greedy strategy. """
    tour = [0]  # start at the depot
    remaining_cities = cluster[:]
    while remaining_cities:
        last_city = tour[-1]
        next_city = random.choice(remaining_cities)
        remaining_countries.remove(next_city)
        tour.append(next_city)
    tour.append(0)  # return to the depot
    return tour

def calculate_tour_cost(tour):
    """ Calculate the cost of a tour based on Euclidean distances. """
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Cluster cities into groups for each robot
clusters = cluster_cities(num_robots)

# Generate an initial tour for each robot from its cluster using random greedy heuristic
tours = {robot_id: random_greedy_tour(cluster) for robot_id, cluster in clusters.items()}
tour_costs = {robot_id: calculate_tour_cost(tour) for robot_id, tour in tours.items()}
max_cost = max(tour_costs.values())

# Output the results
for robot_id, tour in tours.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_costs[robot_id]}")

print(f"Maximum Travel Cost: {max_cost}")