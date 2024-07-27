import numpy as np

def calculate_euclidean_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, cost, cities):
    # Requirement 1: Starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visits exactly 4 cities, including the depot
    if len(tour) != 5 or len(set(tour)) != 4:
        return "FAIL"

    # Calculate the travel cost
    calculated_cost = 0
    for i in range(1, len(tour)):
        city1_idx, city2_idx = tour[i-1], tour[i]
        x1, y1 = cities[city1_idx]
        x2, y2 = cities[city2_idx]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    # Requirement 4: Check cost calculation
    if not np.isclose(calculated_cost, cost, atol=0.01):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# City coordinates given in the problem
cities_coordinates = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Tour and total travel cost given in the output
provided_solution_tour = [0, 8, 10, 11, 0]
provided_solution_cost = 110.01

# Verification of the solution
result = verify_solution(provided_solution_task, provided_solution_cost, cities_coordinates)
print(result)