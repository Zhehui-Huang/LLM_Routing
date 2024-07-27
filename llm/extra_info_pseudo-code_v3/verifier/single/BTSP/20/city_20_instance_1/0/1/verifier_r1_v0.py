import math

# Given data
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Solution data
tour = [0, 12, 19, 17, 18, 15, 1, 8, 13, 9, 2, 6, 14, 3, 5, 7, 4, 16, 10, 11, 0]
computed_total_cost = 445.3836778169854
computed_max_distance = 96.1041102138717

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city2][0] - cities[city1][0])**2 + (cities[city2][1] - cities[city1][1])**2)

# Check requirements
def check_requirements(tour, computed_total_cost, computed_max_distance):
    # [Requirement 1] & [Requirement 5]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return "FAIL"
    
    # [Requirement 4] & [Requirement 6] & [Requirement 7]
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        d = distance(tour[i], tour[i + 1])
        total_cost += d
        max_distance = max(max_distance, d)
    
    # Checking total_cost and max_distance against provided values
    if not (math.isclose(total_cost, computed_total_cost, rel_tol=1e-9) and
            math.isclose(max_distance, computed_max_distance, rel_tol=1e-9)):
        return "FAIL"

    return "CORRECT"

# Perform the check
print(check_requirements(tour, computed_total_post, computed_max_distance))