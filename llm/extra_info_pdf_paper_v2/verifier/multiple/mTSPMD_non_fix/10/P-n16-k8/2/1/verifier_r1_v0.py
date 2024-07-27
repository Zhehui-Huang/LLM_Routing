import math

# Define city coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

# Define robots and their tours
robot_tours = {
    0: [0, 10, 15, 0],
    1: [0, 12, 11, 0],
    2: [0, 4, 3, 0],
    3: [0, 8, 13, 0],
    4: [0, 9, 14, 0],
    5: [0, 7, 5, 0],
    6: [0, 1, 6, 0],
    7: [0, 2, 0]
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

def check_solution(robot_tours):
    # Check if all cities are visited exactly once
    all_visited = set()
    for tour in robot_tours.values():
        if tour[0] != 0 or (len(tour) > 1 and tour[-1] != 0):
            print("FAIL: Tour does not start or end at designated depot city 0")
            return "FAIL"
        all_visited.update(tour)

    if len(all_visited) != 16:
        print("FAIL: Not all cities are visited or some are visited more than once")
        return "FAIL"

    # Calculate total travel cost
    total_travel_cost = 0
    for tour in robot_tours.values():
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(tour[i], tour[i+1])
        print(f"Robot Tour: {tour} Total Tour Cost: {tour_cost}")
        total_travel_cost += tour_cost

    # Compare against claimed overall cost
    claimed_overall_cost = 496.7267964747708
    if abs(total_travel_cost - claimed_overall_cost) > 0.01:
        print("FAIL: Calculated total cost does not match the claimed cost")
        return "FAIL"
    
    return "CORRECT"

# Check the solution and output the result
result = check_solution(robot_tours)
print(result)