import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_cost):
    cities = [
        (9, 93),  # depot city 0
        (8, 51),  # city 1
        (74, 99), # city 2
        (78, 50), # city 3
        (21, 23), # city 4
        (88, 59), # city 5
        (79, 77), # city 6
        (63, 23), # city 7
        (19, 76), # city 8
        (21, 38), # city 9
        (19, 65), # city 10
        (11, 40), # city 11
        (3, 21),  # city 12
        (60, 55), # city 13
        (4, 39)   # city 14
    ]

    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour must start and end at depot city 0."
    
    # [Requirement 2]
    if len(set(tour)) != len(cities) + 1 or len(tour) != len(cities) + 1:
        return "FAIL: Each city must be visited exactly once, other than the depot."
    
    # [Requirement 3 & 5]
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-9):
        return f"FAIL: The reported total cost {total_cost} doesn't match computed cost {computed_cost}."
    
    # [Requirement 4]
    if not isinstance(tour, list) or any(not isinstance(x, int) for x in tour):
        return "FAIL: Tour output format is incorrect."

    return "CORRECT"

# Test the given solution
solution_tour = [0, 8, 10, 1, 11, 14, 12, 4, 9, 7, 3, 5, 6, 2, 13, 0]
solution_total_cost = 359.53718629646994
result = test_solution(solution_tour, solution_total_cost)
print(result)