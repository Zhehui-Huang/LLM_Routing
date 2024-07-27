import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution():
    # Provided cities' coordinates
    cities = [
        (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
        (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
        (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
    ]
    
    # Provided tour
    tour = [0, 9, 7, 2, 5, 12, 4, 11, 6, 10, 8, 14, 3, 1, 13, 0]
    
    # Provided costs
    calculated_total_cost = 404.1488964044057
    calculated_max_distance = 35.77708763999664
    
    # Verify Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify Requirement 2
    if len(set(tour)) != len(cities) or len(tour) != len(cities) + 1:
        return "FAIL"
    
    # Compute and verify Requirements 3, 6, and 7
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        distance = euclidean_distance(x1, y1, x2, y2)
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
            
    if not (abs(total_cost - calculated_total_cost) < 0.0001 and abs(max_distance - calculated_max_distance) < 0.0001):
        return "FAIL"
    
    return "CORRECT"

# Running the test
result = test_solution()
print(result)