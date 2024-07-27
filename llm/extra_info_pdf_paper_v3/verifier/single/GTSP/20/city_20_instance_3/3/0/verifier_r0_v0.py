import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def test_solution(tour, cost):
    city_coordinates = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
        (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
        (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]
    
    city_groups = [
        [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
    ]
    
    # Requirement 1, 3, 5: Check if the tour starts and ends at depot city and visits one per group
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    visited_groups = [False] * len(city_groups)
    for city in tour[1:-1]:
        in_group = False
        for i, group in enumerate(city_groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"  # Visited a group more than once
                visited_groups[i] = True
                in_group = True
                break
        if not in_group:
            return "FAIL"  # City not in any group

    if not all(visited_groups):
        return "FAIL"  # Not all groups are visited
    
    # Requirement 2: Calculate the distance and compare with provided cost
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += euclidean_distance(city_coordinates[tour[i-1]], city_coordinates[tour[i]])
    
    if not math.isclose(calculated_cost, cost, rel_tol=1e-2):
        return "FAIL"
    
    # If all the checks are passed:
    return "CORRECT"

# Using given tour and total cost
tour = [0, 9, 1, 4, 8, 2, 6, 0]
total_travel_cost = 334.11

# Perform the test
print(test_solution(tour, total_travel_cost))