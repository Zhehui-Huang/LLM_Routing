import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    cities = [
        (16, 90),  # Depot 0
        (43, 99),  # City  1
        (80, 21),  # City  2
        (86, 92),  # City  3
        (54, 93),  # City  4
        (34, 73),  # City  5
        (6, 61),   # City  6
        (86, 69),  # City  7
        (30, 50),  # City  8
        (35, 73),  # City  9
        (42, 64),  # City  10
        (64, 30),  # City  11
        (70, 95),  # City  12
        (29, 64),  # City  13
        (32, 79)   # City  14
    ]

    # [Requirement 1] Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Visit each city exactly once
    unique_cities = set(tour)
    # Should visit cities from 1 to 14, and the depot city 0 should be visited exactly twice
    if len(tour) != 16 or len(unique_cities) != 15 or tour.count(0) != 2:
        return "FAIL"
    
    # [Requirement 3] Check distance calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Given tour and total cost
tour = [0, 6, 5, 9, 14, 1, 4, 12, 3, 7, 2, 11, 10, 13, 8, 0]
total_cost = 336.25

# Verify the solution
result = verify_solution(tour, total_cost)
print(result)