import math
import random
from itertools import permutations

# Euclidean distance function
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate total tour distance
def tour_cost(tour, cities):
    return sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def local_search(initial_tour, cities, iterations=1000):
    best_tour = initial_tour[:]
    best_cost = tour_cost(initial_tour, cities)
    for _ in range(iterations):
        new_tour = best_tour[:]
        # Swap two cities in the tour (excluding depot-0 index)
        i, j = random.sample(range(1, len(best_tour) - 1), 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        new_cost = tour_cost(new_tour, cities)
        if new_cost < best_cost:
            best_tour, best_cost = new_tour[:], new_cost
    return best_tour, best_cost

# Define cities coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), 
    (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), 
    (64, 30), (70, 95), (29, 64), (32, 79)
]

# Initialize parameters
num_cities_to_visit = 10

# Start at depot, choose 9 other cities to make total of 10 visited cities
all_possible_cities = list(range(1, 15))  # Exclude depot
best_overall_tour = None
best_overall_cost = float('inf')

# Try different initial subsets
for subset in permutations(all_possible_cities, num_cities_to_visit - 1):
    tour = [0] + list(subset) + [0]
    refined_tour, refined_cost = local_search(tour, cities, iterations=100)
    if refined_cost < best_overall_cost:
        best_overall_tour, best_overall_cost = refined_tour, refined_cost

# Output best found solution
print("Tour:", best_overall_tour)
print("Total travel cost:", best_overall_cost)