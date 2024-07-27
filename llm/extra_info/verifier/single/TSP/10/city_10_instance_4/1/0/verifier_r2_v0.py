import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, coordinates):
    # [Requirement 1] Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Visit all other cities exactly once
    unique_cities = set(tour[1:-1])  # Exclude the depot city from both ends
    if len(unique_cities) != 9:  # 9 other cities
        return "FAIL"
    if len(tour[1:-1]) != 9:
        return "FAIL"

    # [Requirement 3] Travel cost calculated correctly
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of cities
coordinates = [
    (79, 15),  # City 0 - Depot
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

# Given solution to verify
tour = [0, 4, 3, 1, 5, 7, 9, 8, 2, 6, 0]
total_cost = 337.1694332678818

# Run verification
result = verify_solution(tour, total800_cost, coordinates)
print(result)