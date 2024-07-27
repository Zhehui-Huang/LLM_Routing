import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    # City coordinates
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    
    # City groups
    groups = [
        [5, 6, 7],
        [2, 3],
        [1, 9],
        [4, 8]
    ]
    
    # Tour provided in the solution
    solution_tour = [0, 9, 5, 3, 8, 0]
    reported_cost = 169.94
    
    # Test 1: Check if the tour starts and ends at the depot
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"
    
    # Test 2: Check if exactly one city from each group is visited
    visited_groups = [False] * len(groups)
    for i in range(1, len(solution_tour) - 1):  # exclude the depot at the start and end
        city = solution_tour[i]
        for index, group in enumerate(groups):
            if city in group:
                if visited_groups[index] == True:
                    return "FAIL"
                visited_groups[index] = True
    
    if not all(visited_groups):
        return "FAIL"
    
    # Test 3: Calculate and validate the total travel cost
    calculated_cost = 0
    for i in range(len(solution_tour) - 1):
        city1, city2 = solution_tour[i], solution_tour[i + 1]
        calculated_cost += euclidean_distance(cities[city1], cities[city2])
    
    if abs(calculated_cost - reported_cost) > 0.01:  # allow for a small rounding error
        return "FAIL"
    
    # If all tests passed
    return "CORRECT"

# Run the test function and print the result
print(test_solution())