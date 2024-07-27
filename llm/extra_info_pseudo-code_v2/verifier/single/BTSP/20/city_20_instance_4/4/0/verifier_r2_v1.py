import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution():
    # Coords indexed by city number
    coords = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
        (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
        (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
        (64, 72), (14, 89)
    ]
    # Provided solution details
    tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
    reported_cost = 410.03585920085146
    reported_max_dist = 89.00561780022652
    
    # Verify Requirement 4
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify Requirement 1
    if sorted(tour[:-1]) != list(range(20)):
        return "FAIL"

    # Calculate actual total travel cost and max distance
    actual_cost = 0
    actual_max_dist = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        distance = calculate_euclidean_distance(*coords[city1], *coords[city2])
        actual_cost += distance
        actual_max_dist = max(actual_max_dist, distance)
    
    # Verify Requirement 5 and 6
    if not (math.isclose(actual_cost, reported_cost, rel_tol=1e-5) and 
            math.isclose(actual_max_dist, reported_max_dist, rel_tol=1e-5)):
        return "FAIL"
    
    return "CORRECT"

# Running the test
print(test_solution())