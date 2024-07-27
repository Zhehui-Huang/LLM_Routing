import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_cost):
    cities = [
        (35, 40),  # City 0 - Depot
        (39, 41),  # City 1
        (81, 30),  # City 2
        (5, 50),   # City 3
        (72, 90),  # City 4
        (54, 46),  # City 5
        (8, 70),   # City 6
        (97, 62),  # City 7
        (14, 41),  # City 8
        (70, 44),  # City 9
        (27, 47),  # City 10
        (41, 74),  # City 11
        (53, 80),  # City 12
        (21, 21),  # City 13
        (12, 39),  # City 14
    ]

    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 12 cities are visited including the depot city
    if len(set(tour)) != 12:
        return "FAIL"

    # Verify the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    # Check if the provided total cost is rounded correctly
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Given solution
tour = [0, 1, 5, 9, 7, 2, 4, 12, 3, 13, 10, 14, 0]
total_cost = 342.86

# Test the solution
result = test_solution(tour, total_cost)
print(result)