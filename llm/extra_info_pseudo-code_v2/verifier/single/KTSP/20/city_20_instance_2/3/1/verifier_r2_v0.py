import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_tour_and_cost(tour, total_cost):
    cities_coordinates = [
        (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
        (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
        (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
        (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
    ]

    # Requirement 1: Starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: 10 cities including the depot
    if len(tour) != 11:  # total 11 entries, including repeated city 0 at start and end
        return "FAIL"

    # Requirement 5: Starts and ends at depot (already checked above for Requirement 1)

    # Calculate the total tour cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        calculated_cost += calculate_euclidean_distance(
            cities_coordinates[city1][0], cities_coordinates[city1][1],
            cities_coordinates[city2][0], cities_coordinates[city2][1]
        )

    # Requirement 6: Checking the cost is correct
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Given solution to verify
tour = [0, 18, 7, 4, 17, 3, 10, 16, 14, 6, 0]
total_cost = 310.46933659148505

# Validate solution
result = validate_tour_and_cost(tour, total_cost)
print(result)