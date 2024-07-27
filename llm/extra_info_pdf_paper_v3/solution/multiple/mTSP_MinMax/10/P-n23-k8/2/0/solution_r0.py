import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
import random

# Data - City Coordinates excluding depot city
cities_coordinates = [
    (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), 
    (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), 
    (63, 69), (45, 35), (32, 39), (56, 37)
]
depot = (30, 40) # Depot city coordinates
cities_coordinates.insert(0, depot) # Inserting depot at index 0

num_cities = len(cities_coordinates)
num_robots = 8

# Function to calculate Euclidean distance matrix
def calculate_distance_matrix(coords):
    num_coords = len(coords)
    dist_matrix = np.zeros((num_coords, num_coords))
    for i in range(num_coords):
        for j in range(num_coords):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

# Perform clustering to create initial solutions
def cluster_cities(n_clusters, coords):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(coords)
    clusters = [[] for _ in range(n_clusters)]
    for idx, label in enumerate(kmeans.labels_):
        clusters[label].append(idx)
    return clusters

# Initialize tours from clusters
def generate_initial_tours(clusters):
    tours = [[] for _ in range(len(clusters))]
    for i, cluster in enumerate(clusters):
        # Include the depot as start and end point
        tours[i].append(0)
        tours[i].extend(cluster)
        tours[i].append(0)
    return tours

# Function to compute the total distance for a tour
def tour_distance(tour, dist_matrix):
    total_dist = 0
    for i in range(1, len(tour)):
        total_dist += dist_matrix[tour[i-1]][tour[i]]
    return total_dist

# Using VNS with 2-opt as a local search method
def apply_two_opt(tour, dist_matrix):
    best_distance = tour_distance(tour, dist_matrix)
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Skip adjacent edges
                new_tour = tour[:]
                new_tour[i:j] = tour[j-1:i-1:-1]
                new_distance = tour_distance(new_tour, dist_matrix)
                if new_distance < best_distance:
                    best_tour = new_tour[:]
                    best_distance = new_distance
                    improved = True
        tour = best_tour[:]
    return tour, best_distance

def main():
    # Step 1: Calculate distance matrix
    dist_matrix = calculate_distance_matrix(cities_coordinates)
    
    # Step 2: Cluster to form initial tours
    initial_clusters = cluster_cities(num_robots, cities_coordinates[1:]) # exclude depot for clustering
    tours = generate_initial_tours(initial_clusters)
    
    # Step 3: Optimize each tour using 2-opt
    optimized_tours = []
    max_travel_cost = 0
    for tour in tours:
        optimized_tour, travel_cost = apply_two_opt(tour, dist_matrix)
        optimized_tours.append((optimized_tour, travel_cost))
        max_travel_cost = max(max_travel_cost, travel_cost)
    
    # Output results
    for idx, (tour, cost) in enumerate(optimized_tours):
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {cost:.2f}\n")
    print(f"Maximum Travel Cost: {max_travel_cost:.2f}")

# Run the main function
main()