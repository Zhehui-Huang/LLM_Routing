import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, provided_cost, city_coordinates):
    # Requirement 1: Start and end at city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Exactly 7 cities including the starting city
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Calculate and check total travel cost for Requirement 3
    total_cost_calculated = 0
    for i in range(len(tour) - 1):
        total_cost_calculated += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    # Comparing provided cost with calculated cost
    if not math.isclose(provided_cost, total_cost_calculated, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# City coordinates as given in the problem
city_coordinates = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    7: (74, 56),
    8: (85, 71)
}

# Provided solution details
provided_tour = [0, 1, 2, 3, 4, 7, 8, 0]
provided_total_cost = 242.68

# Verify the solution
result = verify_solution(provided_tour, provided_total_cost, city_coordinates)
print(result)