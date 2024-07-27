import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(robot_tours, robot_costs, expected_total_cost):
    # Define the coordinates for each city
    city_coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
        15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
    }
    
    all_cities_visited = set()
    total_calculated_cost = 0.0

    for robot_id, tour in enumerate(robot_tours):
        # Check if the tour starts and ends at the robot's assigned depot
        if tour[0] != tour[-1] or tour[0] != robot_id:
            print(f"Robot {robot_id} does not start and end at its assigned depot {robot_id}.")
            return "FAIL"
        
        # Check each tour's travel cost
        calculated_cost = 0
        for i in range(len(tour) - 1):
            city_id1 = tour[i]
            city_id2 = tour[i + 1]
            calculated_cost += calculate_distance(city_coordinates[city_id1], city_coordinates[city_id2])
        
        if not math.isclose(calculated_cost, robot_costs[robot_id], abs_tol=1e-2):
            print(f"Cost mismatch for Robot {robot_id} (Calculated: {calculated_cost}, Expected: {robot_costs[robot_id]})")
            return "FAIL"
        
        total_calculated_cost += calculated_cost

        # Track all visited cities except the start/end depot
        all_cities_visited.update(tour)

    # Check if total cost is as expected
    if not math.isclose(total_calculated_cost, expected_total_cost, abs_tol=1e-2):
        print(f"Total cost mismatch (Calculated: {total_calculated_cost}, Expected: {expected_total_cost})")
        return "FAIL"
    
    # Check if all cities were visited exactly once
    if all_cities_visited != set(city_coordinates.keys()):
        print("Not all cities were visited or some were visited more than once.")
        return "FAIL"
    
    return "CORRECT"

# Solution details
tours = {
    0: [0, 1, 10, 12, 3, 8, 16, 17, 14, 4, 11, 0],
    1: [1, 6, 1, 2, 7, 18, 5, 13, 15, 9, 1]
}
costs = {
    0: 132.06,
    1: 115.54
}
total_cost = 247.6

# Validate the solution
print(check_solution([tours[0], tours[1]], [costs[0], costs[1]], total_cost))