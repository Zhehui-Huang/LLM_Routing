import math

# Data for cities' coordinates provided in the problem statement
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def validate_tour(tour, expected_cost):
    # Test 1: Check if the route starts and ends in depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test 2: Check if exactly 12 cities are visited including the depot city
    if len(set(tour)) != 12:
        return "FAIL"
    
    # Test 3: Calculate the total distance and validate it
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Checking the precision of floating point arithmetic up to 2 decimal places
    if round(total_distance, 2) != expected_cost:
        return "FAIL"
    
    return "CORRECT"

# Expected solution based on the task description
solution_tour = [0, 1, 5, 9, 7, 2, 13, 14, 8, 3, 6, 0]
expected_cost = 261.22

# Running the unit test
result = validate_tour(solution_tour, expected_cost)
print(result)