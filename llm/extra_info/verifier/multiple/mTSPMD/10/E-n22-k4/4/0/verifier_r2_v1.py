import math

# Given solution data
robots_tours = {
    0: [0, 16, 12, 8, 4, 20, 0],
    1: [1, 5, 9, 13, 17, 21, 1],
    2: [2, 6, 10, 14, 18, 2],
    3: [3, 11, 7, 15, 19, 3]
}

robots_costs = {
    0: 177.49,
    1: 196.44,
    2: 149.69,
    3: 196.84
}

cities_and_coordinates = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Check each robot starts and ends at its depot city
def check_requirement_1():
    for robot, tour in robots_tours.items():
        if tour[0] != robot or tour[-1] != robot:
            return False
    return True

# Check every city is visited exactly once
def check_requirement_2():
    all_cities_visited = [city for tour in robots_tours.values() for city in tour if city not in [0, 1, 2, 3]]
    return len(set(all_cities_visited)) == 18 and len(all_cities_visited) == 18

# Check that the reported costs match the calculated costs
def check_requirement_3():
    for robot, tour in robots_tours.items():
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += calculate_euclidean_distance(cities_and_coordinates[tour[i]], cities_and_coordinates[tour[i+1]])
        if not math.isclose(total_cost, robots_costs[robot], abs_tol=0.01):
            return False
    return True

def verify_solution():
    if check_requirement_1() and check_requirement_2() and check_requirement_3():
        return "CORRECT"
    else:
        return "FAIL"

# Output verification result
verification_result = verify_solution()
print(verification_result)