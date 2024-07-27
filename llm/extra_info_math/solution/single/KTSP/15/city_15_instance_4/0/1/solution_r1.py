import math
import numpy as np

# City coordinates provided
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Compute Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create a distance matrix
n = len(coordinates)
distance_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Nearest Neighbor Heuristic to find the TSP tour
def nearest_neighbor_tour(start_city, num_cities):
    remaining_cities = set(range(n))
    tour = [start_city]
    current_city = start_city
    remaining_cities.remove(current_city)

    while len(tour) < num_cities:
        next_city = min(remaining_cities, key=lambda city: distance_matrix[current_city, city])
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city

    # Close the tour by returning to the starting city
    tour.append(start_city)
    return tour

# Calculate the total travel cost of the tour
def calculate_tour_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i], tour[i+1]]
    return total_cost

# Generate the tour to visit exactly 12 cities starting and ending at city 0
tour = nearest_neighbor_tour(0, 12)
total_cost = calculate_tour_cost(tour, distance_matrix)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")