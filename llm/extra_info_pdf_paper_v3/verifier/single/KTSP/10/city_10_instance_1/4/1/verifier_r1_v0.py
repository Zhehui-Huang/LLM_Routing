import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_cost):
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }

    num_cities = 10
    tour_length = 5

    # Check if exactly 10 cities are available
    if len(cities) != num_cities:
        return "FAIL"

    # Check if the tour starts and ends at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the tour visits exactly 5 cities including the depot
    if len(tour) != tour_length + 1:
        return "FAIL"

    # Check if the tour includes no duplicate cities except the depot at the beginning and end
    if len(set(tour) - {0}) + 1 != len(tour) - 1:
        return "FAIL"

    # Calculate and check the total travel cost reported
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Provided solution to test:
tour_solution = [0, 4, 8, 3, 5, 0]
total_cost_solution = 110.38
result = test_solution(tour_solution, total_cash_solution)
print(result)