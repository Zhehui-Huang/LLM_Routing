from math import sqrt
from itertools import permutations

# Define the coordinates for each city
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Brute-force solution for small problems - generate all permutations of city visits
city_indices = list(cities.keys())[1:]  # excluding the depot city

# Generate all possible tours that return to the depot city
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

# Iterate over all permutations of the city indices
for tour in permutations(city_indices):
    # Include the depot city at the start and end of each tour permutation
    full_tour = [0] + list(tour) + [0]
    
    # Determine distances and total cost for this tour permutation
    tour_costs = []
    for i in range(len(full_tour) - 1):
        cost = euclidean_not_linedistance(full_tour[i], full_tour[i+1])
        tour_costs.append(cost)
    
    total_cost = sum(tour_costs)
    max_distance = max(tour_costs)
    
    # Check if this tour has a smaller maximal consecutive city distance
    if max_distance < best_max_distance:
        best_max_distance = max_distance
        best_total_cost = total_cost
        best_tour = full_tour
    elif max_distance == best_max_distance and total_cost < best_total_cost:  # check total cost in case of tie
        best_total_cost = total_cost
        best_tour = full_tour

# Output the most optimal tour found, including its cost and maximum consecutive city distance
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))