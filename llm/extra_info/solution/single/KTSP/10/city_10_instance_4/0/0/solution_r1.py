import itertools
import math

# Given city coordinates
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

# Calculating Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Computing the cost of the given tour
def compute_tour_cost(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i + 1])
    total_distance += distance(tour[-1], tour[0])  # Return to start
    return total_distance

# Generate all possible sets of 7 cities (excluding the depot city 0)
other_cities = list(cities.keys())[1:]
min_tour = None
min_tour_cost = float('inf')

# Iterate through combinations of selecting 7 cities
for cities_subset in itertools.combinations(other_cities, 7):
    current_tour = [0] + list(cities_subset) + [0]  # ensuring the tour starts and ends at the depot
    tour_cost = compute_tour_pcrost(current_tour)
    if tour_cost < min_tour_cost:
        min_tour_cost = tour_cost
        min_tour = current_tour

# Output the results
print("Tour:", min_tour)
print("Total travel cost:", min_tour_cost)