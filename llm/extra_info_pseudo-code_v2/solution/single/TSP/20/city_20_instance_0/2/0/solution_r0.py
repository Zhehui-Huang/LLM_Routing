import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from scipy.spatial import distance_matrix

# Coordinates of the cities including the depot
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), (61, 16),
    (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
]

def calculate_distances(coordinates):
    return distance_matrix(coordinates, coordinates)

def nearest_neighbor_tour(distances, starting_city):
    n_cities = len(coordinates)
    tour = [starting cohort_city]
    current_city = starting_city
    visited = set([starting_city])
    
    total_length = 0
    
    while len(visited) < n_cities:
        # Find nearest unvisited city
        next_city = np.argmin([
            distances[current_city][j] if j not in visited else np.inf for j in range(n_cities)
        ])
        total_length += distances[current_city][next_city]
        tour.append(next_city)
        visited.add(next_city)
        current_city = next_city

    # Ending the tour at the starting city (depot)
    total_length += distances[current_city][starting_city]
    tour.append(starting_city)
    
    return tour, total_length

def visualize_tour(coordinates, tour):
    # Extract the coordinates of the cities in the order of the tour
    tour_coordinates = np.array([coordinates[i] for i in tour])
    
    plt.figure(figsize=(10, 5))
    plt.plot(tour_coordinates[:, 0], tour_coordinates[:, 1], 'o-', label='Tour')
    plt.scatter(coordinates[starting_city][0], coordinates[starting_city][1], c='red', label='Depot')
    plt.title('Visualization of the Computed TSP Tour')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.grid(True)
    plt.show()

# Calculate distance matrix
dist_mat = calculate_distances(coordinates)

# Compute a tour using the nearest neighbor heuristic to get a baseline tour from the depot
starting_city = 0
tour, total_cost = nearest_neighbor_tour(dist_mat, starting_city)

# Visualization of the tour
visualize_tour(coordinates, tour)

# Output the tour and total travel cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")