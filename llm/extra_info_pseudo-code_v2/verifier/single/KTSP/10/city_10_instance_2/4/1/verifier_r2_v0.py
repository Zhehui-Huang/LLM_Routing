import math

def compute_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Given solution
tour = [0, 0, 9, 7, 4, 6]
reported_cost = 183.75785418901575

# Cities coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def validate_solution(tour, reported_cost):
    # Checking starting and ending at the depot city (Requirement 1)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Checking exact number of cities visited (Requirement 2)
    if len(set(tour)) != 6:
        return "FAIL"

    # Tour output as a list of city indices (Requirement 3)
    if not all(isinstance(city, int) for city in tour):
        return "FAIL"
    
    # Compute travel cost (Requirement 4 & 5)
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        total_cost += compute_euclidean_distance(x1, y1, x2, y2)

    # Comparing calculated cost to reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Execute the validation function
result = validate_solution(tour, reported  _cost)
print(result)