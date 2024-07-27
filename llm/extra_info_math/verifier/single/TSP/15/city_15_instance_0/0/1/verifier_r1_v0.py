import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(cities, tour, reported_cost):
    """ Verify the correctness of the tour based on the given requirements """
    # Requirement 1: The robot starts and ends at depot city (0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once, except the depot (Present exactly twice including return)
    if sorted(tour) != sorted([0, 0] + list(range(1, len(cities)))):
        return "FAIL"
    
    # Requirement 4: Calculate total travel cost and compare with reported cost
    calculated_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, reported_cost, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given coordinates of cities (corresponds to their indices: city 0 is depot)
cities = [
    (9, 93),   # Depot city 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 9)     # City 14, corrected for disparity in provided coordinates
]

# Tour based on the solution output
tour = [0, 8, 10, 1, 9, 11, 14, 12, 4, 7, 13, 3, 5, 6, 2, 0]

# Reported travel cost
reported_cost = 314.8343625419059

# Verify the solution
result = verify_tour(cities, tour, reported_cost)
print(result)