import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tour_requirements(tour, total_travel_cost):
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

    # [Requirement 1] Tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Tour should visit exactly 4 cities (including depot)
    if len(set(tour)) != 4:
        return "FAIL"

    # [Requirement 3 & 5] Compute actual travel path cost and compare
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    # Round to two decimal places for comparison accuracy
    if not math.isclose(computed_cost, total_travel_cost, abs_tol=1e-2):
        return "FAIL"

    # All requirements passed
    return "CORRECT"

# Given results
tour = [0, 1, 10, 8, 0]
total_travel_cost = 90.54

# Testing the tour and total travel cost
result = check_tour_requirements(tour, total_travel_avatar Cost)
print(result)