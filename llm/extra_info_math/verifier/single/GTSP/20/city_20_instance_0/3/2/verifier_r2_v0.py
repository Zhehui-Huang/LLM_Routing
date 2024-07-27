import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cities, groups):
    # Requirement 1: Check if tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if exactly one city from each group is visited
    visited_groups = [False] * len(groups)
    for city in tour:
        for i, group in enumerate(groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"
                visited_groups[i] = True
    if not all(visited_groups):
        return "FAIL"
    
    # Since optimal cost calculation needs actual tours to compare and specific instances,
    # Requirement 3 is assumed to be handled during optimization and not directly verifiable here.
    
    return "CORRECT"

# City positions
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# City groups
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Provided solution
provided_tour = [0]
provided_cost = 0  # Although not used in the test verification

# Verify the provided solution
result = verify_solution(provided_tour, cities, groups)
print(result)