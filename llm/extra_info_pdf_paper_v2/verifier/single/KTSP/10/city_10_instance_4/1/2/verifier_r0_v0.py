import math

# Define the cities with their coordinates
cities = {
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

# Provided solution
tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
provided_total_cost = 235.37735391753955

def calculate_euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities with their coordinates."""
    return math.sqrt((cities[city2][0] - cities[city1][0])**2 + (cities[city2][1] - cities[city1][1])**2)

def test_solution(tour, provided_total_cost):
    # Test [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test [Requirement 2]
    if len(set(tour)) != 9:  # Set to count unique cities, must be 9 including city 0 repeated.
        return "FAIL"
    
    # Test [Requirement 3] and [Requirement 4]
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_euclidean_distance(tour[i], tour[i+1])
    
    if abs(total_calculated_cost - provided_totalolesale) > 1e-6:
        return "FAIL"

    # Everything passed implying the solution may be correct
    return "CORRECT"

# Check the solution
result = test_solution(tour, provided_total_cost)
print(result)