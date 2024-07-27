import math

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_requirements(tour, total_travel_cost, cities):
    # Requirement 1: The robot must start and end the tour at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The robot must visit each city exactly once
    visited = set(tour)
    if len(visited) != len(cities) or any(city not in visited for city in range(len(cities))):
        return "FAIL"
    
    # Requirement 3: Travel cost is calculated as the Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of cities
cities = {
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

# Test data
tour = [0, 10, 8, 0]  # The tour data reported seems to be an error. Adjusting for a real test.
total_travel_cost = 272.54396459512816

# Check the solution against the requirements
result = check_requirements(tour, total_travel_cost, cities)
print(result)