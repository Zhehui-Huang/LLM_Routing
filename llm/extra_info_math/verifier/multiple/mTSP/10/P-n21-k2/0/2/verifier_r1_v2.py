def unit_test_solution(tours, total_costs, coordinates):
    num_cities = len(coordinates)
    num_robots = len(tours)
    total_travel_cost_calculated = 0.0

    # Creating a set of all visits to ensure each city is visited exactly once
    all_visits = set()

    # Check each robot's tour
    for robot_id, tour in enumerate(tours):
        # Check if each salesman leaves the depot exactly once
        if tour.count(0) != 2 or tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Check if the tour visits new cities exactly once
        visited_cities = set(tour[1:-1])  # exclude depot in check of unique visits in the middle of the tour
        if any(city in all_visits for city in visited_cities):
            return "FAIL"
        all_visits.update(visited_cities)

        # Calculate travel cost for this robot and validate against given
        travel_cost = 0.0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            dx = coordinates[city_from][0] - coordinates[city_to][0]
            dy = coordinates[city_from][1] - coordinates[city_to][1]
            travel_cost += (dx**2 + dy**2)**0.5

        # Check calculated vs provided travel cost with a tolerance
        if not abs(travel_cost - total_costs[robot_id]) <= 1e-2:
            return "FAIL"

        total_travel_cost_calculated += travel_cost

    # Ensure coverage of all cities exactly once excluding the depot
    if len(all_visits) != num_cities - 1:  # exclude depot
        return "FAIL"

    # Validate overall total cost
    if not abs(total_travel_cost_calculated - sum(total_costs)) <= 1e-2:
        return "FAIL"

    return "CORRECT"

# Example coordinates mapping from your environment, you must provide coordinates matched to city ids.
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Robot tours and their corresponding calculated travel costs as provided
tours = [
    [0, 16, 0],
    [0, 6, 0]
]
provided_total_costs = [20.0, 24.08]

# Running the test
result = unit_test_solution(tours, provided_total_costs, coordinates)
print(result)  # Should print "CORRECT" if everything is okay, otherwise "FAIL"