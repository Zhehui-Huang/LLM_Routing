import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, expected_cost):
    # Define cities' coordinates
    cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]
    
    # Required checks
    # Check if the tour is None
    if tour is None:
        return "FAIL"  # The inability to provide a route indicates a failure condition.

    # Check 1: The tour should start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check 2: The robot must visit exactly 5 cities
    if len(tour) != 6:  # Including the return to the starting point
        return "FAIL"
    
    # Check 3: Travel cost calculation
    actual_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        actual_cost += euclidean_distance(cities[city2][0], cities[city2][1], cities[city1][0], cities[city1][1])
    
    # Check 4: Check if the travel cost matches the expected cost
    if not math.isclose(actual_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Test the provided solution
solution_tour = None
solution_cost = 74.42907764752479
result = verify_solution(solution_tour, solution_cost)
print(result)