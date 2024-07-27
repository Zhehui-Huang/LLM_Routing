import math

# City coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Provided tour and its total cost
tour = [0, 14, 9, 8, 1, 15, 18, 0]
reported_cost = 151.27

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, reported_cost):
    # Checking Requirement 1: Start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Checking Requirement 2: Tour includes exactly 7 cities
    if len(set(tour)) != 7+1:  # +1 because the depot city is counted twice
        return "FAIL"

    # Checking Requirement 3: Correct calculation of the total tour distance
    total_distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    if not math.isclose(total_distance, reported_cost, rel_tol=1e-2):
        return "FAIL"

    # Requirement 5: Output format checking would be skipped because this is reflected through the setup of the 'tour' and 'reported_cost' variables.
    
    # Requirement 6: We assume the GVNS algorithm has been employed as no direct check can be implemented for that from the result alone.

    return "CORRECT"

# Run the verification
result = verify_tour(tour, reported_cost)
print(result)