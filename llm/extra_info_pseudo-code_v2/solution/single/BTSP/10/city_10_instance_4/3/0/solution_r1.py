import math
from itertools import permutations

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define cities coordinates 
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Prepare distance matrix
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = calculate_distance(cities[i], cities[j])

# Searching for the best tour
best_tour = None
min_max_distance = float('inf')
total_distance = 0
for perm in permutations(range(1, num_cities)):
    tour = [0] + list(perm) + [0]
    max_dist_in_tour = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    tour_total_distance = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    if max_dist_in_tour < min_max_distance:
        min_max_distance = max_dist_in_tour
        best_tour = tour
        total_distance = tour_total_distance

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")