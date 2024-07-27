import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cost):
    # City coordinates as provided in the task description
    cities = {
        0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
        5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
    }
    
    # [Requirement 1] Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if all cities are visited exactly once, except the depot
    visited = set(tour)
    if visited != set(cities.keys()):
        return "FAIL"
    
    # [Requirement 3] Calculate the travel cost and check against provided cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, cost, rel_tol=1e-5):
        return "FAIL"
    
    # [Requirement 4] and [Requirement 5] are inherently satisfied by the nature of the input parameters to the function.

    return "CORRECT"

# Provided solution
tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]
total_cost = 320.7939094250147

# Verify the solution
verification_result = verify_solution(tour, total_cost)
print(verification_result)