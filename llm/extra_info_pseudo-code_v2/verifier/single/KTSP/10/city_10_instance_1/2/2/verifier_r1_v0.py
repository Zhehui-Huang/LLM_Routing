import numpy as np
from math import sqrt

# Cities coordinates dictionary
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

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Tour and total cost from the solution
solution_tour = [0, 4, 8, 3, 5, 0]
solution_cost = 110.38

# Requirement and verification
def check_requirements(tour, cost):
    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]
    if len(tour) != 6:  # 5 cities + 1 repeated depot at the end
        return "FAIL"
    
    # [Requirement 3]
    calculated_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    if not np.isclose(calculated_cost, cost, atol=0.1):  # allowing a small numerical tolerance
        return "FAIL"

    # Additional check: the cities must be unique except for the repeated depot
    if len(set(tour[:-1])) != 5:
        return "FAIL"

    # If all checks passed:
    return "CORRECT"

# Execute the checks
verification_result = check_requirements(solution_tour, solution_cost)
print(verification_result)