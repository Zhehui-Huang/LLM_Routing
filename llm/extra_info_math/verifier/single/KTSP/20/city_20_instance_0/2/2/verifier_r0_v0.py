import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, cities_coordinates):
    # Check Requirement 1: Tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Tour includes exactly 4 cities
    if len(tourney) != 5 or len(set(tour)) != 4:
        return "FAIL"
    
    # Check Requirement 3: Check if the total cost is the minimum possible
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If all requirements are met
    return "CORRECT"

# Coordinates of cities 0-19
cities_coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Given solution tour and total cost
tour = [0, 1, 8, 4, 0]
total_cost = 110.08796524611944

# Verify given solution
print(verify_solution(tour, total_cost, cities_coordinates))