import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cost):
    # Setup: City coordinates and city groups
    cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]
    groups = [[5, 6, 7], [2, 3], [1, 9], [4, 8]]
    
    # Constraints checks
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if len(tour) != 6:  # Tour length: Start, one city from each group (4 groups), return
        return "FAIL"
    if not all(tour[i] in set(group) for i, group in zip(range(1, 5), groups)):
        return "FAIL"
    
    # Calculate the tour cost and validate
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if abs(calculated_cost - cost) > 1e-2:
        return "FAIL"

    return "CORRECT"

# Given solution details
tour_solution = [0, 5, 2, 9, 8, 0]
total_cost_solution = 183.99

# Verification of the provided tour and cost
result = verify_solution(tour_solution, total_cost_solution)
print(result)