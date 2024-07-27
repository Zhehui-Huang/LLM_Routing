import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_robot_tour():
    # Maps city indices to their coordinates
    cities = {
        0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
        5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
        10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
    }
    
    # Grouping of the cities
    group0 = {2, 7, 10, 11, 14}
    group1 = {1, 3, 5, 8, 13}
    group2 = {4, 6, 9, 12}
    
    # Provided tour and total cost
    tour = [0, 10, 1, 9, 0]
    provided_cost = 122.22
    
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Compute the actual cost of the tour
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if provided cost matches computed cost accurately to two decimal places
    if not math.isclose(provided_cost, actual_cost, rel_tol=1e-2):
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = [group0, group1, group2]
    visited_from_each_group = [any(city in group for city in tour) for group in visited_groups]
    if not all(visited_from_each_group) or len([city for group in visited_groups for city in group if city in tour]) != 3:
        return "FAIL"
    
    # Verification passed
    return "CORRECT"

# Output the test result
print(test_robot_tour())