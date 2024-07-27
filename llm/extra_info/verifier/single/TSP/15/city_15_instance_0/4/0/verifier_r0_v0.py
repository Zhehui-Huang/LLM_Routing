import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, total_cost):
    # Cities coordinates (including depot)
    cities = {
        0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
        5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
        10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
    }
    
    # [Requirement 1] Check starting and ending at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check each city is visited exactly once, except depot city
    visited = set(tour)
    if len(visited) != len(cities) or set(cities.keys()) != visited:
        return "FAIL"
    
    # [Requirement 3] and [Requirement 4] Calculate total distance and compare
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # [Requirement 5] Check total numbers of cities
    if len(cities) != 15:
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
total_travel_cost = 373.97393412233544

# Verify the solution
result = verify_solution(tour, total_travel_cut)
print(result)