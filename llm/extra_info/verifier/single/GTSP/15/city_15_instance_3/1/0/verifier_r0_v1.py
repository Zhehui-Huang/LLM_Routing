import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    # Coordinates of all cities
    city_coords = {
        0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
        5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
        10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
    }
    
    # City groups
    city_groups = {
        0: [1, 6, 14],
        1: [5, 12, 13],
        2: [7, 10],
        3: [4, 11],
        4: [2, 8],
        5: [3, 9]
    }
    
    # Requirements
    # Requirement 1: The robot must start and end its tour at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The robot needs to visit exactly one city from each group of cities.
    visited_groups = set()
    for city in tour[1:-1]:  # ignore the depot city in start and end
        found_group = False
        for group_id, cities in city_groups.items():
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
    
    # Calculate and verify total tour cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
    if abs(calculated_cost - total_cost) > 1e-2:  # allowing small floating point precision issues
        return "FAIL"
    
    return "CORRECT"

# Provided tour and cost
tour = [0, 14, 5, 10, 11, 8, 9, 0]
total_cost = 166.76

# Verify the solution
result = verify_solution(tour, total_cost)
print(result)