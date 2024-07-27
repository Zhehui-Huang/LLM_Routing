import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def calculate_total_travel_cost(cities, tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total  distance

def test_solution():
    cities = {
        0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 
        5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 
        10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 
        15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
    }
    proposed_tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 11, 10, 1, 0]
    proposed_cost = 254.73018946347761
    
    # Requirement 1: Start and end at depot city 0
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Tour must include exactly 13 cities including the depot
    if len(set(proposed_tour)) != 13:
        return "FAIL"
    
    # Requirement 3: Total travel cost should be minimized
    computed_cost = calculate_total_travel_cost([cities[i] for i in range(len(cities))], proposed_tour)
    # Upper bound allowance for floating point arithmetic issues
    if abs(computed_cost - proposed_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Output the result of the test
print(test_solution())