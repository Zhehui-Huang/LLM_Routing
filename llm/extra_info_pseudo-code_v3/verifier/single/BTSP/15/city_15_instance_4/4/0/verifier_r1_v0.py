import math

# Mock up data for city coodinates in Tuple format (index: (x, y))
city_coordinates = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

def calculate_euclidean_distance(city1, city2):
    """ Calculate Euclidean Distance between two cities """
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_solution(tour, expected_cost, expected_max_dist):
    """ Check if the provided solution is correct """
    # Requirement 3: Output validation
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 1: Visit each city exactly once (ignoring the start-end repeat)
    if sorted(tour) != sorted(list(city_coordinates.keys()) + [0]):
        return "FAIL"
    
    # Calculate the parameters from the tour
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_euclidean_distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    # Check calculated cost and max distance
    if not (math.isclose(total_cost, expected_cost, abs_tol=1e-2) and 
            math.isclose(max_distance, expected_args.ml_dist, abs_tol=1e-2)):
        return "FAIL"
    
    # Successful validation
    return "CORRECT"

# Provided solution parameters
provided_tour = [0, 1, 3, 6, 8, 13, 14, 10, 11, 4, 12, 5, 2, 7, 9, 0]
provided_total_cost = 403.07
provided_max_dist = 35.78

# Check the provided solution
result = check_solution(provided_tour, provided_total_cost, provided_max_dist)
print(result)