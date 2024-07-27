import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_requirements(tour, total_cost, max_distance):
    cities = [
        (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
        (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
        (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
    ]
    
    # Check Requirement 1: Starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: All cities are visited exactly once except depot
    unique_cities = set(tour)
    if len(unique_cities) != 16 or len(tour) != 19 or len(set(tour[1:-1])) != 14:
        return "FAIL"

    # Check Requirement 4 and calculate Requirement 6 and 7 during tour simulation
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        dist = calculate_distance(x1, y1, x2, y2)
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist

    # Check Requirement 6: Total travel cost
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    # Check Requirement 7: Max distance between consecutive cities
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Provided solution details
solution_tour = [0, 10, 6, 3, 8, 13, 14, 10, 11, 12, 4, 12, 5, 9, 7, 2, 5, 1, 0]
solution_total_cost = 388.19
solution_max_distance = 35.78

# Check the solution
result = check_requirements(solution_tour, solution_total_cost, solution_max_distance)
print(result)