import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def validate_solution(tour, expected_cost):
    # Cities coordinates
    cities = {
        0: (79, 15),
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }
    
    # Check if starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check exactly 8 unique cities including depot are visited
    if len(set(tour)) != 8 or len(tour) != 9:
        return "FAIL"
    
    # Checking direct travel and computing distance
    total_distance = 0
    previous_city = tour[0]
    for current_city in tour[1:]:
        if current_city not in cities:
            return "FAIL"
        total_distance += euclidean_sdistance(cities[previous_city], cities[current_city])
        previous_city = current_city
    
    # Check if the total travel cost matches
    if not math.isclose(total_distance, expected_cost, abs_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Given solution details
tour_solution = [0, 1, 5, 7, 9, 8, 2, 0]
expected_cost_solution = 278.99

# Validate the solution
result = validate_solution(tour_solution, expected_cost_solution)
print(result)