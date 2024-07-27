import math

def calculate_euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def verify_tour(tour, cities):
    # Check start and end at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check that every city except deposition appears exactly once
    visited = set(tour)
    if len(visited) != len(cities) or any(i not in visited for i in range(len(cities))):
        return "FAIL"
    
    # Check if the calculated distance matches the claimed total travel cost
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Rounding to two decimal places for comparison
    total_calculated_cost = round(total_calculated_cost, 2)
    if total_calculated_cost != 376.93:  # Check against given total cost
        return "FAIL"
    
    return "CORRECT"

# Coordinates for each city including the depot
cities_coordinates = [
    (14, 77),
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9)
]

# The suggested tour and total travel cost
suggested_tour = [0, 1, 13, 12, 2, 9, 6, 0, 3, 14, 5, 7, 4, 10, 11, 16, 17, 19, 15, 18, 8, 0]
result = verify_tour(suggested_tour, cities_coordinates)
print(result)