import math

# City coordinates
cities = {
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
    21: (139, 182),
}

# Tours and distances provided
solutions = {
    'Robot 0': ([0, 12, 13, 14, 15, 16, 18, 0], 152.95),
    'Robot 1': ([0, 1, 2, 3, 4, 0], 131.29),
    'Robot 2': ([0, 5, 6, 7, 8, 9, 10, 11, 0], 168.61),
    'Robot 3': ([0, 17, 19, 20, 21, 0], 116.66)
}

# Helper function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Test to verify the solution
def verify_solution(solutions):
    visited_cities = set()
    max_travel_cost = 0
    for robot, (tour, total_travel_cost) in solutions.items():
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL: Tour does not start and end at the depot.")
            return
        calculated_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        if not math.isclose(calculated_cost, total_travel_cost, abs_tol=0.01):
            print(f"FAIL: Calculated travel cost does not match for {robot}.")
            return
        visited_cities.update(tour[1:-1])  # Exclude the depot city from what should be collected
        if max_travel_cost < total_travel_cost:
            max_travel_cost = total_travel_cost

    if visited_cities != set(range(1, 22)):  # Checking if all cities except depot are visited exactly once
        print("FAIL: Not all cities are visited or some are visited more than once.")
        return
    if not math.isclose(max_travel_cost, 168.61, abs_tol=0.01):
        print("FAIL: Maximum travel cost is incorrect.")
        return
    print("CORRECT")

verify_solution(solutions)