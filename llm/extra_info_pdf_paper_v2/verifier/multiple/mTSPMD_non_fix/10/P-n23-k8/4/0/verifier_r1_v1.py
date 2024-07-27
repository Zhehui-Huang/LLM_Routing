def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities based on given coordinates."""
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5

def verify_solution(tours, city_coordinates, required_costs):
    all_visited_cities = set()

    for robot_index, tour in enumerate(tours):
        if tour[0] != 0:
            return "FAIL"  # Check if all tours start at the depot 0

        last_city = tour[0]
        total_robot_cost = 0

        # Confirm that every subsequent city in the tour is visited only once
        visited_cities = set([last_city])

        for city in tour[1:]:
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)
            all_visited_cities.add(city)

            # Calculate the travel cost for the segment
            total_robot_cost += calculate_distance(city_coordinates[last_city], city_coordinates[city])
            last_city = city

        # Validate if the robot's computed travel cost matches the provided costs within a small margin
        if not (abs(total_robot_cost - required_costs[robot_index]) < 0.01):
            return "FAIL"

    # Confirm that all cities are visited exactly once
    if len(all_visited_cities) != 23:  # There are 23 cities in total
        return "FAIL"

    return "CORRECT"

# Coordinates of cities from the task description
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Tours provided in the solution
robot_tours = [
    [0, 5, 3, 12, 0],
    [0, 16, 2, 17, 0],
    [0, 10, 7, 14, 0],
    [0, 11, 4, 8, 0],
    [0, 22, 1, 15, 0],
    [0, 21, 6, 13, 0],
    [0, 9, 19, 0],
    [0, 20, 18, 0]
]

# Costs provided in the solution
required_costs = [63.57, 41.40, 54.91, 61.68, 67.38, 29.90, 59.08, 48.57]

# Perform the verification
result = verify_solution(robot_tours, city_coordinates, required_costs)
print(result)