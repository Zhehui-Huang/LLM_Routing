import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour_solution(tour, cost):
    # City coordinates mapped from the problem statement
    cities = [
        (16, 90),  # Depot city (0)
        (43, 99),  # City 1
        (80, 21),  # City 2
        (86, 92),  # City 3
        (54, 93),  # City 4
        (34, 73),  # City 5
        (6, 61),   # City 6
        (86, 69),  # City 7
        (30, 50),  # City 8
        (35, 73),  # City 9
        (42, 64),  # City 10
        (64, 30),  # City 11
        (70, 95),  # City 12
        (29, 64),  # City 13
        (32, 79)   # City 14
    ]

    # [Requirement 1] Check if tour starts and ends at the depot city:
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Check if all cities are visited exactly once excluding depot:
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != len(cities) - 1 or any(v == 0 for v in tour[1:-1]):
        return "FAIL"

    # [Requirement 3] Calculate and check the total travel cost:
    calculated_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        return "FAIL"

    # [Requirement 4] Check for subtours by ensuring no repeated visits of non-depot cities:
    if len(tour) - 1 != len(set(tour) - {0}):
        return "FAIL"

    return "CORRECT"

# Solution given:
solution_tour = [0, 1, 4, 12, 3, 7, 10, 9, 5, 14, 13, 8, 6, 0]
solution_cost = 217.35199765477634
    
# Execute the test function and print the result:
test_result = test_tour_solution(solution_tour, solution_cost)
print(test_result)