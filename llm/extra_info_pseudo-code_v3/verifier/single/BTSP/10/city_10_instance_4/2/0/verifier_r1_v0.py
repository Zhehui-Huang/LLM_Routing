import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def verify_solution(tour, total_travel_cost, max_distance):
    cities_coordinates = {
        0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
        5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
    }
    
    # [Requirement 1]
    if len(set(tour)) != len(cities_coordinates) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 4]
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Calculating total travel cost and maximum distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(1, len(tour)):
        city1 = tour[i - 1]
        city2 = tour[i]
        x1, y1 = cities_coordinates[city1]
        x2, y2 = cities_coordinates[city2]
        distance = euclidean_distance(x1, y1, x2, y2)
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # [Requirement 5]
    if not math.isclose(calculated_total_cost, total_travel_cost, abs_tol=0.01):
        return "FAIL"
    
    # [Requirement 6]
    if not math.isclose(calculated_max_distance, max_distance, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Given solution details
tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
total_travel_cost = 408.41360886151256
max_distance = 61.68468205316454

# Verify the solution
result = verify_solution(tour, total_travel_cost, max_distance)
print(result)