import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define the coordinates of the cities
cities_coordinates = [
    (53, 68), (75, 11), (91, 95), (22, 80),
    (18, 63), (54, 91), (70, 14), (97, 44),
    (17, 69), (95, 89)
]

# Calculate distances between all pairs of cities
n = len(cities_coordinates)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities_coordinates[i], cities_coordinates[j])

# Brute force find the optimal tour minimizing the maximum distance between consecutive cities
min_max_distance = float('inf')
best_tour = None

for perm in permutations(range(1, n)):  # Exclude the depot city 0 for permutations
    current_tour = [0] + list(perm) + [0]  # Start and end at the depot city
    max_distance = max(distances[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour) - 1))
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = current_tour

# Calculate total travel cost based on best tour
total_travel_cost = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", min_max_distance)