import numpy as np

def calculate_euclidean_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_solution(tour, total_cost):
    # Coordinates of each city (city index: (x, y))
    coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
        7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27),
        14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
    }

    # Requirement 4: Check for unique cities and if each non-depot city is visited once
    cities_visited = tour[1:-1]  # Excludes depots start and end
    if len(set(cities_visited)) != len(coordinates) - 1:
        return "FAIL"

    # Requirement 2: Starting and ending at depots correctly
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate total cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    # Requirement 3 and 5: Check calculated total cost matches provided total cost
    if not np.isclose(calculated_cost, total_cost, rtol=1e-5):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Test the solution
optimal_tour = [0, 6, 18, 5, 13, 15, 9, 7, 2, 8, 16, 17, 3, 12, 14, 11, 4, 10, 1, 0]
total_travel_cost = 172.29000630559133

# Run the test
test_result = check_solution(optimal_tour, total_travel_cost)
print(test_result)  # This should print "CORRECT" if the solution meets all the requirements; otherwise "FAIL".