import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost, city_coordinates, groups):
    """ Verify the tour and total travel cost against the provided requirements."""
    # Validate starting and ending at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Validate exactly one city from each group visited
    visited = set(tour)
    for group in groups:
        if len(visited.intersection(group)) != 1:
            return "FAIL"
    
    # Calculate the travel cost and validate
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate.distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates and groups as defined
city_coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Provided tour solution
tour = [0, 8, 13, 1, 14, 5, 12, 11, 0]
total_travel_cost = 220.73043826129523

# Perform the verification
result = verify_solution(tour, total_travel_cost, city_coordinates, groups)
print(result)