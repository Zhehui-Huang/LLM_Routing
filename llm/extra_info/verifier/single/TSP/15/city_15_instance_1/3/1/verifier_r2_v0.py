import math

# Given cities coordinates
cities_coordinates = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((cities_coordinates[city1][0] - cities_coordinates[city2][0])**2 + 
                     (cities_coordinates[city1][1] - cities_coordinates[city2][1])**2)

def check_solution(tour, expected_cost):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour should start and end at the depot city 0
    
    if len(set(tour)) != len(cities_coordinates):
        return "FAIL"  # Tour must include each city exactly once
    
    if sorted(tour) != sorted(list(cities_coordinates.keys())):
        return "FAIL"  # Tour should contain all cities
    
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_count += calculate_distance(tour[i], tour[i+1])
    
    if not math.isclose(total_calculated_cost, expected_cost, abs_tol=1e-6):
        return "FAIL"  # Check if the calculated travel cost matches the expected cost
    
    return "CORRECT"

# Provided solution
tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
total_travel_cost = 442.570870788815

# Check the solution
result = check_solution(tour, total_travel_cost)
print(result)