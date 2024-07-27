import math

# Define the city coordinates
coordinates = [
    (14, 77),  # Depot city 0
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9)
]

# Provided results
tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
total_cost = 477.05
max_dist = 87.46

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities based on their coordinates. """
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_solution(tour, total_cost, max_dist):
    # Check requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check requirement 2: Visit each city exactly once
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return "FAIL"
    
    # Calculate the total and maximum consecutive travel distance
    calc_total_cost = 0
    calc_max_dist = 0
    
    for i in range(len(tour) - 1):
        dist = euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        calc_total_cost += dist
        calc_max_dist = max(calc_max_dist, dist)
    
    # Check requirement 5: Total cost calculated correctly
    if not math.isclose(calc_total_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    # Check requirement 6: Maximum distance calculated correctly
    if not math.isclose(calc_max_dist, max_dist, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Test and output the result
test_result = check_solution(tour, total_cost, max_dist)
print(test_result)