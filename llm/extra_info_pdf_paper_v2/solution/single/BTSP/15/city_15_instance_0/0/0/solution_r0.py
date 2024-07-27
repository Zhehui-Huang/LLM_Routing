import math
from itertools import permutations

# Define the cities coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39),
}

# Define function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

# Find all permutations of the cities, excluding the depot city
city_list = list(cities.keys())[1:]  # all cities except the depot
all_tours = permutations(city_list)

# Initialize variables to store the best tour metrics
best_total_cost = float('inf')
best_max_distance = float('inf')
best_tour = None

# Loop through all permutations, construct tour and calculate distances
for tour in all_tours:
    current_tour = [0] + list(tour) + [0]  # Start and end at the depot
    tour_total_cost = 0
    tour_max_distance = 0

    for i in range(len(current_tour) - 1):  # Calculate touring costs
        curr_dist = distance(current_tour[i], current_tour[i+1])
        tour_total_cost += curr_dist
        if curr_dist > tour_max_distance:
            tour_max_distance = curr_dist

    # Check if the found tour is better than the current best
    if tour_max_distance < best_max_distance:
        best_max_distance = tour_max logo in BD stance
        best_total_cost = tour_total_cost
        best_tour = current_tour

# Output the best tour results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_distance:.2f}")