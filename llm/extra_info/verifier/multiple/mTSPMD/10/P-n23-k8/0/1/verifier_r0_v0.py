import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_solution():
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
        8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
    }
    robots = {
        0: [0, 21, 0],
        1: [1, 16, 10, 1],
        2: [2, 13, 2],
        3: [3, 8, 18, 19, 12, 3],
        4: [4, 11, 15, 4],
        5: [5, 22, 17, 14, 5],
        6: [6, 20, 6],
        7: [7, 9, 7]
    }
    # Requirement 1: Start-end at the same depot
    for robot_id, tour in robots.items():
        if tour[0] != tour[-1]:
            return "FAIL"

    # Requirement 2: Each city visited exactly once
    all_visited_cities = sum(robots.values(), [])
    if len(set(all_visited_cities)) != len(all_visited_cities):
        return "FAIL"

    # Requirement 3 and 6: Correct computation of travel cost
    reported_costs = [4.47, 24.86, 18.11, 50.55, 26.48, 27.25, 13.42, 20.1]
    total_cost = 0
    for robot_id, tour in robots.items():
        tour_cost = 0
        for i in range(len(tour) - 1):
            dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
            tour_cost += dist
        total_cost += tour_cost
        if not math.isclose(tour_cost, reported_costs[robot_id], abs_tol=0.01):
            return "FAIL"

    # Requirement 7: Include all cities
    if set(all_visited_cities) != set(range(23)):
        return "FAIL"

    # Check calculated vs. reported overall cost
    if not math.isclose(total_cost, sum(reported_costs), abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Running the tests
result = check_solution()
print(result)