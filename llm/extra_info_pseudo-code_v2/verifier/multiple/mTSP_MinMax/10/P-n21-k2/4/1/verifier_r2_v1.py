import math

# Coordinates of cities including the depot city (city 0).
CITIES = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 
    18: (62, 63), 19: (63, 69), 20: (45, 35)
}

ROBOT_TOURS = {
    0: [0, 1, 2, 3, 4, 5, 0],
    1: [0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]
}

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = CITIES[city1]
    x2, y2 = CITIES[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def test_solution(tours):
    """Perform tests on the solution."""
    all_cities_visited = set(range(1, len(CITIES)))  # All cities excluding the depot
    cost_verification_passed = True
    costs = []

    for robot, tour in tours.items():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Each tour must start and end at the depot."
        
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(tour[i], tour[i + 1])
            if i != 0:  # Exclude adding the depot multiple times
                all_cities_visited.discard(tour[i])

        costs.append(cost)

    if all_cities_visited:
        return "FAIL: Not all cities are visited exactly once."

    max_cost = max(costs)
    if abs(max_cost - 348.1448530084161) > 1e-3:
        return "FAIL: The max cost does not match the expected."

    return "CORRECT"

# Test the solution
test_result = test_solution(ROBOT_TOURS)
print(test_result)