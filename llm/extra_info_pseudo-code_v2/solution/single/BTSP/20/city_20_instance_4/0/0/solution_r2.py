import math

# Coordinates for the cities including the depot city
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# Number of cities (including the depot city)
num_cities = len(coordinates)

# Create a distance matrix
distance_matrix = [[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Simple greedy approach to find an initial solution for the TSP
def greedy_tsp(start):
    unvisited = set(range(num_cities))
    tour = [start]
    unvisited.remove(start)
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda city: distance_matrix[last][city])
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start)  # returning to the starting/depot city
    return tour

# Construct a tour with the greedy method
tour = greedy_tsp(0)

# Calculate the total travel cost and the maximum distance between consecutive cities
total_travel_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the tour, total travel cost, and max distance between consecutive cities
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travelv_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")