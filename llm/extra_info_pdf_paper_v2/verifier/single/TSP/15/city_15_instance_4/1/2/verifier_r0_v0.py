import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost_reported):
    # Define city coordinates
    cities = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
        5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
        10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
    }

    # Check if the tour starts and ends at the depot and if all cities are visited exactly once
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour[1:-1]) != list(range(1, 15)):
        return "FAIL"
    
    # Calculate total travel cost
    total_cost_calculated = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost_calculated += euclidean_distance(*cities[city1], *cities[city2])

    # Check if the reported cost is approximately equal to the calculated cost
    if not math.isclose(total_cost_reported, total_cost_calculated, rel_tol=1e-5):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Provided solution
tour = [0, 1, 5, 9, 2, 7, 4, 12, 11, 6, 3, 14, 8, 10, 13, 0]
total_cost = 295.9986753170861

# Verify the solution
result = verify_solution(tour, total_cost)
print(result)