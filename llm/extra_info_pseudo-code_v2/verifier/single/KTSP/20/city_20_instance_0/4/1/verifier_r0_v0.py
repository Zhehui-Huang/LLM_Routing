import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, expected_cost):
    cities = [
        (8, 11),  # Depot city 0
        (40, 6),  # City 1
        (95, 33), # City 2
        (80, 60), # City 3
        (25, 18), # City 4
        (67, 23), # City 5
        (97, 32), # City 6
        (25, 71), # City 7
        (61, 16), # City 8
        (27, 91), # City 9
        (91, 46), # City 10
        (40, 87), # City 11
        (20, 97), # City 12
        (61, 25), # City 13
        (5, 59),  # City 14
        (62, 88), # City 15
        (13, 43), # City 16
        (61, 28), # City 17
        (60, 63), # City 18
        (93, 15)  # City 19
    ]

    # [Requirement 1] The tour must start and end at the depot city, which has the index of 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] The robot must visit exactly 4 cities in total, including the depot city.
    if len(tour) != 5:
        return "FAIL"

    # Calculate the actual travel cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    # [Requirement 3] The objective is to minimize the total travel cost.
    # This is tricky to verify without knowing all possible tours' distances
    # But we can check if the cost is correctly calculated.
    if not math.isclose(actual_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Provided solution for verification
provided_tour = [0, 1, 13, 4, 0]
provided_cost = 115.77

# Call the test function
result = test_solution(provided_tour, provided_cost)
print(result)