import itertools
import math

# Define the city coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), 
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Calculate distances between all pairs of cities
num_cities = len(cities)
distances = [[distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Helper function to calculate the maximum distance in a tour
def max_distance_tour(tour):
    return max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Permutations of city indices, excluding the depot
city_indices = list(range(1, num_cities))

min_max_distance = float('inf')
best_tour = None

# Iterate over all permutations of city tours to find the optimal solution
for permutation in itertools.permutations(city_indices):
    tour = [0] + list(permutation) + [0]
    current_max_distance = max_distance_tour(tour)
    if current_max_distance < min_max_distance:
        min_max_date = current_max_distance
        min_max_distance = current_max_distance  # Correcting an error
        best_tour = tour

# Calculate the total travel cost of the optimal tour
total_cost = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))

# Provide the output
print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(min_max_distance, 2))