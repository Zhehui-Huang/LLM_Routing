import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    # City coordinates as per provided data
    cities = {
        0: (8, 11),   # Depot
        1: (40, 6),
        2: (95, 33),
        3: (80, 60),
        4: (25, 18),
        5: (67, 23),
        6: (97, 32),
        7: (25, 71),
        8: (61, 16),
        9: (27, 91),
        10: (91, 46),
        11: (40, 87),
        12: (20, 97),
        13: (61, 25),
        14: (5, 59),
        15: (62, 88),
        16: (13, 43),
        17: (61, 28),
        18: (60, 63),
        19: (93, 15)
    }

    # Groups of cities
    groups = {
        0: [1, 3, 5, 11, 13, 14, 19],
        1: [2, 6, 7, 8, 12, 15],
        2: [4, 9, 10, 16, 17, 18]
    }
    
    # Requirement 1: Tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit exactly one city from each group
    visited_groups = [0 for _ in range(3)]  # Tracks visited groups
    for city in tour[1:-1]:  # Exclude the depot
        found = False
        for group_id, city_list in groups.items():
            if city in city_list:
                visited_groups[group_id] += 1
                found = True
                break
        if not found or visited_groups[group_id] > 1:
            return "FAIL"
    if sum(visited_groups) != len(groups):
        return "FAIL"

    # Requirement 3 and 4: Correct calculation of distance and check the total cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Given solution to be verified
tour = [0, 1, 8, 4, 0]
total_cost = 110.09

# Output the result of verification
print(verify_solution(tour, total_cost))