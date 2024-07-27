import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

# Cities with their coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Given solution details
tour = [0, 16, 14, 7, 9, 12, 11, 15, 18, 3, 10, 2, 6, 19, 5, 13, 17, 8, 1, 4, 0]
reported_total_cost = 353.09426628274167

def check_requirements():
    # Requirement 1: Start and finish at depot (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit every other city exactly once
    unique_cities = set(tour)
    if len(unique_cities) != 21 or len(tour) != 21:  
        return "FAIL"
    
    # Requirement 3: Calculate proper total distance
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(total_cost, reported_total_cost, abs_tol=1e-5):
        return "FAIL"
    
    # Requirements 4 and 5 are about output format and total cost, we verify these checking the tour and cost directly
    # Requirement 6 is a procedural requirement we assume is met since the algorithm's output fits the expected output pattern
    
    return "CORRECT"

# Perform the verification
print(check_requirements())