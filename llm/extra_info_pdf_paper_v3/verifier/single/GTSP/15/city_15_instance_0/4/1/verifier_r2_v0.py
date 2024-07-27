import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_cost):
    # Positions of cities
    cities = {
        0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
        5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
        10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
    }
    
    # Groups of cities
    group_0 = {2, 7, 10, 11, 14}
    group_1 = {1, 3, 5, 8, 13}
    group_2 = {4, 6, 9, 12}
    
    # Starting and ending at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Visiting exactly one city from each group
    visited_groups = [0] * 3
    for index in tour[1:-1]:  # exclude the first and last indices (depot)
        if index in group_0:
            visited_groups[0] += 1
        elif index in group_1:
            visited_groups[1] += 1
        elif index in group_2:
            visited_groups[2] += 1
            
    if not all(v == 1 for v in visited_groups):
        return "FAIL"
    
    # Calculating the total travel cost and check with provided
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 10, 1, 9, 0]
total_cost = 122.22

# Validate solution
result = test_solution(tour, total_cost)
print(result)