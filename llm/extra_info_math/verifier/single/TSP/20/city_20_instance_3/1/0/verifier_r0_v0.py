import math

# Given cities coordinates
cities_coordinates = [
    (30, 56),  # City 0: depot city
    (53, 42),  # City 1
    (1, 95),   # City 2
    (25, 61),  # City 3
    (69, 57),  # City 4
    (6, 58),   # City 5
    (12, 84),  # City 6
    (72, 77),  # City 7
    (98, 95),  # City 8
    (11, 0),   # City 9
    (61, 25),  # City 10
    (52, 0),   # City 11
    (60, 95),  # City 12
    (10, 94),  # City 13
    (96, 73),  # City 14
    (14, 47),  # City 15
    (18, 16),  # City 16
    (4, 43),   # City 17
    (53, 76),  # City 18
    (19, 72)   # City 19
]

# Provided tour and calculated cost
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 14, 8, 12, 18, 0]
provided_total_cost = 426.0

def euclidean_distance(city1, city2):
    x_distance = city1[0] - city2[0]
    y_distance = city1[1] - city2[1]
    return math.sqrt(x_distance**2 + y_distance**2)

def verify_tour(cities_coordinates, tour, provided_total_cost):
    # Verify start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify all other cities are visited exactly once
    visited_cities = set(tour)
    if len(visited_cities) != 20 or any(i not in visited_cities for i in range(20)):
        return "FAIL"

    # Verify the total travel cost
    calculated_cost = sum(euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]]) for i in range(len(tour)-1))
    if int(round(calculated_cost)) != int(provided_total_cost):
        return "FAIL"
    
    return "CORRECT"

# Output the test result
result = verify_tour(cities_coordinates, tour, provided_total_cost)
print(result)