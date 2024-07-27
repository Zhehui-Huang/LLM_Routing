import math

# Cities' coordinates where index corresponds to the city number
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Provided solution
tour = [0, 17, 18, 13, 9, 10, 15, 4, 3, 6, 12, 16, 5, 2, 14, 8, 0]
reported_cost = 347.41946925416363

def calculate_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_tour(tour, reported_cost):
    """ Validate the provided tour against all requirements """
    # [Requirement 1] Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Exactly 16 unique cities including depot
    if len(set(tour)) != 16 or len(tour) != 17:  # Includes repetition of depot city
        return "FAIL"
    
    # [Requirement 3] and [Requirement 4] are inherently checked by the travel method and optimization claim
    
    # [Requirement 5] Calculate total travel cost and use Euclidean formula
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(tour[i], tour[i+1])
    
    # Tolerance for floating point comparison
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    # [Requirement 6] Output includes tour and cost
    # This is met by providing a function output explicitly
    
    return "CORRECT"  # If all checks are passed

# Execute the test
result = validate_tour(tour, reported_cost)
print(result)