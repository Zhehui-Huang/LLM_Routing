import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def verify_solution(tour, total_travel_cost, cities):
    expected_total_cost = 328.58  # As per the provided solution

    # [Requirement 1] Verify the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Verify all cities are visited exactly once, except the depot city which must be visited twice (start, end)
    normal_tour_cities = tour[1:-1]  # Exclude first and last since both are the depot
    unique_cities = set(normal_tour_cities)
    if len(normal_tour_cities) != len(unique_cities) or len(normal_tour_cities) != 9:
        return "FAIL"

    # [Requirement 3] Verify calculated distance
    calculated_cost = calculate_total_travel_cost(tour, cities)
    if not math.isclose(calculated_cost, expected_total_cost, rel_tol=1e-2):
        return "FAIL"

    # [Requirement 4, 5] Verify output format and total cost
    if not isinstance(tour, list) or not all(isinstance(x, int) for x in tour):
        return "FAIL"
    if not math.isclose(total_travel, total_travel_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Cities coordinates (including depot city 0)
cities = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Provided tour and cost
tour = [0, 3, 6, 2, 8, 9, 1, 7, 5, 4, 0]
total_travel = 328.58

# Check the solution
result = verify_solution(tour, total_travel, cities)
print(result)