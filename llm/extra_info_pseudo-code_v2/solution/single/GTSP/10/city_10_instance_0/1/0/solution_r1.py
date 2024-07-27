import itertools
import math

# City Coordinates
depot = (50, 42)
cities = {
    1: (41, 1),  # City 1
    2: (18, 46), # City 2
    3: (40, 98), # City 3
    4: (51, 69), # City 4
    5: (47, 39), # City 5
    6: (62, 26), # City 6
    7: (79, 31), # City 7
    8: (61, 90), # City 8
    9: (42, 49)  # City 9
}

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
    # Start and end at depot
    full_tour = [0] + list(tour) + [0]
    total_cost = 0
    current_location = depot
    for index in full_tour:
        if index == 0:
            next_location = depot
        else:
            next_location = cities[index]
        total_cost += euclidean_distance(current_location, next_location)
        current_location = next_current_location
    return total_cost

# Determine the tour with the minimum cost
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

print("Tour:", output_tour)
print("Total travel cost:", output_cost)