import math

# Define the robot tours and corresponding city coordinates
tours = {
    0: [0, 6, 13, 0],
    1: [0, 1, 12, 0],
    2: [0, 10, 3, 0],
    3: [0, 2, 8, 0],
    4: [0, 4, 15, 0],
    5: [0, 7, 9, 0],
    6: [0, 5, 14, 0],
    7: [0, 11, 0]
}

city_coordinates = {
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

# Expected costs from solution
expected_costs = {
    0: 58.62628333248735,
    1: 60.014586538396706,
    2: 65.57284885461793,
    3: 65.51535209959684,
    4: 61.07512778319072,
    5: 64.13503025042893,
    6: 62.44277221633522,
    7: 56.32051136131489
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0]) ** 2 + 
                     (city_coordinates[city1][1] - city_coordinates[city2][1]) ** 2)

# Function to calculate tour costs
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(tour[i], tour[i+1])
    return cost

# Check if each city is visited exactly once
all_visited_cities = sum([tour[1:-1] for tour in tours.values()], [])
unique_visited_cities = set(all_visited_cities)

# Check all requirements for 'CORRECT' outcome
def unit_tests():
    try:
        # Check that each city is visited exactly once
        if len(all_visited_cities) != 16 or len(unique_visited_cities) != 16:
            return "FAIL"

        # Check that tours match expected travel costs
        for robot_id, tour in tours.items():
            calculated_cost = calculate_tour_cost(tour)
            if not math.isclose(calculated_cost, expected_costs[robot_id], rel_tol=1e-5):
                return "FAIL"
        return "CORRECT"
    except Exception as e:
        return "FAIL"

# Run unit tests
print(unit_tests())