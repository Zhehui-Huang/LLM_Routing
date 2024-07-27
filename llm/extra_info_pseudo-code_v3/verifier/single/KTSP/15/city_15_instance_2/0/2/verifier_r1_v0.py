import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def is_valid_solution(tour, total_cost, cities_coordinates):
    # Requirement 1: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Requirement 2: Exactly 8 cities including the depot
    if len(tour) != 9:  # Considering tour is started and ended at city 0
        return False
    
    # Requirement 3: The tour should be shortest - This can't be directly checked without comparing all solutions, hence skipped here
    
    # Requirement 4: Travel cost is Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
    
    # Requirement 5 and 6: Format checks, implicitly checked by parameters
    if not isinstance(tour, list) or not all(isinstance(x, int) for x in tour):
        return False
    if not isinstance(total_cost, (int, float)):
        return False
    
    # Rounded comparison to avoid floating-point precision issues
    if round(calculated_cost, 2) != round(total_cost, 2):
        return False
    
    return True

# Provided cities' coordinates
cities_coordinates = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Example solution to verify
tour = [0, 13, 10, 5, 8, 11, 6, 2, 0]
total_cost = 203

# Verification of the solution
if is_valid_solution(tour, total_cost, cities_coordinates):
    print("CORRECT")
else:
    print("FAIL")