import math

# Test data
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def euclidean_distance(a, b):
    """Calculate Euclidean distance between two coordinates."""
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def validate_tour(tour, total_cost):
    """
    Validate the tour against given requirements.
    """
    # Requirement: The robot must start and end the tour at the depot city, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement: The robot visits exactly 7 cities, including the depot
    if len(set(tour)) != 8:
        return "FAIL"
    
    # Check if tour only consists of defined cities
    if not all(city in cities for city in tour):
        return "FAIL"
    
    # Calculate total travel distance in the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Requirement: Check if calculated total travel distance matches the given total cost (with some tolerance due to floating point arithmetic)
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
tour_solution = [0, 4, 2, 1, 7, 3, 8, 0]
total_cost_solution = 159.97188184793015

# Validate provided solution
result = validate_tour(tour_solution, total_cost_solution)
print(result)