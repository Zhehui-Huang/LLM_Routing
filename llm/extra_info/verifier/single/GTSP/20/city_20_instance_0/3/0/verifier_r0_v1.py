import math

# City coordinates
cities = {
    0: (8, 11),
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

# City groups
city_groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Solution provided
solution_tour = [0, 1, 8, 4, 0]
solution_cost = 110.08796524611944

# Run Tests
def test_solution():
    # Test Requirement 1: Tour starts and ends at depot
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"
    
    # Test Requirement 2: Each city group is visited exactly once
    visited_groups = [0] * len(city_groups)
    
    for city in solution_tour[1:-1]:  # Excluding the depot visits
        for index, group in enumerate(city_groups):
            if city in group:
                visited_groups[index] += 1
    
    if not all(count == 1 for count in visited_groups):
        return "FAIL"
    
    # Test Requirement 3: Validate total cost
    calculated_cost = 0
    for i in range(len(solution_tour) - 1):
        calculated_cost += euclidean_distance(solution_tour[i], solution_tour[i + 1])
    
    if abs(calculated_cost - solution_cost) > 1e-5:  # Allowing a tiny error margin
        return "FAIL"

    return "CORRECT"

print(test_solution())