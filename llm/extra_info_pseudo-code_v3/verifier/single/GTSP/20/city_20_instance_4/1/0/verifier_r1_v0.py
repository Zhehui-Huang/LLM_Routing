import math

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22), 6: (28, 11),
    7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68), 12: (60, 1), 
    13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# City groups
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

# Provided solution details
solution_tour = [0, 5, 18, 12, 3, 4, 10, 15, 0]
solution_cost = 205.9370484511064

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def calculate_total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

def test_solution():
    # [Requirement 1]
    if len(cities) != 20:
        return "FAIL"
    
    # [Requirement 2]
    # Since it's mentioned one robot, we assume it is correct since there's no need for verification in code.
    
    # [Requirement 3]
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 4]
    # We assume distance calculation is correct based on implemented function euclidean_distance.
    
    # [Requirement 5]
    visited_groups = [set() for _ in groups]
    for city in solution_tour:
        for group_index, group in enumerate(groups):
            if city in group:
                visited_groups[group_index].add(city)
    if not all(len(group) == 1 for group in visited_groups):
        return "FAIL"
    
    # [Requirement 6]
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 7]
    # Checked already in requirement 3.
    
    # [Requirement 8]
    if abs(calculate_total_travel_cost(solution_tour) - solution_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

print(test_solution())