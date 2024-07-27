import math

# Given cities coordinates
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

# Provided tour and cost
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
provided_cost = 349.1974047195548

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities based on their coordinates."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, provided_cost):
    # Check requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check requirement 2
    if sorted(tour[1:-1]) != sorted(list(cities.keys())[1:]):
        return "FAIL"
    
    # Check requirement 3
    calculated_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    if not math.isclose(calculated_cost, provided_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Check if the solution is correct based on the requirements
result = verify_tour(tour, provided_cost)
print(result)