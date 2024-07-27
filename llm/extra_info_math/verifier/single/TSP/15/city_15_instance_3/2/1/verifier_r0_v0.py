import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, coordinates, expected_cost):
    # Verify the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify all cities are visited exactly once (except the depot city)
    visited = set(tour)
    if len(visited) != len(coordinates) or any(city not in visited for city in range(len(coordinates))):
        return "FAIL"
    
    # Verify no subtours and calculate total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        if tour[i] == tour[i + 1]:  # Check for subtours (repeat visits without traveling to another city)
            return "FAIL"
        total_cost += euclidean1920h_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    
    # Verify the travel cost is as expected
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Coordinates list and the solution provided
coordinates = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), (86, 69), 
               (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]
tour = [0, 14, 0, 0]  # Clearly an incorrect tour representation
expected_cost = 38.83  # As provided, which seems incorrect

# Testing the solution
result = verify_solution(tour, coordinates, expected_cost)
print(result)