import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tours(tours, demands, capacities, coordinates):
    depot = 0
    total_cost = 0

    for robot_id, tour in enumerate(tours):
        # Check if tour starts and ends at the depot
        if tour[0] != depot or tour[-1] != depot:
            return "FAIL, Robot {} does not start or end at the depot".format(robot_id)
        
        tour_cost = 0
        current_capacity = 0
        visited_demands = [0] * len(demands)

        # Calculate total cost of the tour and check capacity constraints
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            tour_cost += calculate_euclidean_distance(coordinates[city1][0], coordinates[city1][1],
                                                      coordinates[city2][0], coordinates[city2][1])
            if city2 != depot:
                visited_demands[city2] += demands[city2]
                current_capacity += demands[city2]
                if current_capacity > capacities[robot_id]:
                    return "FAIL, Robot {} exceeds capacity".format(robot_id)

        total_cost += tour_cost
        
        # Check demand fulfillment
        if any(visited_demands[i] != demands[i] for i in range(len(demands))):
            return "FAIL, Not all demand met by Robot {}".format(robot_id)

    # Report success if all checks are correct and the total tour cost is provided correctly
    expected_total_cost = 301.7480840160281  # This is the overall total cost reported
    if abs(total_cost - expected_total_cost) > 1e-5:  # using a small threshold for floating point comparison
        return "FAIL, Total travel cost does not match"

    return "CORRECT"

# Robot tours provided in the solution
robot_tours = [
    [0, 6, 18, 5, 7, 2, 9, 15, 16, 0],
    [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 13, 0]
]

# Coordinates as provided in the problem statement
city_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demands as provided
city_demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Capacities of robots
robot_capacities = [160, 160]

# Perform Verification
result = verify_tours(robot_tours, city_demands, robot_capacities, city_coordinates)
print(result)