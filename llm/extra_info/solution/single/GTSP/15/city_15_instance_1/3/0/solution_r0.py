import itertools
import math

# Define a function to calculate the Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Define cities and their locations
cities = [
    (29, 51),  # Depot city 0
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

# Define city groups
city_groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Find the best tour visiting one city from each group
min_tour = None
min_cost = float('inf')

# Iterate over all combinations (one city from each group)
for combination in itertools.product(*city_groups):
    # Start with the depot city and construct the tour including the depot at the end
    tour = [0] + list(combination) + [0]
    # Calculate the total travel cost
    total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    
    # Update the minimum cost and tour if current is better
    if total_cost < min_cost:
        min_cost = total_cost
        min_tour = tour

# Print the results
print("Tour:", min_tour)
print("Total travel cost:", min_cost)