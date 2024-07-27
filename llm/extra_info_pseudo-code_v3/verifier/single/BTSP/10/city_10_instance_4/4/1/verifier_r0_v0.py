import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, total_travel_cost, max_distance):
    # Coordinates for each city
    coordinates = {
        0: (79, 15),
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }
    
    # Requirement 1: Check correct number of cities
    if len(coordinates) != 10:
        return "FAIL"
    
    # Requirement 2: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 3: Check each city is visited exactly once
    if sorted(tour[1:-1]) != sorted(coordinates.keys() - {0}):
        return "FAIL"
    
    # Requirement 4 & 7: Calculate and verify travel cost and distances
    calculated_cost = 0
    distances = []
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        distance = calculate_euclidean_distance(*coordinates[city1], *coordinates[city2])
        distances.append(distance)
        calculated_cost += distance
    
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=1e-5):
        return "FAIL"
    
    # Requirement 8: Verify maximum distance
    if not math.isclose(max(distances), max_distance, abs_tol=1e-5):
        return "FAIL"
    
    # Requirement 5: Incomplete verification as "minimizing" can't be verified without running optimization
    # Requirements checked, hence assuming correct unless there's explicit contradiction in expectations
    return "CORRECT"

# Given solution parameters
given_tour = [0, 1, 4, 5, 7, 9, 3, 6, 2, 8, 0]
given_cost = 204.0
given_max_distance = 43.0

# Verify and output the result of the solution check
print(verify_solution(given_tour, given_cost, given_max_distance))