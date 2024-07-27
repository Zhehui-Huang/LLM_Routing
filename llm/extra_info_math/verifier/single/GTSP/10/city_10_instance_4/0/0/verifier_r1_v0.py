import math

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two points (x1, y1) and (x2, y2). """
    return round(math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2), 2)

def verify_solution(tour, city_positions, groups):
    # Requirement 2: Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Collect one city from each group as visited
    visited_from_groups = set()
    for city in tour[1:-1]:  # Exclude the depot from the check
        for group_index, group in enumerate(groups):
            if city in group:
                visited_from_groups.add(group_index)
                break
    
    # Requirement 1: Check if exactly one city from each group is visited
    if len(visited_from_groups) != len(groups):
        return "FAIL"
    
    # Requirement 3: Verify the reported total travel cost using Euclidean distance
    calculated_cost = 0.0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]])
    
    if abs(calculated_cost - 35.61) > 0.01:  # Allow some floating point rounding differences
        return "FAIL"
    
    return "CORRECT"

# City coordinates
city_positions = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Groups of cities
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Provided tour and reported cost
tour = [0, 3, 0]
reported_cost = 35.61

# Verify the solution
result = verify_solution(tour, city_positions, groups)
print(result)