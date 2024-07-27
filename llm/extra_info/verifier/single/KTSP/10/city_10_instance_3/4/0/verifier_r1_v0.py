import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, cost):
    # Coordinates indexed by city number
    coords = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # Check tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check tour visits exactly 7 cities including depot
    if len(set(tour)) != 7 or len(tour) != 8:
        return "FAIL"
    
    # Check output format
    if not isinstance(tour, list) or not isinstance(cost, float):
        return "FAIL"
    
    # Verify travel cost matches Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        calculated_cost += calculate_distance(*coords[city1], *coords[city2])
    
    # Considering some minimal float number differences, use a tolerance
    if not math.isclose(cost, calculated_cost, abs_tol=1e-6):
        return "FAIL"
    
    return "CORRECT"

# Given solution details
tour_given = [0, 4, 2, 1, 7, 3, 8, 0]
cost_given = 159.97188184793015

# Check the solution
result = verify_solution(tour_given, cost_given)
print(result)