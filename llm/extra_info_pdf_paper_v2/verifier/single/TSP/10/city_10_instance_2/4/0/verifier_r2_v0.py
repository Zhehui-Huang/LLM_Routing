import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, total_travel_cost):
    # Test cities and their coordinates
    cities = {
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

    # [Requirement 1] Check if tour starts and ends at the depot
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # [Requirement 2] Check if all cities except depot are visited once
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(cities) - 1 or any(city not in unique_cities for city in cities if city != 0):
        return "FAIL"

    # [Requirement 3] Calculate the tour cost and check against the given total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"

    # [Requirement 4 & 5] Check tour format as list starting and ending at depot and if total cost is correct
    if not isinstance(tour, list) or not all(isinstance(city, int) for city in tour):
        return "FAIL"

    return "CORRECT"

# Given solution to test
tour = [0, 8, 9, 1, 2, 5, 4, 7, 6, 3, 0]
total_travel_cost = 279.59

# Validate the solution
result = validate_tour(tour, total_travel_cost)
print(result)