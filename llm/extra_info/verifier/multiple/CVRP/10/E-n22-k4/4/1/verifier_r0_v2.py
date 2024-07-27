import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(robots_tours, robots_costs, overall_cost, city_demands, city_coordinates, robot_capacity):
    total_delivered = [0] * len(city_demands)
    calculated_overall_cost = 0

    # Verify each robot's tour
    for robot_id, tour in enumerate(robots_tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tours must start and end at the depot"

        robot_load = 0
        previous_city = tour[0]
        calculated_cost = 0
        for current_city in tour[1:]:
            # Calculate travel cost and accumulate
            distance = calculate_euclidean_distance(*city_coordinates[previous_city], *city_coordinates[current_city])
            calculated_cost += distance
            previous_city = current_city
            
            # Accumulate the load
            if current_city != 0:  # Ignoring depot city for load
                robot_load += city_demands[current_city]

        # Compare calculated route cost with provided cost
        if abs(calculated_cost - robots_costs[robot_id]) > 0.01:
            return "FAIL: Incorrect computed travel cost for Robot {}".format(robot_id)

        # Accumulate overall cost
        calculated_overall_cost += calculated_cost

        # Verify load does not exceed capacity
        if robot_load > robot_capacity:
            return "FAIL: Capacity exceeded for Robot {}".format(robot_id)

        # Record deliveries for demand check
        for city in tour:
            if city != 0:  # Ignoring depot city for delivery check
                total_delivered[city] += city_demands[city]

    # Check all demands are met
    if not all(delivered >= demand for delivered, demand in zip(total_delivered, city_demands)):
        return "FAIL: Not all city demands are met"

    # Verify overall cost
    if abs(calculated_overall_cost - overall_cost) > 0.01:
        return "FAIL: Incorrect total travel cost"

    return "CORRECT"

# Scenario
city_coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
                    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
                    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)]
city_demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

robots_capacity = 6000

robots_tours = [[0, 0], [0, 0], [0, 0], [0, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
robots_costs = [0.0, 0.0, 0.0, 445.37]
overall_cost = 445.37

# Now run the test
result = verify_solution(robots_tours, robots_costs, overall_cost, city_demands, city_coordinates, robots_capacity)
print(result)