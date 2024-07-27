import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost):
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # [Requirement 1] Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if all other cities are visited exactly once
    if sorted(tour[1:-1]) != list(range(1, 10)):
        return "FAIL"
    
    # [Requirement 3 & 5] Check the total cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        calculated_cost += euclidean_distance(x1, y1, x2, y2)
    
    if abs(calculated_cost - total_cost) > 1e-6:  # Include tolerance for float precision issues
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 7, 1, 4, 2, 5, 6, 9, 3, 8, 0]
total_travel_cost = 294.17253892411236

# Test the solution
result = verify_solution(tour, total_travel_test)
print(result)