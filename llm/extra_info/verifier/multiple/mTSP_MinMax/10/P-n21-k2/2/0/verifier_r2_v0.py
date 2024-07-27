import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(robots_tours, city_coordinates):
    city_visit_count = [0] * len(city_coordinates)
    
    # Calculate and verify if tours start and end at the depot city and calculate costs
    robot_costs = []
    for tour in robots_tours:
        if tour[0] != 0 or tour[-1] != 0:
            print("Tours must start and end at the depot (City 0).")
            return "FAIL"
        cost = 0.0
        for i in range(len(tour) - 1):
            city1, city2 = tour[i], tour[i+1]
            distance = calculate_distance(city_coordinates[city1], city_coordinates[city2])
            cost += distance
            if city2 != 0:  # Exclude depot city from visit count
                city_visit_count[city2] += 1
        robot_costs.append(cost)

    # Check if every city is visited exactly once
    if any(count != 1 for count in city_visit_count[1:]):  # Don't count depot city in visits
        print("Visit count for each city should be exactly once:", city_visit_count)
        return "FAIL"

    # Check if output includes correct max cost tracking
    reported_max_cost = max(robot_costs)
    if reported_max_cost != 274.70246724401983:  # Should match provided result
        print("Reported maximum cost does not match the expected max cost.")
        return "FAIL"

    return "CORRECT"

# City coordinates including depot city at index 0
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Tours assigned to robots, consistent with the format of the solution
robots_tours = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0],
    [0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]
]

# Print correctness of the provided solution
print(check_solution(robots_tours, city_coordinates))