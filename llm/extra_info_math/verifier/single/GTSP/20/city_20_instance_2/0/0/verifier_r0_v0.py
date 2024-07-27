import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    # Cities coordinates
    cities = {
        0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
        5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
        10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49),
        14: (18, 49), 15: (64, 41), 16: (28, 49), 17: (91, 94),
        18: (51, 58), 19: (30, 48)
    }
    
    # City groups
    groups = [
        [7, 10, 11, 12],
        [3, 8, 13, 16],
        [2, 4, 15, 18],
        [1, 9, 14, 19],
        [5, 6, 17]
    ]
    
    # Provided solution
    tour = [0, 12, 0]
    reported_cost = 28.844410203711913
    
    # [Requirement 1] Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
        
    # [Requirement 2] Check exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:
        for i, group in enumerate(groups):
            if city in group:
                visited_groups.add(i)
                
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # [Requirement 3] Check if the tour cost is minimized correctly
    # Calculate actual tour cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if abs(actual_cost - reported_cost) > 1e-6:
        return "FAIL"
        
    return "CORRECT"

# Output the result of the test
print(test_solution())