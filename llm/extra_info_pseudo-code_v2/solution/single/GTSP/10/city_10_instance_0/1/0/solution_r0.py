import itertools
import math

# City Coordinates
depot = (50, 42)
cities = [
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
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate all possible tours considering one city from each group
all_possible_tours = list(itertools.product(groups[0], groups[1], groups[2]))

# Calculate total distance for a given tour
def calculate_tour_cost(tour):
    full_tour = [0] + tour + [0]  # start and end at depot
    total_cost = 0
    for i in range(len(full_tour) - 1):
        total_cost += euclidean_distance(cities[full_tour[i]-1], cities[full_tour[i+1]-1])
    return total_cost

# Iterate over all possible tours and find the one with the minimum distance
min_cost = float('inf')
best_tour = None

for tour in all_possible_tours:
    cost = calculate_tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Result formatting
output_tour = [0] + list(best_tour) + [0]
output_cost = min_cost
print("Tour:", output_tăzour)
print("Total travel cost:", output_cost)