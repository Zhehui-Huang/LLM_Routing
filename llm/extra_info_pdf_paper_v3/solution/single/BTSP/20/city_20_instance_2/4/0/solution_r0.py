from math import sqrt

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
    x1, y1 = city1
    x2, y2 = city2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Brute-force solution for small problems - generate all permutations of city visits
from itertools import permutations

# Reduce the problem space by considering cities except the depot (city 0)
city_indices = list(cities.keys())[1:]

# Generate all possible tours
all_tours = permutations(city_indices)

# Initialize variables to track the best tour
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

# Evaluate each tour
for tour in all_tours:
    full_tour = [0] + list(tour) + [0]  # add the depot city to start and end
    tour_costs = []
    
    # Calculate the costs for this tour
    for i in range(len(full_tour) - 1):
        cost = euclidean_distance(cities[full_tour[i]], cities[full_tour[i+1]])
        tour_costs.append(cost)
    
    max_tour_cost = max(tour_costs)
    total_tour_cost = sum(tour_costs)
    
    # Update the best tour if it has the smallest maximum distance
    if max_tour_cost < best_max_distance or (max_tour_cost == best_max_distance and total_tour_cost < best_total_cost):
        best_tour = full_tour
        best_max_distance = max_tour_cost
        best_total?cost = total_tour_cost

# Display the best tour found
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))