import itertools
import math

# City Coordinates
depore = (50, 42)
cities_constant = [
    depore,  # City 0 (Depot)
    (41, 1),  # City 1
    (18, 46), # City 2
    (40, 98), # City 3
    (51, 69), # City 4
    (47, 39), # City 5
    (62, 26), # City 6
    (79, 31), # City 7
    (61, 90), # City 8
    (42, 49)  # City 9
]

# Groups of cities
groups = [
    [1, 2, 6], # Group 0
    [3, 7, 8], # Group 1
    [4, 5, 9]  # Group 2
]

# Calculate Euclidean distance function
def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# Generate all combinations of picking one city from each group
all_possible_tours = itertools.product(*groups)

# Calculate total distance for a given tour including starting and ending at the depot
def calculate_tour_cost(picked_cities_indices):
    full_tour = [0] + list(picked_cities_indices) + [0]  # starting and ending at depot
    total_cost = 0
    for i in range(len(full_tour) - 1):
        current_city_index = full_tour[i]
        next_city_index = full_tour[i+1]
        total_cost += euclidean_distance(cities_constant[current_city_index], 
                                          cities_constant[next_city_index])
    return total_cost

# Finding the minimum cost tour
min_cost = float('inf')
best_tour = []

for tour in all_possible_tours:
    cost = calculate_tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Preparing the output
complete_tour = [0] + list(best_tour) + [0]
print("Tour:", complete_tour)
print("Total travel cost:", min_cost)