import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, total_cost):
    cities = [
        (3, 26),  # Depot
        (85, 72),
        (67, 0),
        (50, 99),
        (61, 89),
        (91, 56),
        (2, 65),
        (38, 68),
        (3, 92),
        (59, 8),
        (30, 88),
        (30, 53),
        (11, 14),
        (52, 49),
        (18, 49),
        (64, 41),
        (28, 49),
        (91, 94),
        (51, 58),
        (30, 48)
    ]

    # [Requirement 1] Check if tour starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Check if tour includes exactly 10 distinct cities including depot
    if len(set(tour)) != 10:
        return "FAIL"
    
    # [Requirement 3] Verify total travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    # [Requirement 5] Check the output format implicitly by input type and the above checks
    return "CORRECT"

# Given solution
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 0]
total_cost = 187.05

# Verify the provided solution
result = verify_tour(tour, total_cost)
print(result)