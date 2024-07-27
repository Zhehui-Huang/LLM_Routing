import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def run_checks():
    # Define cities and tour from solution
    cities = {
        0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
        5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
        10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
        15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
    }
    tour = [0, 12, 15, 13, 18, 7, 11, 19, 16, 14, 0]
    expected_cost = 175.48

    # Check tour starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check exactly 10 cities are visited
    if len(set(tour)) != 10:
        return "FAIL"
    
    # Compute total cost and check it
    total_distance = 0
    for i in range(len(tour) - 1):
        city_a, city_b = tour[i], tour[i + 1]
        total_distance += euclidean_distance(cities[city_a], cities[city_b])
    
    if not math.isclose(total_distance, expected_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Output result
print(run_checks())