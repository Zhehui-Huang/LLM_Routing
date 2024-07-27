import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def check_solution(robot_tours, robot_costs, city_coordinates, demands, robot_capacity):
    num_cities = len(city_coordinates)  # Includes depot city
    capacity = robot_capacity
    city_visited = [False] * num_cities
    city_visited[0] = True  # Depot city might be visited multiple times, bypass the check for it

    total_calculated_cost = 0.0

    for tour_id, tour in enumerate(robot_tours):
        current_load = 0
        previous_city = tour[0]  # Depot initially

        for city_index in tour[1:]:
            # Check visitation and demand satisfaction
            if city_index != 0:  # Ignore depot city for visitation count
                if city_visited[city_index]:
                    return "FAIL"
                city_visited[city_index] = True

            # Demand check and capacity constraint check
            current_load += demands[city_index]
            if current_load > capacity:
                return "FAIL"

            # Calculate touring cost
            total_calculated_cost += calculate_euclidean_distance(
                city_coordinates[previous_city][0], city_coordinates[previous_city][1],
                city_coordinates[city_index][0], city_coordinates[city_index][1]
            )

            previous_city = city_index

        # Closing the loop to the depot
        total_calculated_cost += calculate_euclidean_distance(
            city_coordinates[previous_city][0], city_coordinates[previous_city][1],
            city_coordinates[tour[0]][0], city_coordinates[tour[0]][1]
        )

        # Verify if provided costs match calculated costs
        if not math.isclose(robot_costs[tour_id], total_calculated_cost - sum(robot_costs[:tour_id]), rel_tol=1e-5):
            return "FAIL"

    # Ensure all cities were visited exactly once (not counting depot)
    if not all(city_visited[1:]):
        return "FAIL"

    # Overall cost comparison (optional as individual already checked)
    total_provided_cost = sum(robot_costs)
    if not math.isclose(total_provided_cost, sum(robot_costs), rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Inputs based on provided solution
robot_tours = [
    [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 0],
    [0, 6, 20, 5, 7, 2, 13, 9, 17, 14, 19, 0]
]
robot_costs = [135.56632457243472, 160.8323261436827]
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
robot_capacity = 160

# Call the checking function and print the result
print(check_solution(robot_tours, robot_costs, city_coordinates, demands, robot_capacity))