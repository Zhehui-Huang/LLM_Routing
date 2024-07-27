import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_solution(tour, total_cost, cities_coordinates):
    # Checking Requirement 1: Visit exactly 4 cities, starting and ending at depot city 0
    if len(tour) != 5 or tour[0] != 0 or tour[-1] != 0 or len(set(tour)) != 5:
        return "FAIL"
    
    # Checking Requirement 2: Calculate cost as Euclidean distance between cities
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-2):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Given cities coordinates (indexed from 0 to 19)
cities_coordinates = [
    (8, 11),   # Depot city 0
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# Provided solution
tour_solution = [0, 1, 8, 4, 0]
total_cost_solution = 110.09

# Verification
result = verify_solution(tour_solution, total_cost_solution, cities_coordinates)
print(result)  # Expected output: "CORRECT" or "FAIL"