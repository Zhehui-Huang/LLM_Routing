import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, coordinates):
    # Verify each city is visited exactly once
    if sorted(tour[1:-1]) != list(range(1, len(coordinates))):
        return "FAIL: Not all cities are visited exactly once or there are duplicates."
    
    # Verify tour starting from depot city
    if tour[0] != 0 or tour[-1] != 2:
        return "FAIL: Tour does not start or end at depot city 0."
    
    # Verify the distance formula
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += calculate_euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    
    if not math.isclose(total_distance, 324.165, rel_tol=0.001):
        return "FAIL: The total distance does not match."
    
    return "CORRECT"

# City coordinates indexed by city ID
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Provided solution
robot_0_tour = [0, 0, 14, 19, 21, 20, 18, 9, 5, 7, 10, 12, 15, 17, 16, 13, 11, 8, 6, 4, 3, 1, 2]

# Verify the solution
result = verify_solution(robot_0_tour, city_coordinates)
print(result)