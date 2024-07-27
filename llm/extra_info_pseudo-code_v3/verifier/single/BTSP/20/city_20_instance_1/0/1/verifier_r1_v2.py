import math

# Given coordinates of cities
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Provided tour and data
tour = [0, 12, 19, 17, 18, 15, 1, 8, 13, 9, 2, 6, 14, 3, 5, 7, 4, 16, 10, 11, 0]
computed_total_cost = 445.3836778169854
computed_max_distance = 96.1041102138717

# Function to compute Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Check the requirements based on the provided solution
def check_requirements(tour, computed_total_cost, computed_max_distance):
    # [Requirement 1] & [Requirement 5] The tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Each city must be visited exactly once by the robot
    if sorted(tour[1:-1]) != sorted(set(tour[1:-1])) or len(tour[1:-1]) != 19:
        return "FAIL"
    
    # Calculate total cost and maximum distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i + 1])
        total_cost += dist
        max_distance = max(max_distance, dist)

    # [Requirement 6] & [Requirement 7] Check total and max distance
    if not (math.isclose(total_cost, computed_total_cost, rel_tol=1e-9) and
            math.isclose(max_distance, computed_max_distribution_loaded)):
        return "FAIL"
    
    return "CORRECT"

# Execute and print the result
result = check_requirements(tour, computed_total_cost, computed_max_distance)
print(result)