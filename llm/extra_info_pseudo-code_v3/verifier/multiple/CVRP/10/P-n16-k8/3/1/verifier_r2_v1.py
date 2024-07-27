import numpy as np

# Constants definition
CAPACITY = 35
CITY_DEMANDS = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
DEPOT = 0
CITY_COORDINATES = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

def calculate_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Data about the provided solution
tours = [
    [0, 6, 0], [0, 1, 0, 13, 0], [0, 10, 0, 15, 0, 3, 0],
    [0, 2, 0], [0, 4, 0, 9, 0], [0, 7, 0, 12, 0],
    [0, 5, 0, 14, 0], [0, 11, 0, 8, 0]
]

robot_travel_costs = [
    12.041594578792296, 72.13332310369395, 145.58966999178884,
    21.02379604162864, 86.14759371307083, 81.95601180063203,
    84.82818892296291, 93.06017863900925
]

def verify_solution(tours, robot_travel_costs):
    # Verify that all robots start and end with the depot
    if not all(tour[0] == DEPOT and tour[-1] == DEPOT for tour in tours):
        return "FAIL"
    
    # Verify capacity constraints
    for tour in tours:
        load = 0
        for city in tour:
            if city != DEPOT:
                load += CITY_DEMANDS[city]
            if load > CAPACITY:
                return "FAIL"
    
    # Check that total demand is met
    all_city_count = [0] * len(CITY_DEMANDS)
    for tour in tours:
        for city in tour:
            if city != DEPOT:
                all_city_count[city] += 1
    
    if any(count != 1 for count in all_city_count[1:]):  # starts from 1 since depot is not considered
        return "FAIL"
    
    # Calculate and verify travel cost correctness
    calculated_total_cost = 0
    for tour in tours:
        for i in range(len(tour) - 1):
            calculated_total_cost += calculate_distance(CITY_COORDINATES[tour[i]], CITY_COORDINATES[tour[i+1]])

    if not np.isclose(calculated_total_cost, sum(robot_travel_costs)):
        return "FAIL"

    return "CORRECT"

# Perform the test
test_result = verify_solution(tours, robot_travel_costs)
print(test_result)