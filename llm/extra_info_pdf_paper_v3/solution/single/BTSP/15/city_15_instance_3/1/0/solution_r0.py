import math
import numpy as np

# Define the coordinates of each city
coordinates = [
    (16, 90),
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Step 1: Compute the Euclidean distance matrix
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

distance_matrix = np.array([
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))]
    for i in range(len(coordinates))
])

# Step 2: Heuristic - Nearest neighbor algorithm to get an initial tour
def nearest_neighbor_tour(start, distance_matrix):
    num_cities = len(distance_matrix)
    unvisited = set(range(num_cities))
    unvisited.remove(start)
    tour = [start]
    current_city = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
        
    tour.append(start)  # return to the depot
    return tour

# Step 3: Optimize to minimize the maximum distance between consecutive cities
def optimize_tour(tour, distance_matrix):
    improved = True
    best_tour = tour[:]
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if tour[i] != tour[j] and tour[i-1] != tour[j-1]:
                    new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                    if max_tour_distance(new_tour, distance_matrix) < max_tour_distance(best_tour, distance_matrix):
                        best_tour = new_tour[:]
                        improved = True
        tour = best_tour
    return best_tour

def sum_tour_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def max_tour_distance(tour, distance_matrix):
    return max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Compute the tour
initial_tour = nearest_neighbor_tour(0, distance_matrix)
optimized_tour = optimize_tour(initial_tour, distance_matrix)
total_cost = sum_tour_distance(optimized_tour, distance_matrix)
max_distance = max_tour_distance(optimized_tour, distance_matrix)

print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)