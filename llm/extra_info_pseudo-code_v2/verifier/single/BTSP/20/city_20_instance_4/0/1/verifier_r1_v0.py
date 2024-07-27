import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cities, expected_total_cost, expected_max_distance):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour must start and end at depot city 0."
    
    if len(set(tour)) != len(cities):
        return "FAIL: Each city must be visited exactly once."
    
    if len(tour) != len(cities) + 1:
        return "FAIL: Each city must be visited exactly once, plus return to start."
    
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    if abs(total_cost - expected_total_cost) > 0.1:
        return f"FAIL: Total travel cost expected: {expected_total_context}, but got: {total_cost}"
    
    if abs(max_distance - expected_max_distance) > 0.1:
        return f"FAIL: Max distance expected: {expected_max_distance}, but got: {max_distance}"
    
    return "CORRECT"

# Given cities coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22), 
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 
    17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Test verification against provided solution
solution_tour = [0, 8, 19, 10, 17, 6, 15, 18, 4, 13, 3, 1, 11, 14, 2, 5, 9, 16, 7, 12, 0]
solution_total_cost = 870.76
solution_max_distance = 102.08

# Check correctness
result = verify_solution(solution_tour, cities, solution_total_cost, solution_max_distance)
print(result)