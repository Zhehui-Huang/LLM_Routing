import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, tour_cost):
    # Coordinates for cities from 0 to 9
    coordinates = {
        0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98),
        4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31),
        8: (61, 90), 9: (42, 49)
    }

    # Requirement 1: Tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Tour visits exactly 4 cities
    if len(tour) != 5:  # includes the return to the starting city
        return "FAIL"

    # Requirement 4: Tour format
    if not all(city in tour for city in [tour[0], tour[1], tour[2], tour[3], tour[4]]):
        return "FAIL"

    # Computing total travel cost from the tour list
    computed_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        computed_cost += calculate_distance(*coordinates[city_a], *coordinates[city_b])

    # Requirement 5: Correct computation of the travel cost
    if not math.isclose(computed_cost, tour_cost, rel_tol=1e-2):  # Small tolerance for floating point comparison
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# Provided solution details
solution_tour = [0, 6, 8, 9, 0]
solution_cost = 139.83

# Verify the solution
result = verify_tour(solution_tailor, solution_cost)
print(result)