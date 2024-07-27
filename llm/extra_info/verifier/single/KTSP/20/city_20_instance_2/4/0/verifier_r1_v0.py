import math

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost, city_coordinates):
    # Checking for Requirement 1
    if len(tour) != 11 or len(set(tour)) != 11:
        return "FAIL"
    
    # Checking for Requirement 2
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculating total distance cost for the provided tour
    computed_cost = 0
    for i in range(len(tour) - 1):
        src = tour[i]
        dest = tour[i + 1]
        computed_cost += euclidean_distance(city_coordinates[src], city_coordinates[dest])
    
    # Checking for Requirement 3 and Requirement 4
    # Comparing the computed distance cost with the provided one
    if abs(computed_cost - total_cost) > 1e-6:
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# City coordinates as given in the task description
city_coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Proposed solution tour and total cost
tour = [0, 6, 8, 10, 11, 13, 14, 16, 18, 19, 0]
reported_total_cost = 277.47243278560416

# Verify the solution
result = verify_solution(tour, reported_total_cost, city_coordinates)
print(result)