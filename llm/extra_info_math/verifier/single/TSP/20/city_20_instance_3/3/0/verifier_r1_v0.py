import math

# City coordinates given in the task
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Provided tour and total travel cost
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 14, 8, 12, 18, 0]
reported_total_cost = 425.9972169790246

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_tour_and_cost():
    # Check start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the robot visits all other cities exactly once
    visited = set(tour) - {0}
    if visited != set(range(1, 20)):
        return "FAIL"
    
    # Calculate the total travel cost
    total_calculated_cost = sum(calculate_euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    # Compare calculated travel cost with the reported one (allowing for a small floating point error margin)
    if not math.isclose(total_calculated_cost, reported_total_cost, rel_tol=1e-9):
        return f"FAIL: Calculated cost {total_calculated_cost} != Reported cost {reported_total_cost}"
    
    # All checks passed
    return "CORRECT"

# Conduct the tests
result = check_tour_and_cost()
print(result)