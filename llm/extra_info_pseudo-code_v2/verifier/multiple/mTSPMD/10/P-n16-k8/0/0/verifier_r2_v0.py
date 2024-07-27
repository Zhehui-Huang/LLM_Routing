import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Solution provided
robots_tours = {
    0: [0, 10, 0], 1: [1, 12, 1], 2: [2, 13, 2], 3: [3, 8, 3],
    4: [4, 11, 4], 5: [5, 14, 5], 6: [6, 9, 6], 7: [7, 15, 7]
}

# Travel costs provided
robots_travel_costs = {
    0: 41.62, 1: 32.31, 2: 18.11, 3: 15.62,
    4: 14.42, 5: 16.97, 6: 40.05, 7: 63.53
}

# Validate requirements
def validate_requirements():
    visited_cities = set()
    overall_cost_calculated = 0.0

    for robot_id, tour in robots_tours.items():
        # Check if each tour starts and ends at the assigned depot
        if tour[0] != robot_id or tour[-1] != robot_id:
            return "FAIL"

        # Check if all cities are visited exactly once
        for city in tour[1:-1]:  # Exclude depots at the start/end
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)

        # Calculate and validate the travel cost for each tour
        tour_cost_calculated = 0.0
        for i in range(len(tour) - 1):
            tour_cost_calculated += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        
        # Check if the calculated cost matches the provided cost (rounded to two decimal places)
        if not math.isclose(tour_cost_calculated, robots_travel_costs[robot_id], abs_tol=0.01):
            return "FAIL"

        overall_cost_calculated += tour_cost_calculated

    # Check if all cities were visited exactly once
    if len(visited_cities) != 8:
        return "FAIL"

    # Check the overall total cost
    provided_total_cost = sum(robots_travel_costs.values())
    if not math.isclose(overall_cost_calculated, provided_total_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Run validation
result = validate_requirements()
print(result)