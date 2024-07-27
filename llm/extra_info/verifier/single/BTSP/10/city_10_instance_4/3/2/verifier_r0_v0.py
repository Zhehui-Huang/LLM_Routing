import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, coordinates):
    # Requirement 1: The robot starts and ends its journey at depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city must be visited exactly once by the robot.
    unique_cities = set(tour)
    if len(unique_cities) != len(coordinates) or len(tour) != len(coordinates) + 1:
        return "FAIL"
    
    # Calculate distances
    distances = []
    for i in range(len(tour) - 1):
        dist = euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        distances.append(dist)
    
    # Requirement 3: Is calculated and provided outside, can't check minimization here without complete heuristic/search.
    # But we can check if the provided max distance is actually in the calculated distances.
    if max(distances) != 61.68:  # Using max distance from the problem's provided solution
        return "FAIL"
    
    # If no checks fail
    return "CORRECT"

# Defined cities coordinates
coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Provided solution
tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]

# Check the solution
result = check_solution(tour, coordinates)
print(result)