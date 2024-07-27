import math
import random

# Cities' coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate a distance matrix
def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = distance(cities[i], cities[j])
            else:
                dist_matrix[i][j] = float('inf')
    return dist_matrix

# Nearest neighbor heuristic for initial tour
def nearest_neighbor_tour(start_city, dist_matrix):
    n = len(dist_matrix)
    unvisited = set(range(n))
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # return to the start city
    return tour

# Function to calculate the total travel cost of a tour
def calculate_total_distance(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Placeholder for a potentially complex heuristic enhancement using Lin-Kernighan
def lin_kernighan_heuristic(tour, dist_matrix):
    # This is a highly simplified placeholder for demonstration
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+2, len(tour) - 1):
                if dist_matrix[tour[i-1]][tour[i]] + dist_matrix[tour[j-1]][tour[j]] > dist_matrix[tour[i-1]][tour[j-1]] + dist_matrix[tour[i]][tour[j]]:
                    tour[i:j] = reversed(tour[i:j])
                    improved = True
    return tour

# Calculate distances
distance_matrix = create_distance_matrix(cities)

# Get a tour using nearest neighbor and improve it with Lin-Kernighan
initial_tour = nearest_neighbor_tour(0, distance_matrix)
improved_tour = lin_kernighan_heuristic(initial_tour, distance_matrix)

# Calculate tour cost
tour_cost = calculate_total_distance(improved_tour, distance_matrix)

# Output results
print("Tour:", improved_tour)
print("Total travel cost:", tour_cost)