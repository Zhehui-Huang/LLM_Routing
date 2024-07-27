import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_solution():
    # Coordinates for the cities
    cities = {
        0: (8, 11),
        1: (40, 6),
        2: (95, 33),
        3: (80, 60),
        4: (25, 18),
        5: (67, 23),
        6: (97, 32),
        7: (25, 71),
        8: (61, 16),
        9: (27, 91),
        10: (91, 46),
        11: (40, 87),
        12: (20, 97),
        13: (61, 25),
        14: (5, 59),
        15: (62, 88),
        16: (13, 43),
        17: (61, 28),
        18: (60, 63),
        19: (93, 15)
    }
    
    # Test solution details
    tour = [0, 4, 8, 1, 0]
    reported_cost = 110.08796524611944
    
    # Compute the actual cost based on the provided solution
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Requirements check
    is_correct = True
    
    # [Requirement 1] Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        is_correct = False
    
    # [Requirement 2] Visits exactly 4 cities, including the depot city
    unique_cities = set(tour)
    if len(unique_cities) != 4:
        is_correct = False
    
    # [Requirement 4] Output as list of city indices, starting and ending at depot city
    if not isinstance(tour, list) or tour[0] != 0 or tour[-1] != 0:
        is_correct = False
    
    # [Requirement 5] Output the total cost in the advertised format
    if not isinstance(reported_cost, float):
        is_correct = False
    
    # Check if the reported cost is close to the calculated cost (to account for floating point inaccuracies)
    if not math.isclose(reported_cost, actual_cost, rel_tol=1e-9):
        is_correct = False
    
    # Final evaluation
    if is_correct:
        return "CORRECT"
    else:
        return "FAIL"

# Invoke the test function and print the result
print(test_solution())