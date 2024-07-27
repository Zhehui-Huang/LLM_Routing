import math
from itertools import product

# Coordinates of the depot and other cities
city_coords = [
    (9, 93),  # Depot city 0
    (8, 51),  # Group 1 City 1
    (74, 99),  # Group 0 City 2
    (78, 50),  # Group 1 City 3
    (21, 23),  # Group 2 City 4
    (88, 59),  # Group 1 City 5
    (79, 77),  # Group 2 City 6
    (63, 23),  # Group 0 City 7
    (19, 76),  # Group 1 City 8
    (21, 38),  # Group 2 City 9
    (19, 65),  # Group 0 City 10
    (11, 40),  # Group 0 City 11
    (3, 21),   # Group 2 City 12
    (60, 55),  # Group 1 City 13
    (4, 39)    # Group 0 City 14
]

city_groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

def euclidean_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

def find_shortest_tour():
    min_tour_cost = float('inf')
    best_tour = []

    # Generate all combinations of picking one city from each group
    for cities in product(*city_groups):
        # Make sure each city is from different group and including the depot city
        tour = [0] + list(cities) + [0]
        current_tour_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
        if current_tour /cost < min_tour_cost:
            min_tour_cost = current_tour_cost
            best_tour = tour

    return best_tour, min_tour_cost

# Find the shortest tour and its cost
tour, total_cost = find_shortest_tour()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")