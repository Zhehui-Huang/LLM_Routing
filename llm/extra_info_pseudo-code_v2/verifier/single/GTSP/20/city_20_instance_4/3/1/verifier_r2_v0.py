import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, cost):
    city_coordinates = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
        6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
        12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
        18: (64, 72), 19: (14, 89)
    }
    city_groups = [
        [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
    ]

    # Check Requirement 1: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2 and 3: One city from each group
    visited_groups = [0] * len(city_groups)  # Tracker for groups
    visited_cities = tour[1:-1]  # all visited cities, excluding starting and ending 0

    if len(visited_cities) != len(city_groups):
        return "FAIL"
    
    for city in visited_cities:
        found = False
        for i, group in enumerate(city_groups):
            if city in group:
                if visited_groups[i] == 0:
                    visited_groups[i] = 1
                    found = True
                    break
        if not found:
            return "FAIL"

    if sum(visited_groups) != len(city_groups):  # Ensure all groups are visited
        return "FAIL"

    # Check Requirement 4 and 5: Correct total travel distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        calculated_cost += calculate_distance(x1, y1, x2, y2)

    if abs(calculated_cost - cost) > 1e-4:
        return "FAIL"

    # Requirement 6 is implicitly checked by output format

    return "CORRECT"

# Provided solution
tour = [0, 5, 18, 13, 1, 14, 10, 15, 0]
cost = 266.72

print(verify_solution(tour, cost))