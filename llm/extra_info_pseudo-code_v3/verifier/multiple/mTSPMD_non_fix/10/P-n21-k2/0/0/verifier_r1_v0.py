import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    # Coordinates of each city
    coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
        4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
        8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
        16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35)
    }

    # Tours provided
    tours = {
        0: [0, 6, 7, 5, 9, 2, 10, 4, 3, 8, 0],
        1: [1, 16, 20, 14, 17, 13, 18, 19, 12, 15, 11, 1]
    }

    # Total costs provided
    costs = {
        0: 109.88,
        1: 114.47
    }

    # Calculate total cost for each robot and check cities
    cities_visited = set()
    overall_cost_computed = 0

    for robot_id, tour in tours.items():
        start_depot = tour[0]
        
        if robot_id == 1 and start_depot != 1:
            return "FAIL: Robot starts at incorrect depot"

        # Track all visited cities
        cities_visited.update(tour)

        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])

        # Check computed total costs
        if not math.isclose(tour_cost, costs[robot_id], abs_tol=0.01):
            return f"FAIL: Incorrect cost for robot {robot_id}: Computed cost = {tour_cost}, Provided cost = {costs[robot_id]}"

        overall_cost_computed += tour_cost

    # Check if all cities are visited exactly once
    if len(cities_visited) != 21:
        return "FAIL: Not all cities are visited or some are visited multiple times"

    provided_total_cost = 224.35  # This should be sum of all robot costs if provided separately
    if not math.isclose(overall_cost_computed, provided_total_cost, abs_tol=0.01):
        return f"FAIL: Incorrect overall travel cost. Computed = {overall_cost_computed}, Provided = {provided_total_cost}"

    return "CORRECT"

# Running the test function
print(test_solution())