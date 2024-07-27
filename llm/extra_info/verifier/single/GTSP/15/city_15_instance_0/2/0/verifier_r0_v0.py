import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tour(tour, total_cost):
    # City coordinates
    city_positions = {
        0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50),
        4: (21, 23), 5: (88, 59), 6: (79, 77), 7: (63, 23),
        8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
        12: (3, 21), 13: (60, 55), 14: (4, 39)
    }
    
    # City groups
    groups = {
        0: [2, 7, 10, 11, 14],
        1: [1, 3, 5, 8, 13],
        2: [4, 6, 9, 12]
    }
    
    # Requirement 1: Check start and end at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check exactly one city from each group
    unique_cities = set(tour[1:-1])  # Exclude the depot repeats
    group_check = all(any(city in group for city in unique_cities) for group in groups.values())
    if not group_check or len(unique_cities) != 3:
        return "FAIL"
    
    # Requirement 3: Check travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(
            city_positions[city1][0], city_positions[city1][1],
            city_positions[city2][0], city_positions[city2][1]
        )
    
    if abs(calculated_cost - total_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Provided Tour and Cost
tour = [0, 10, 1, 9, 0]
total_cost = 122.21527940040238

# Verification
result = verify_tour(tour, total_cost)
print(result)