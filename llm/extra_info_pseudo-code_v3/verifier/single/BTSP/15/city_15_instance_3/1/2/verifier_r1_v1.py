import math

def calculate_distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_solution(tour, total_travel_cost, max_distance):
    # Coordinates of cities
    coordinates = [
        (16, 90),  # Depot: city 0
        (43, 99),
        (80, 21),
        (86, 92),
        (54, 93),
        (34, 73),
        (6, 61),
        (86, 69),
        (30, 50),
        (35, 73),
        (42, 64),
        (64, 30),
        (70, 95),
        (29, 64),
        (32, 79),
    ]
    
    if tour[0] != 0 or tour[-1] != 0:  # Check if starts and ends at city 0
        return "FAIL"
    if sorted(tour[:-1]) != list(range(len(coordinates))):  # Check all cities visited once
        return "FAIL"
    
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(1, len(tour)):
        dist = calculate_distance(coordinates[tour[i-1]], coordinates[tour[i]])
        calculated_total_cost += dist
        calculated_max_distance = max(calculated_max_distance, dist)
    
    if not math.isclose(calculated_total_cost, total_travel_cost, rel_tol=1e-9) or \
       not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Using given data
tour = [0, 1, 3, 4, 5, 6, 8, 9, 10, 11, 2, 7, 12, 14, 13, 0]
total_travel_cost = 447.48293528145035
maximum_distance = 48.373546489791295

# Run test
result = check_solution(tour, total_travel_cost, maximum_distance)
print(result)