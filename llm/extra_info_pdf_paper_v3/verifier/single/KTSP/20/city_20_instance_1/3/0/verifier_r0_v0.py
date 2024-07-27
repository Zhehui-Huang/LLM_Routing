import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, claimed_cost, city_coordinates):
    # Requirement: There are 20 cities
    if len(city_coordinates) != 20:
        return "FAIL"
    
    # Requirement: The robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement: The robot has to visit exactly 7 cities
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Calculate total travel cost using Euclidean distance
    total_cost = 0.0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += calculate_distance(city_coordinates[city1], city_coordinates[city2])

    # Compare calculated total_cost with claimed_cost
    if not math.isclose(total_cost, claimed_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# City coordinates as given in problem statement
city_coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Solution tour and claimed cost
tour = [0, 6, 2, 13, 8, 9, 14, 0]
claimed_cost = 130.67

# Verifying the solution
result = verify_solution(tour, claimed_cost, city_coordinates)
print(result)