import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, travel_cost):
    # City coordinates
    coords = [
        (79, 15),  # City 0 - depot
        (79, 55),  # City 1
        (4, 80),   # City 2
        (65, 26),  # City 3
        (92, 9),   # City 4
        (83, 61),  # City 5
        (22, 21),  # City 6
        (97, 70),  # City 7
        (20, 99),  # City 8
        (66, 62)   # City 9
    ]
    
    # Verify requirement 1: start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify requirement 2: all cities visited exactly once (except depot visited twice)
    if sorted(tour[:-1]) != list(range(10)):  # Check if all cities from 0 to 9 are in the tour
        return "FAIL"

    # Verify requirement 3: travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(coords[tour[i]], coords[tour[i+1]])
    
    if not math.isclose(calculated_cost, travel_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Solution provided
tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]
total_travel_cost = 306.47608836173833

# Verify the solution
test_result = verify_solution(tour, total_travel_cost)
print(test_result)