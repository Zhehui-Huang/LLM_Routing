import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost):
    # City coordinates
    cities = {
        0: (16, 90),
        1: (43, 99),
        2: (80, 21),
        3: (86, 92),
        4: (54, 93),
        5: (34, 73),
        6: (6, 61),
        7: (86, 69),
        8: (30, 50),
        9: (35, 73),
        10: (42, 64),
        11: (64, 30),
        12: (70, 95),
        13: (29, 64),
        14: (32, 79)
    }

    # [Requirement 1] Start and finish at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Tour must include exactly 10 cities
    if len(set(tour)) != 10:
        return "FAIL"
    
    # [Requirement 3] and [Requirement 4] Travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(*cities[city1], *cities[city2])
    
    # Check if calculated cost matches the reported cost
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "FAIL"

    # [Requirement 5 and 6] Tour starts and ends at depot, and cost is reported correctly.
    # These have been effectively checked by previous conditions.
    return "CORRECT"

# Provided solution
tour_solution = [0, 0, 6, 13, 5, 9, 14, 1, 4, 12, 7]
total_cost_solution = 153.88296343204163

# Validate the solution
result = verify_solution(tour_solution, total_cost_solution)
print(result)