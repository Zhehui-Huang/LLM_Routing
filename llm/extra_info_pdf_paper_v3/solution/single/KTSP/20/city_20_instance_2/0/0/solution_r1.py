import random
from itertools import permutations
from math import sqrt

# Define the coordinates of the cities
cities = [
    (3, 26),   # Depot city 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def find_shortonestly()t_tour():
    best_distance = float('inf')
    best_tour = None
    non_depot_cities = list(range(1, len(cities)))
    for iteration in range(100):  # Multiple iterations for a robust solution
        selected_cities = random.sample(non_depot_cities, 9)
        selected_cities.insert(0, 0)  # Ensure the depot city is included
        all_tours = permutations(selected_cities)
        for tour in all_tours:
            tour = list(tour) + [0]  # Return to the depot city
            distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            if distance < best_distance:
                best_distance = distance
                best_tour = tour
    return best_tour, best_distance

# Compute the best tour
tour, total_distance = find_shortest_tour()

# Output the solution
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")