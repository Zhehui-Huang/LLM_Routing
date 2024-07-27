import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, cost, max_distance):
    # City coordinates
    cities = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
        5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
        10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    
    # Requirement 1: Check if tour starts and ends at the depot city 0 and visits each city exactly once
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour[1:-1]) != sorted(list(cities.keys())[1:]):
        return "FAIL"

    # Calculate total travel cost and maximum distance between consecutive cities
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist

    # Requirement 5: Check total travel cost
    if not math.isclose(calculated_cost, cost, rel_tol=1e-2):
        return "FAIL"
    
    # Requirement 6: Check maximum distance between consecutive cities
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Given solution details
tour = [0, 4, 10, 4, 10, 4, 10, 4, 10, 4, 10, 4, 10, 4, 10, 0]
total_travel_cost = 223.90
maximum_distance = 26.57

# Verify the solution
result = verify_solution(tour, total_travel_cost, maximum_distance)
print(result)