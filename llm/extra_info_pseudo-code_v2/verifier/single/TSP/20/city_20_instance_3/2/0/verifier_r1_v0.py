import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_solution(coordinates, tour, total_cost):
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check all cities are visited exactly once (except the depot city)
    visited = set(tour)
    if len(visited) != len(coordinates) or set(range(len(coordinates))) != visited:
        return "FAIL"
    
    # Check the tour's calculated cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    if not math.isclose(calculated_сost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of cities including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Provided tour and total travel_cost
provided_tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0, 0]
provided_total_cost = 458

# Validate the tour and output the result
result = validate_solution(coordinates, provided_tour, provided_total_cost)
print(result)