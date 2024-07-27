import math

# Define the coordinates for each city
cities_coordinates = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Given solution
tour = [0, 8, 10, 1, 9, 11, 14, 12, 4, 7, 13, 3, 5, 6, 2, 0]
reported_cost = 334.55744546522186

def calculate_euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities.codehaus[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_tour(tour, reported_cost):
    # [Requirement 1] Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if each city, except the depot, is visited exactly once
    if sorted(tour[1:-1]) != list(range(1, 15)):
        return "FAIL"
    
    # [Requirement 3 and 5] Check the travel cost and if it matches the reported cost
    calculated_cost = sum(calculate_euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    if not math.isclose(reported_cost, calculated_cost, rel_tol=1e-5):
        return "FAIL"
    
    # All tests passed
    return "CORRECT"

# Run the test
result = test_tour(tour, reported_cost)
print(result)