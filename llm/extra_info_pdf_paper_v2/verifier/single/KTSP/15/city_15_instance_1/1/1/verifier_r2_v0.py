import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    # Given Tour and Total Cost
    provided_tour = [0, 6, 1, 7, 3, 9, 0]
    provided_cost = 118.8954868377263
    
    # City coordinates
    coordinates = [
        (29, 51),   # City 0 - Depot
        (49, 20),   # City 1
        (79, 69),   # City 2
        (17, 20),   # City 3
        (18, 61),   # City 4
        (40, 57),   # City 5
        (57, 30),   # City 6
        (36, 12),   # City 7
        (93, 43),   # City 8
        (17, 36),   # City 9
        (4, 60),    # City 10
        (78, 82),   # City 11
        (83, 96),   # City 12
        (60, 50),   # City 13
        (98, 1)     # City 14
    ]

    # [Requirement 1] Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] The tour must include exactly 6 cities
    if len(set(tour)) != 6:
        return "FAIL"
    
    # [Requirement 3] Calculate and compare Euclidean distances
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += calculate_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Parameters from the user's solution
user_tour = [0, 6, 1, 7, 3, 9, 0]
user_total_cost = 118.8954868377263

# Verification
result = verify_solution(user_tour, user_total_cost)
print(result)