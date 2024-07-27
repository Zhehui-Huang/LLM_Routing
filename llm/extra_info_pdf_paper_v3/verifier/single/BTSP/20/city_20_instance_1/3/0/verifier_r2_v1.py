import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, coordinates, expected_total_cost, expected_max_distance):
    # Checks the starting and ending at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Checks that all cities are visited exactly once (plus the return to the depot)
    if len(tour) != len(coordinates) + 1:
        return "FAIL"
    
    visited = set(tour)
    if len(visited) != len(coordinates):
        return "FAIL"
    
    total_cost = 0
    max_distance = 0
    
    # Calculate the total cost and the maximum distance between consecutive cities
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        x1, y1 = coordinates[city1]
        x2, y2 = coordinates[city2]
        distance = calculate_euclidean_distance(x1, y1, x2, y2)
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Check against expected values with a tolerance for floating point arithmetic
    if not math.isclose(total_cost, expected_total_test, rel_tol=1e-2):
        return "FAIL"
    if not math.isclose(max_distance, expected_max_distance, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Define the cities' coordinates
cities_coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

# Provided solution
tour_solution = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
total_travel_cost_solution = 477.05
max_distance_solution = 87.46

# Verify the provided solution
result = verify_solution(tour_solution, cities_coordinates, total_travel_cost_solution, max_distance_solution)
print(result)