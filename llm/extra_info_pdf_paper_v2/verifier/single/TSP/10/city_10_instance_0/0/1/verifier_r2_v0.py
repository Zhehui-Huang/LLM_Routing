import math

def calculate_total_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_solution(tour, expected_cost, cities):
    # Check if it starts and ends at the depot (Requirement 2)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once, except depot (Requirement 3)
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or unique_cities != set(range(len(cities))):
        return "FAIL"
    
    # Check if the total travel cost is computed correctly (Requirement 5)
    calculated_cost = calculate_total_cost(tour, cities)
    if not math.isclose(calculated_cost, expected_cost, abs_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = [
    (50, 42),
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

# Given tour and total cost
tour = [0, 7, 6, 1, 5, 9, 2, 3, 8, 4, 0]
total_cost = 284.43620745523253

# Validate tour and total cost using the unit test
result = validate_solution(tour, total_cost, cities)
print(result)