import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, total_cost, cities, groups):
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group
    visited_groups = []
    for city_index in tour[1:-1]:  # exclude the initial and final depot city
        found_group = False
        for group_index, group in enumerate(groups):
            if city_index in group:
                if group_index in visited_groups:
                    return "FAIL"
                visited_groups.append(group_index)
                found_group = True
                break
        if not found_group:
            return "FAIL"
    
    if len(visited_groups) != 5:
        return "FAIL"
    
    # Requirement 3: Correct calculation of the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(total_cost, calculated_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates (index corresponds to city number)
cities = [
    (3, 26),  # Depot
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

# Define groups
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Solution to test
solution_tour = [0, 11, 16, 18, 19, 6, 0]
solution_total_cost = 162.38

# Test the solution
test_result = check_solution(solution_tour, solution_total_cost, cities, groups)
print(test_result)