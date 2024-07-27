import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def test_tour(tour, total_cost):
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
        (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
        (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    groups = [[5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]]

    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group
    visited_groups = set()
    for index in tour[1:-1]:  # exclude the first and last index which are the depot
        for group_index, group in enumerate(groups):
            if index in group:
                visited_town = index
                if group_index in visited_groups:
                    return "FAIL"
                visited_groups.add(group_index)
                
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Calculate travel cost and compare with given total
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if abs(calculated_cost - total_cost) > 1e-2:  # Allow for slight floating point discrepancies
        return "FAIL"

    # If all tests pass
    return "CORRECT"

# Given solution
tour = [0, 5, 18, 13, 1, 14, 10, 15, 0]
total_cost = 266.72
result = test_tour(tour, total_cost)
print(result)