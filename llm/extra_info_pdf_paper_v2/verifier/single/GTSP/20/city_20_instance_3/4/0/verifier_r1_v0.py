import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, reported_cost):
    city_coordinates = {
        0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
        6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
        12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43),
        18: (53, 76), 19: (19, 72)
    }
    
    city_groups = {
        0: [4, 10, 13, 17],
        1: [6, 7, 14],
        2: [9, 12, 16],
        3: [2, 5, 15],
        4: [1, 3, 19],
        5: [8, 11, 18],
    }
    
    # Check requirement 1: Tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check requirement 2: Exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the first and last city as they are the depot
        found_group = False
        for group_id, cities in city_by_group.items():
            if city in cities:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups.add(group_id)
                found_group = True
                break
        if not found_group:
            return "FAIL"
        
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Check requirement 3: Calculate travel cost using the Euclidean distance formula
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    if abs(calculated_cost - reported_cost) > 0.01:  # Allow for rounding differences
        return "FAIL"

    return "CORRECT"

# Given tour and reported total cost
tour = [0, 4, 7, 12, 15, 3, 18, 0]
reported_cost = 227.40

# Verify the solution
result = verify_solution(tour, reported_cost)
print(result)