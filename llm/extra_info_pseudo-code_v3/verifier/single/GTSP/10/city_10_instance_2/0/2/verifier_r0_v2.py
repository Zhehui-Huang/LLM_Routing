import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, total_cost):
    # City coordinates
    cities = {0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
              5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)}
    
    # City groups (each group must have at least one visited city)
    groups = [{3, 6}, {5, 8}, {4, 9}, {1, 7}, {2}]
    
    # Check tour starting and ending at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check exactly one city from each group is visited
    visited_groups = [set() for _ in range(len(groups))]
    for city in tour:
        for index, group in enumerate(groups):
            if city in group:
                visited_groups[index].add(city)
    
    if not all(len(group) == 1 for group in visited_groups):
        return "FAIL"
    
    # Calculate the total travel cost and compare
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(computed_cost, total_cost, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 3, 5, 9, 1, 2, 0]
total_cost = 281.60273931778477

# Check if the provided solution meets all the requirements
result = check_solution(tour, total_cost)
print(result)