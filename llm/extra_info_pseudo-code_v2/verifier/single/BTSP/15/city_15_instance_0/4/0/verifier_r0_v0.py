import math

# Cities coordinates, indexed from 0 to 14
cities = [
    (9, 93),  # City 0 - Depot
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Tour provided in the solution
provided_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]
provided_total_cost = 748.0763256382368
provided_max_distance = 81.60882305241266

def check_solution(tour, total_cost, max_distance):
    # Requirement 1 & 5: Tour start and end at city 0, correct start and end points
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city visited exactly once (except the return to depot)
    if sorted(tour[:-1]) != list(range(15)):
        return "FAIL"
    
    # Calculated values for verification
    calc_total_cost = 0
    calc_max_distance = 0
    
    # Traverse the entire provided tour
    for i in range(len(tour)-1):
        city_a = cities[tour[i]]
        city_b = cities[tour[i+1]]
        # Requirement 3: Distance calculation (Euclidean)
        distance = math.sqrt((city_b[0] - city_a[0])**2 + (city_b[1] - city_a[1])**2)
        calc_total_cost += distance
        if distance > calc_max_distance:
            calc_max_distance = distance
    
    # Requirement 6: Check total cost
    if not math.isclose(calc_total_cost, total_cost, abs_tol=1e-5):
        return "FAIL"
    
    # Requirement 7: Check max distance
    if not math.isclose(calc_max_distance, max_distance, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Execute the function to check solution validity
result = check_solution(provided_tour, provided_total_cost, provided_max_distance)
print(result)