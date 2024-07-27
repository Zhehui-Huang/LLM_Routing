import itertools
import math

# Coordinates of cities including the depot city
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
          (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
          (83, 96), (60, 50), (98, 1)]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Generate all combinations of 5 cities (excluding the depot city) from the remaining 14 cities
city_indices = list(range(1, 15))
combinations = itertools.combinations(city_indices, 5)

# To store the minimum tour cost and corresponding tour
min_cost = float('inf')
best_tour = []

for combination in combinations:
    # Including the depot city at the start and end of the tour
    # All permutations of the cities in this combination
    for permutation in itertools.permutations(combination):
        # Create the entire tour
        tour = [0] + list(permutation) + [0]
        current_cost = sum([euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)])
        
        # Check if the current cost is less than the found minimum cost
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = tour

# Print the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)