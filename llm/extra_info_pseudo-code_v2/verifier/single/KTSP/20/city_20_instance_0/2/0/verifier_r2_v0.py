import math

def calculate_distance(city1, city2):
    # City format: (x, y)
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, total_cost):
    cities_coordinates = {
        0: (8, 11),
        1: (40, 6),
        2: (95, 33),
        3: (80, 60),
        4: (25, 18),
        5: (67, 23),
        6: (97, 32),
        7: (25, 71),
        8: (61, 16),
        9: (27, 91),
        10: (91, 46),
        11: (40, 87),
        12: (20, 97),
        13: (61, 25),
        14: (5, 59),
        15: (62, 88),
        16: (13, 43),
        17: (61, 28),
        18: (60, 63),
        19: (93, 15)
    }

    # Requirement 1: The robot must visit exactly 4 cities
    if len(set(tour)) != 4:
        return "FAIL"
    
    # Requirement 2: The robot must start and end at depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 3 & 5: Travel cost calculation & Output must include tour starting and ending at city 0
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])

    # Compare calculated cost to provided one
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Given solution and its total cost
solution_tour = [0, 1, 1, 1, 0]
solution_total_cost = 64.78

# Verify the solution
print(check_solution(solution_tour, solution_total_HEIGHT))