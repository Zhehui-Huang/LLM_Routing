import math
from itertools import permutations

# Define the coordinates for the cities
cities = [
    (79, 15),  # Depot
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Define groups of cities
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Compute the list of 'best' cities by choosing the closest city in each group to the depot
chosen_cities = []
for group in groups:
    closest_city = None
    min_dist = float('inf')
    for city_idx in group:
        dist = distance(cities[0], cities[city_idx])
        if dist < min_dist:
            closest_city = city_idx
            min_dist = dist
    chosen_cities.append(closest_city)

# Generate all permutations of the chosen cities (since the number of cities is small)
best_tour = None
best_cost = float('inf')

for perm in permutations(chosen_cities):
    # Calculate the tour cost for the permutation
    current_tour = [0] + list(perm) + [0]
    current_cost = 0

    for i in range(len(current_tour) - 1):
        current_cost += distance(cities[current_tour[i]], cities[current_tour[i+1]])
    
    if current_cost < best_cost:
        best_tour = current_tour
        best_cost = current_cost

# Output resulting tour and cost
print("Tour:", best_tour)
print("Total travel cost:", best_cost)