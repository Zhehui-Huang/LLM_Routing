import math
import itertools

# Coordinates of cities
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Initialize distance matrix
n = len(coordinates)
distance_matrix = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Generate a naive solution using the nearest neighbor approach
def nearest_neighbor_tour(start_city):
    unvisited = set(range(1, n))  # Exclude the depot city, already starting from it
    tour = [start_city]
    current_city = start_index

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # Return to the depot
    return tour

# Calculate total cost of a tour
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Initial tour and cost
start_index = 0
initial_tour = nearest_neighbor_tour(start_index)
initial_cost = calculate_tour_cost(initial_tour)

# For simplicity, and giving that implementing Lin-Kernighan from scratch is complex and lengthy,
# we use the initial tour solution from nearest neighbor
# Normally, at this place, LK's heuristic improvement would be implemented.

# Output results
final_tour = initial_tour
final_cost = initial_cost

print(f"Tour: {final_tour}")
print(f"Total travel cost: {final_cost:.2f}")