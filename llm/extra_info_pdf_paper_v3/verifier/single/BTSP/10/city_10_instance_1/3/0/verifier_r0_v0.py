import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cities, total_cost, max_distance):
    """ Validate the solution based on the given requirements. """
    # Requirement: The robot must start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement: The robot must visit each of the 10 cities exactly once
    if sorted(tour) != list(range(10)) + [0]:  # Tour ends and starts with 0
        return "FAIL"
    
    # Calculate travel costs and verify they match
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Requirement: Check total cost and max distance
    if not (math.isclose(calculated_total_cot, total_cost, rel_tol=1e-2) and
            math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2)):
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates
cities = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Provided solution details
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
total_cost = 291.41
max_distance = 56.61

# Validate the solution
result = verify_solution(tour, cities, total_cost, max_distance)
print(result)