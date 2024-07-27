import math

# Cities coordinates indexed by city number
cities_coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Tours assigned to robots
robot_tours = {
    0: [13, 8, 17, 10, 4, 11],
    1: [0, 15, 16, 3, 2, 14],
    2: [0, 7, 9, 6, 18, 5, 12]
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities_coordinates[city1][0] - cities_coordinates[city2][0])**2 + (cities_coordinates[city1][1] - cities_coordinates[city2][1])**2)

# Verify each robot starts from the depot
def check_starts_from_depot(robot_tours):
    starts_correctly = all(tour[0] == 0 for tour in robot_tours.values())
    return starts_correctly

# Verify each robot visits cities exactly once between them collectively
def check_all_cities_visited_exactly_once(robot_tours):
    all_visited = set()
    for tour in robot_tours.values():
        all_visited.update(tour)
    return len(all_visited) == len(cities_coordinates) and len(set(all_visited)) == len(all_visited)

# Verify total travel cost calculations by comparing with given tours
def check_travel_costs(robot_tours):
    expected_costs = {0: 87.02701069410152, 1: 121.6958803870187, 2: 101.25690017308477}
    calculated_costs = {}
    
    for robot_id, tour in robot_tours.items():
        total_cost = 0
        for i in range(1, len(tour)):
            total_cost += calculate_distance(tour[i-1], tour[i])
        calculated_costs[robot_id] = total_cost

    # Using a tolerance to handle float comparison issues
    return all(abs(calculated_costs[robot_id] - expected_costs[robot_id]) < 1e-4 for robot_id in robot_tours)

# Run tests
def run_tests():
    if not check_starts_from_depot(robot_tours):
        return "FAIL: Starting cities are incorrect"
    if not check_all_cities_visited_exactly_once(robot_tours):
        return "FAIL: Not all cities are visited or some are visited more than once"
    if not check_travel_costs(robot_tours):
        return "FAIL: Travel cost calculations are incorrect"
    return "CORRECT"

# Output test results
print(run_tests())