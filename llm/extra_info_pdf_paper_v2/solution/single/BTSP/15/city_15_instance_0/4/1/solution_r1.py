import math
from itertools import permutations

# Coordinate of cities including the starting city (depop)
coordinates = [
    (9, 93),   # City 0 - Depot
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate the total cost of a tour
def total_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Calculate maximum distance between consecutive cities in a tour
def max_distance(tour):
    return max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Brute force method to find the optimal tour
def find_best_tour():
    best_tour = None
    min_max_distance = float('inf')
    # Generate all permutations of city indices, except for the depot (0)
    all_tours = permutations(range(1, len(coordinates)))
    
    for tour in all_tours:
        # Complete tour by adding the depot at start and end
        full_tour = (0,) + tour + (0,)
        current_max_distance = max_distance(full_tour)
        if current_max_distance < min_max_distance:
            min_max_distance = current_max_distance
            best_tour = full_tour

    if best_tour:
        total_travel_cost = total_cost(best_tour)
        return best_tour, total_travel_cost, min_max_distance
    else:
        return None

# Execute the function and print the results
best_tour, total_travel_cost, min_max_distance = find_best_tour()
print("Tour:", list(best_tour))
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", min_max_distance)