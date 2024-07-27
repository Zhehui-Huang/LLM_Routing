import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def validate_tour(tour, distances, expected_total_distance):
    # Validate Requirement 1: start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Validate Requirement 2: each other city visited exactly once
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != 14 or any(city not in range(1, 15) for city in visited_cities):
        return "FAIL"
    
    # Validate Requirement 4: list indicating the order of cities
    if not all(isinstance(city, int) and city >= 0 for city in tour):
        return "FAIL"
    
    # Validate Requirement 3 & 5: Calculated distances using Euclidean formula and sum up to total
    calculated_total_distance = 0
    for i in range(len(tour) - 1):
        calculated_total_distance += calculate_euclidean_distance(*distances[tour[i]], *distances[tour[i+1]])
    
    if not math.isclose(calculated_total_distance, expected_total_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates including the depot
city_coordinates = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Given tour and its reported total cost
tour = [0, 13, 10, 8, 14, 3, 6, 11, 12, 4, 7, 2, 5, 9, 1, 0]
reported_total_cost = 324.91232585922467

# Verification
result = validate_tour(tour, city_coordinates, reported_total_cost)
print(result)