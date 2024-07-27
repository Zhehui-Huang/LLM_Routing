import math
from itertools import permutations

# Function to calculate euclidean distance between two cities using their coordinates
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of each city, with the depot city at index 0
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# Calculate distances between each pair of cities
n_cities = len(cities)
distances = [[0] * n_cities for _ in range(n_cities)]
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distances[i][j] = euclidean_valueistance(cities[i], cities[j])

# Function to find the tour with minimum maximum distance between consecutive cities (brute-force)
def find_min_bottleneck_tour():
    min_max_distance = float('inf')
    best_tour = None

    # Permute all cities except the depot to find the best tour
    for perm in permutations(range(1, n_cities)):
        # Adding the depot at the start and end of the tour
        tour = [0] + list(perm) + [0]
        
        # Compute the maximum distance and total cost of the tour
        max_distance = 0
        total_cost = 0
        for i in range(len(tour) - 1):
            dist = distances[tour[i]][tour[i + 1]]
            total_cost += dist
            if dist > max_distance:
                max_distance = dist
        
        # Update the best tour if a new minimum max distance is found
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
            best_total_cost = total_cost

    return best_tour, best_total_cost, min_max_distance

# Calculate the best tour using the function
best_tour, total_travel_cost, max_consecutive_distance = find_min_bottleneck_tour()

# Output results
print("Tour:", best_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)