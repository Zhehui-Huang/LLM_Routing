import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_solution(tour, total_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if len(tour) != 6:  # Includes the return to the depot city
        return "FAIL"
    if len(set(tour)) != len(tour):
        return "FAIL"
  
    calculated_cost = 0
    coordinates = {
        0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80),
        4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44),
        8: (17, 69), 9: (95, 89)
    }
    
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-6):
        return "FAIL"
    return "CORRECT"

# Sample test case
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80),
    4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44),
    8: (17, 69), 9: (95, 89)
}

# Given solution to test
tour_given = [0, 4, 8, 3, 5, 0]
total_cost_given = 110.38072506104011

# Validate the tour and costs
test_result = check_solution(tour_given, total_cost_given, cities)
print(test_result)