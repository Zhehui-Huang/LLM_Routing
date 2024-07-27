import math

def calculate_distance(city_a, city_b):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city_a[0] - cityb[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

def test_solution():
    # Given data
    cities = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20),
        4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12),
        8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
        12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    
    # Solution provided
    tour = [0, 5, 13, 1, 9, 0]
    reported_cost = 120.66
    
    # Requirement 1: Start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Exactly 6 cities including depot city
    if len(set(tour)) != 6:
        return "FAIL"
    
    # Requirement 4: Calculate travel cost and verify
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Allow a small margin of error for floating point calculations
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-2):
        return "FAIL"
    
    # If all checks passed
    return "CORRECT"

# Run the test and output the result
print(test_solution())