import math

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def test_solution(tour, total_travel_cost):
    cities = [
        (9, 93),  # City 0
        (8, 51),  # City 1
        (74, 99), # City 2
        (78, 50), # City 3
        (21, 23), # City 4
        (88, 59), # City 5
        (79, 77), # City 6
        (63, 23), # City 7
        (19, 76), # City 8
        (21, 38), # City 9
        (19, 65), # City 10
        (11, 40), # City 11
        (3, 21),  # City 12
        (60, 55), # City 13
        (4, 39)   # City 14
    ]

    # [Requirement 1] Start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Visit exactly 4 cities, including the depot
    if len(tour) != 5 or len(set(tour)) != 4:
        return "FAIL"
    
    # Calculate the tour cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # [Requirement 3] Minimize the total travel cost
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"

    # [Requirement 5] The output should include correct tour and cost
    if not isinstance(tour, list) or not isinstance(total_travel_cost, float):
        return "FAIL"

    # Note: Requirements 4 and 6 are about the method used and cannot be checked directly from the output.

    return "CORRECT"

# Input data
tour = [0, 9, 10, 8, 0]
total_travel_cost = 114.09092744482805

# Perform the tests
result = test_solution(tour, total_travel_cost)
print(result)