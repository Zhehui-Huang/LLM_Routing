import math
import random
from itertools import permutations

# Define the cities with their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible combinations of 5 cities excluding the depot (0)
from itertools import combinations
city_combinations = list(combinations([i for i in cities.keys() if i != 0], 5))

# Function to find the shortest route for fixed subset of cities
def find_shortest_route(cities_subset):
    min_tour_length = float('inf')
    best_tour = None
    
    # Generate all permutations of the subset
    for perm in permutations(cities_subset):
        current_tour = [0] + list(perm) + [0]  # Start and end at the depot city 0
        current_length = sum(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
        
        if current_length < min_tour_length:
            min_tour_length = current_length
            best_tour = current_tour
            
    return best_tour, min_tour_length

# Search for the best combination of cities minimizing the tour length
best_overall_tour = None
best_overall_length = float('inf')

for subset in city_combinations:
    tour, tour_length = find_shortest_route(subset)
    
    if tour_length < best_overall_length:
        best_overall_length = tour_length
        best_overall_tour = tour

# Output the results
print("Tour:", best_overall_tour)
print("Total travel cost:", best_overall_length)