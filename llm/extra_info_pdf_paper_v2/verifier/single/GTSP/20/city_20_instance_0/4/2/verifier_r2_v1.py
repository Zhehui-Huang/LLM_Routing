import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_tour(tour, cost):
    # Test coordinates setup
    coordinates = {
        0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
        4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
        8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
        12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
        16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
    }
    
    groups = {
        0: [1, 3, 5, 11, 13, 14, 19],
        1: [2, 6, 7, 8, 12, 15],
        2: [4, 9, 10, 16, 17, 18]
    }

    # Requirement 1: Tour must start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return 'FAIL'

    # Requirement 2: Must visit exactly one city from each group
    visited_groups = [0, 0, 0]  # To track city group visit
    for city in tour[1:-1]:
        for i, group in groups.items():
            if city in group:
                visited_groups[i] += 1
    
    if not all(count == 1 for count in visited_groups):
        return 'FAIL'
    
    # Requirement 3: Compute and check the travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        x1, y1 = coordinates[city1]
        x2, y2 = coordinates[city2]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        return 'FAIL'

    return 'CORRECT'  # Requirements are met

# Given test case
tour = [0, 1, 8, 4, 0]
total_cost = 110.08796524611944
result = verify_tour(tour, total_cost)

print(result)  # Output: "CORRECT" or "FAIL"