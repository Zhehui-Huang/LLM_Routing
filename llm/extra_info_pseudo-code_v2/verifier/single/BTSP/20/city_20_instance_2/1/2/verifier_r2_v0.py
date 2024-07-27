import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_requirements(tour, total_travel_cost, max_distance_between_cities):
    # Given coordinates of the cities
    coordinates = [
        (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
        (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
        (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
    ]
    
    # Requirement 1: Start and end at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once
    if sorted(tour) != sorted(list(set(tour))):
        return "FAIL"
    
    # Checking the completeness of the tour
    if set(tour) != set(range(len(coordinates))):
        return "FAIL"
    
    # Calculate distances and verify requirements 4, 6, 7
    calculated_total_cost = 0
    calculated_max_dist = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        distance = calculate_euclidean_distance(x1, y1, x2, y2)
        calculated_total_cost += distance
        if distance > calculated_max_dist:
            calculated_max_dist = distance
    
    # Requirement 6: Verify total travel cost
    if not math.isclose(calculated_total_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Requirement 7: Verify max distance between consecutive cities
    if not math.isclose(calculated_max_dist, max_distance_between_cities, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given solution details
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
total_travel_cost = 478.4306776278287
max_distance_between_cities = 80.61017305526642

# Check the solution
result = check_requirements(tour, total_travel_cost, max_distance_between_cities)
print(result)