import math

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def verify_tours_and_costs(robot_tours, city_coordinates):
    cities_visited = set()
    tours_cost = []

    # Verifying each tour
    for tour in robot_tours:
        total_distance = 0
        # Tour starts and ends at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start and end at depot"

        # Check distances between consecutive cities and collect visited cities
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i+1]
            distance = calculate_distance(city_coordinates[city_from], city_coordinates[city_to])
            total_distance += distance
            if city_to != 0:  # Exclude depot from unique city check
                cities_visited.add(city_to)

        tours_cost.append(total_distance)

    # All non-depot cities must be visited exactly once
    if len(cities_visited) != len(city_coordinates) - 1:
        return "FAIL: Not all cities are visited exactly once or are visited multiple times"

    # Maximum distance should match the specified maximum
    specified_max_distance = max(tours_1_cost, tours_2_cost)
    calculated_max_distance = max(tours_cost)

    if not math.isclose(specified_max_distance, calculated_max_distance, rel_tol=1e-9):
        return "FAIL: Incorrect maximum travel cost"

    return "CORRECT"

# City coordinates and robot tours based on the provided solution
cities = {
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

tours_1 = [0, 1, 10, 14, 12, 7, 16, 2, 13, 18, 0]
tours_1_cost = 165.25479851099098

tours_2 = [0, 15, 5, 9, 17, 8, 3, 11, 4, 6, 0]
tours_2_cost = 166.15823083423138

result = verify_tours_and_costs([tours_1, tours_2], cities)
max_cost = max(tours_1_cost, tours_2_cost)

output = f"Robot 0 Tour: {tours_1}\nRobot 0 Total Travel Cost: {tours_1_cost}\n" \
         f"Robot 1 Tour: {tours_2}\nRobot 1 Total Travel Cost: {tours_2_cost}\n" \
         f"Maximum Travel Cost: {max_cost}\nVerification Result: {result}"

print(output)