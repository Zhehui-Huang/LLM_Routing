import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_travel_cost):
    # Coordinates of the cities
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
    
    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]
    if len(tour) != 8 or len(set(tour)) != 8:
        return "FAIL"
    
    # [Requirement 4]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate total distance and compare with given travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # [Requirement 3 and 5]
    if abs(calculated_cost - total_travel_cost) > 1e-2:  # allow some small numerical error
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 8, 3, 7, 1, 4, 2, 0]
total_travel_cost = 173.18

# Verify the solution
result = verify_solution(tour, total_travel_cost)
print(result)