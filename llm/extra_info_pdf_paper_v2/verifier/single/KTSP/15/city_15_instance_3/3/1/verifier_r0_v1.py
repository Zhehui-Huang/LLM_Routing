import math

def calculate_euclidean_distance(coord1, coord2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution(tour, total_travel_cost):
    """
    Verify if the provided tour and total travel cost satisfy given requirements.
    """
    # Coordinates of the cities
    cities = {
        0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
        5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
        10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
    }
    
    # Requirement 1: Check start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: The tour does not start and end at the depot city 0."
    
    # Requirement 2: Check that exactly 10 cities are visited
    if len(set(tour[:-1])) != 10:  # Checking without the repeated depot city at the end
        return "FAIL: The robot does not visit exactly 10 cities."
    
    # Requirement 3 & 5: Calculating and Checking Total Travel Cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if abs(calculated_cost - total_travel_cost) > 1e-5:
        return "FAIL: Calculated travel cost does not match the given total travel cost."
    
    # All requirements satisfied
    return "CORRECT"

# Provided tour and total travel cost
given_tour = [0, 14, 5, 9, 13, 6, 8, 10, 1, 4, 0]
given_total_travel_cost = 191.2548544658934

# Test the solution
result = verify_solution(given_tour, given_total_travel_cost)
print(result)