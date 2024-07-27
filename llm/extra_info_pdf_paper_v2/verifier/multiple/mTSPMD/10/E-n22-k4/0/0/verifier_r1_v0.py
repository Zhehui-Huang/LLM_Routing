import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_solution(tour, total_cost_given):
    # City coordinates
    coordinates = {
        0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
        4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
        8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
        12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
        16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
        20: (155, 185), 21: (139, 182)
    }
    # Depots
    depots = {0, 1, 2, 3}

    # [Requirement 1] Check if tour starts and ends at a valid depot
    if tour[0] not in depots or tour[-1] not in depots:
        return "FAIL"

    # [Requirement 2] Check if each city is visited exactly once
    if sorted(tour) != sorted(list(coordinates.keys())):
        return "FAIL"

    # [Requirement 3] Calculate and verify the total travel cost
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])

    if not math.isclose(total_calculated_cost, total_cost_given, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Test the provided solution
best_tour = [1, 2, 5, 7, 9, 10, 12, 15, 18, 20, 17, 21, 19, 16, 14, 0, 13, 11, 4, 3, 8, 6, 1]
total_travel_cost = 279.6501319797536

result = verify_solution(best_tour, total_travel_cost)
print(result)