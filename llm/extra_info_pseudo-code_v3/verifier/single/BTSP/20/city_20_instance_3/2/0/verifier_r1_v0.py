import math

# Given cities' coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

def verify_tour(tour, expected_total_cost, expected_max_distance):
    # Check if first and last cities are the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if contains all cities exactly once, except the depot which must appear twice
    all_cities = list(range(20))
    if sorted(tour[:-1]) != all_cities:
        return "FAIL"
    
    # Check total travel cost and max distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    # Adjust precision for comparison to avoid floating-point inaccuracies
    if not (abs(total_cost - expected_total_cost) < 1e-6 and abs(max_distance - expected_max_distance) < 1e-6):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
solution_tour = [0, 1, 3, 5, 2, 6, 13, 19, 15, 17, 16, 9, 11, 10, 4, 7, 14, 8, 12, 18, 0]
solution_total_cost = 506.9319561529173
solution_max_distance = 41.0

# Run verification
result = verify_tour(solution_tour, solution_total_cost, solution_max_distance)
print(result)