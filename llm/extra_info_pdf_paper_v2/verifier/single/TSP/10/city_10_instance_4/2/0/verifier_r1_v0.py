import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost, city_coordinates):
    # Check if the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the robot visits each city exactly once, excluding the depot city
    visited = set(tour)
    if len(visited) != len(city_coordinates) or 0 not in visited:
        return "FAIL"
    if any(city not in visited for city in range(len(city_coordinates))):
        return "FAIL"

    # Calculate the total distance and compare it
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    # Compare the computed cost with the given cost, considering floating point arithmetic properties
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Cities Coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Given tour and travel cost
tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]
total_cost = 320.7939094250147

# Verify the solution
result = verify_solution(tour, total_cost, cities)
print(result)