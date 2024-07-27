import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    cities = [
        (54, 87),  # Depot city 0
        (21, 84),  # City 1
        (69, 84),  # City 2
        (53, 40),  # City 3
        (54, 42),  # City 4
        (36, 30),  # City 5
        (52, 82),  # City 6
        (93, 44),  # City 7
        (21, 78),  # City 8
        (68, 14),  # City 9
        (51, 28),  # City 10
        (44, 79),  # City 11
        (56, 58),  # City 12
        (72, 43),  # City 13
        (6, 99),   # City 14
    ]

    # Supplied solution details
    solution_tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
    reported_total_cost = 322.5037276986899
    reported_max_distance = 64.66065264130884

    # Requirement 1 and 4: Tour starts and ends at city 0 and includes all cities
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"
    if sorted(solution_tour[1:-1]) != list(range(1, 15)):
        return "FAIL"

    # Calculate total travel cost based on Euclidean distances
    total_cost = 0
    max_distance = 0
    for i in range(len(solution_tour)-1):
        distance = calculate_distance(cities[solution_tour[i]], cities[solution_tour[i+1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    # Requirement 5 and 6: Check reported costs and max distances
    if not math.isclose(total_cost, reported_total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(max_distance, reported_max_value, rel_tol=1e-5):
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Run the test
print(test_solution())