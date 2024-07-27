import math

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tour_requirements(tour, total_travel_cost):
    """Check if the provided tour and cost meet the specified requirements."""
    cities = {
        0: (9, 93),
        1: (8, 51),
        2: (74, 99),
        3: (78, 50),
        4: (21, 23),
        5: (88, 59),
        6: (79, 77),
        7: (63, 23),
        8: (19, 76),
        9: (21, 38),
        10: (19, 65),
        11: (11, 40),
        12: (3, 21),
        13: (60, 55),
        14: (4, 39)
    }

    # [Requirement 1] Tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Tour should visit exactly 4 cities (including depot)
    if len(set(tour)) != 4:
        return "FAIL"

    # [Requirement 3 & 5] Compute the route cost and compare
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    # Check accuracy of the computed cost
    if not math.isclose(computed_cost, total_travel_cost, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Provided results
tour = [0, 1, 10, 8, 0]
total_travel_cost = 90.54

# Validate the solution against the requirements
result = check_tour_requirements(tour, total_travel_cost)
print(result)