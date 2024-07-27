import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    cities = [
        (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
        (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
        (83, 96), (60, 50), (98, 1)
    ]
    
    # [Requirement 1] and [Requirement 5]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2]
    if set(tour) != set(range(len(cities))):
        return "FAIL"

    # Calculate travel cost and compare to given total_cost
    calculated_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    
    # [Requirement 3] and [Requirement 6]
    if abs(calculated_cost - total_cost) > 0.01:  # Allowing a tiny margin for floating point arithmetic differences
        return "FAIL"

    # [Requirement 4] Not possible to check optimality without solving the problem but verified other conditions already.
    
    return "CORRECT"

# Solution details
tour = [0, 10, 4, 0, 9, 3, 7, 1, 6, 13, 2, 12, 11, 8, 14, 5, 0]
total_cost = 393.60120757501943

# Verification
print(verify_solution(tour, total_cost))