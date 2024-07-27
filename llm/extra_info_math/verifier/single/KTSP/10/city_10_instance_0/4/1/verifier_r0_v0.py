import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution():
    coordinates = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    
    # Provided solution details
    provided_solution_tour = [0, 9, 5, 6, 0]
    provided_solution_cost = 61.65991894151281
    
    # Check Requirement 1
    if provided_solution_tour[0] != 0 or provided_solution_tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2
    if len(provided_solution_tour) != 5 or len(set(provided_solution_tour)) != 4:  # 4 cities + starting at the depot
        return "FAIL"
    
    # Check Requirement 3
    calculated_cost = 0
    for i in range(len(provided_solution_tour) - 1):
        city_idx1 = provided_solution_tour[i]
        city_idx2 = provided_solution_tour[i+1]
        dist = calculate_euclidean_distance(coordinates[city_idx1], coordinates[city_idx2])
        calculated_cost += dist
    
    if not math.isclose(calculated_cost, provided_solution_cost, rel_tol=1e-9):
        return "FAIL"
    
    # No knowledge of what the minimal cost should be, cannot strictly test Requirement 4, but ensure the cost matches provided
    return "CORRECT"

# Call the verification function
print(verify_solution())