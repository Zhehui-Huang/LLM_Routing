import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, max_distance):
    cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), 
              (23, 95), (20, 56), (49, 29), (13, 17)]

    # [Requirement 1]
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # [Requirement 2]
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != 9 or set(range(1, 10)) != unique_cities:
        return "FAIL"

    # [Requirement 5]
    if len(tour) != 12:
        return "FAIL"

    # Calculate distances to check [Requirement 3], [Requirement 4], [Requirement 6], and [Requirement 7]
    calculated_total_cost = 0
    calculated_max_distance = 0

    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += dist
        calculated_max_distance = max(calculated_max_distance, dist)

    # [Requirement 6]
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    # [Requirement 7]
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Provided solution details
solution_tour = [0, 8, 5, 4, 7, 2, 1, 9, 6, 3, 0]
solution_total_cost = 384.7863591860825
solution_max_distance = 78.63841300535

# Run the verification
result = verify_solution(solution_tour, solution_total_cost, solution_max_distance)
print(result)