import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_solution(tour, total_cost, max_distance):
    # City coordinates
    cities = [
        (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
        (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
        (18, 49), (64,41), (28, 49), (91, 94), (51, 58), (30, 48)
    ]
    
    # [Requirement 1] Check if the tour starts and ends at depot city 0 and visits each city exactly once:
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour) != sorted(set(tour)):
        return "FAIL"
    
    # Calculate the actual total travel cost and max distance
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        actual_total_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance
    
    # [Requirement 3] Check the total cost and max distance
    if not (abs(actual_total_cost - total_cost) < 1e-6 and abs(actual_max_distance - max_distance) < 1e-6):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
total_cost = 478.4306776278287
max_distance = 80.61017305526642

# Call test function and print result
result = test_solution(tour, total_cost, max_distance)
print(result)