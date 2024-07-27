import numpy as np

def calculate_euclidean_distance(city_a, city_b):
    return np.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

def validate_tour(tour, total_cost):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Requirement 6
    
    if len(set(tour)) != 6:
        return "FAIL"  # Requirement 1
    
    if len(tour) != 6:
        return "FAIL"  # Requirement 1

    # City coordinates mapping from the task description
    city_coordinates = {
        0: (90, 3),
        1: (11, 17),
        2: (7, 27),
        3: (95, 81),
        4: (41, 54),
        5: (31, 35),
        6: (23, 95),
        7: (20, 56),
        8: (49, 29),
        9: (13, 17)
    }

    # Check for repeated city visits apart from the depot
    unique_cities = set(tour[1:-1])
    if len(unique_cities) + 1 != len(tour):
        return "FAIL"  # Requirement 4

    # Calculate and verify the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_index_a = tour[i]
        city_index_b = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(city_coordinates[city_index_a], city_coordinates[city_index_b])

    # Allow small numerical error margin
    if not np.isclose(calculated_cost, total_cost, rtol=1e-05):
        return "FAIL"  # Requirement 2

    return "CORRECT"

# Test case from the solution provided
tour = [0, 8, 5, 4, 0, 0]
total_travel_cost = 159.71833973069528

result = validate_tour(tour, total_travel_cost)

print(result)  # Output should be "CORRECT" if all requirements checked correctly and found valid