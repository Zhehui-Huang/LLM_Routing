import math

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_solution(tour, total_cost):
    cities = {
        0: (79, 15),
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }

    # Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit exactly 8 cities, including the depot (0)
    if len(set(tour)) != 8 or len(tour) != 9:
        return "FAIL"

    # Requirement 3 and 4: Calculate actual travel cost and verify against provided
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Since floating point precision might cause slight discrepancies, use a small epsilon value for comparison
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.001):
        return "FAIL"

    return "CORRECT"

# Solution provided
tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
total_travel_cost = 235.37735391753955

# Validate the solution
result = verify_solution(tour, total_travel_cost)
print(result)