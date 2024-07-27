def verify_solution(tours, costs, overall_cost):
    # Constants and data setup
    depot = 0
    num_robots = 8
    all_cities = set(range(16))
    cities_visited = set()
    total_calculated_cost = 0

    # Verification functions
    def calculate_distance(p1, p2):
        import math
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    # City coordinates
    coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
        6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
    }

    if len(tours) != num_robots or len(costs) != num_robots:
        return "FAIL"
    
    for robot_id in range(num_robots):
        tour = tours[robot_id]
        calculated_cost = costs[robot_id]

        # Start and end at the depot
        if tour[0] != depot or tour[-1] != depot:
            return "FAIL"
        
        tour_cost = 0
        last_city = tour[0]
        for city in tour[1:]:
            tour_cost += calculate_distance(coordinates[last_city], coordinates[city])
            last_city = city
            cities_visited.add(city)

        if round(tour_cost, 6) != round(calculated_cost, 6):
            return "FAIL"
        
        total_calculated_cost += calculated_cost

    if cities_visited != all_cities:
        return "FAIL"

    if round(total_calculated_cost, 6) != round(overall_cost, 6):
        return "FAIL"

    return "CORRECT"

# Simulated solution output
robot_tours = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]
robot_costs = [
    27.784887978899608,
    27.784887978899608,
    27.784887978899608,
    27.784887978899608,
    27.784887978899608,
    27.784887978899608,
    27.784887978899608,
    27.784887978899608
]
total_overall_cost = 395.28504124545486

result = verify_solution(robot_tours, robot_costs, total_overall_cost)
print(result)