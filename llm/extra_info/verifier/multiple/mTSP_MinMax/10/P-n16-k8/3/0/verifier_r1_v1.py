import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tours, coordinates):
    # Check Requirement 1: Every city is visited exactly once, excluding depot
    visited = set()
    all_cities = set(range(1, 16))  # cities from 1 to 15

    for tour in tours:
        # Check Requirement 2: Each tour starts and ends at the depot city (0)
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        for city in tour[1:-1]:  # exclude depot at start/end in verification
            if city in visited:
                return "FAIL"
            visited.add(city)

    if visited != all_cities:
        return "FAIL"

    # Check Requirement 3: Minimize the maximum distance traveled by any robot
    max_cost = 0
    for tour in tours:
        tour_cost = 0
        previous_city = tour[0]
        for city in tour[1:]:
            tour_cost += calculate_distance(coordinates[previous_city], coordinates[city])
            previous_city = city
        max_cost = max(max_cost, tour_cost)

    # Known best max cost from the task provided solutions
    known_max_cost = 72.82  # this should be known or calculated prior

    if max_cost > known_max_cost:
        return "FAIL"

    return "CORRECT"

# Coordinates provided in the initial problem statement
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Tours from the provided solution
tours = [
    [0, 13, 9, 0],
    [0, 15, 12, 0],
    [0, 6, 0],
    [0, 4, 11, 0],
    [0, 5, 14, 0],
    [0, 8, 3, 0],
    [0, 1, 10, 0],
    [0, 2, 7, 0]
]

result = verify_solution(tours, coordinates)
print(result)  # Output "CORRECT" if solution is valid, otherwise "FAIL"