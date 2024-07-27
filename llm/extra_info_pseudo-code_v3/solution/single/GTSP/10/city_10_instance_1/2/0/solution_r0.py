import math
from itertools import product

# defining the coordinates of the cities
city_coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# defining city groups
city_groups = [
    [5, 6, 7], # Group 0
    [2, 3],    # Group 1
    [1, 9],    # Group 2
    [4, 8]     # Group 3
]

# function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# function to compute the total cost of a given tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i+1])
    return total_cost

# finding the optimal tour
best_tour = None
minimum_cost = float('inf')

# iterate over all combinations (one city from each group)
for combination in product(city_groups[0], city_groups[1], city_groups[2], city_groups[3]):
    # build the full tour: start at depot, visit one city from each group, and return to depot
    tour = [0] + list(combination) + [0]
    current_cost = tour_cost(tour)
    
    # check if the current tour is better than what we have found before
    if current_cost < minimum_cost:
        best_tour = tour
        minimum_cost = current_cost

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", round(minimum_cost, 2))