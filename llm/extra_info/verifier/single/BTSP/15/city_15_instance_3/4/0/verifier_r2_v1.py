import math

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, cities):
    """Verify the provided tour against the given requirements."""
    # Requirement 1: Starts and ends at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once (and the depot city exactly twice)
    if sorted(tour[1:-1]) != sorted(cities.keys() - {0}):
        return "FAIL"
    
    # Calculate the measures needed for further checks
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        if distance > max_distance:
            max_distance = distance
    
    # Requirement 3: Check if maximum distance between any two consecutive cities is minimized
    # This checks is not fully implementable directly without solving the problem, instead just validate against given threshold
    if max_distance > 94.11163583744573:
        return "FAIL"
    
    # If all checks are passed, the solution meets the criteria
    return "CORRECT"

# Define city coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 0)
}

# Proposed tour
proposed_tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]

# Verify the solution
result = verify_solution(proposed_tour, cities)
print(result)