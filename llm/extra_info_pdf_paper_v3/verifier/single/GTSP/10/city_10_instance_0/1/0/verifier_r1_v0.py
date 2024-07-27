import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, total_cost):
    cities = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    groups = [
        [1, 2, 6],
        [3, 7, 8],
        [4, 5, 9]
    ]
    
    # Check Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2
    visited_groups = set()
    for city in tour[1:-1]:
        for idx, group in enumerate(groups):
            if city in group:
                visited_groups.add(idx)
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Check Requirement 3 & Requirement 4
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        
    if not (abs(calculated_cost - total_cost) < 1e-5):
        return "FAIL"
    
    return "CORRECT"

# Provided solution test
tour = [0, 6, 7, 5, 0]
total_cost = 74.94753083872993
result = check_solution(tour, total_cost)
print(result)  # Output should be "CORRECT"