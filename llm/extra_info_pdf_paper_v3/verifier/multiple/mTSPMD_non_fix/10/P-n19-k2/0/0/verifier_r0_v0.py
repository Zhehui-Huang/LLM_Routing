import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(robot_tours, coordinates):
    # Verify unique and complete city visitation
    cities_visited = set()
    for tour in robot_tours:
        for city in tour:
            cities_visited.add(city)
    
    all_cities = set(range(len(coordinates)))
    if cities_visited != all_cities:
        return "FAIL"
    
    # Check correct starting point for all robots
    if robot_tours[0][0] != 0 or robot_tours[1][0] != 0:
        return "FAIL"

    # Calculate and verify travel costs from the tours
    calculated_costs = []
    for tour in robot_tours:
        total_cost = 0
        for i in range(len(tour) - 1):
            city_1 = tour[i]
            city_2 = tour[i + 1]
            total_cost += calculate_euclidean_distance(coordinates[city_1][0], coordinates[city_1][1],
                                                       coordinates[city_2][0], coordinates[city_2][1])
        calculated_costs.append(total_cost)

        # In this task, tour ends can be any city so no need to check for loopback to the initial depot
    
    presented_costs = [158.2, 170.36]  # As per the solution given
    if not all(math.isclose(calculated_costs[i], presented_costs[i], rel_tol=0.01) for i in range(len(calculated_costs))):
        return "FAIL"

    # Total cost calculated versus total cost presented
    total_presented_cost = 328.56
    if not math.isclose(sum(calculated_cost), total_presented_cost, rel_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Coordinates setup
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64),
    (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Provided tours
robot_tours = [
    [0, 1, 10, 4, 11, 14, 12, 3, 17, 16, 8, 7, 2, 6, 18, 5, 13, 15, 9],
    [1, 4, 11, 14, 12, 10, 0, 6, 18, 2, 7, 5, 13, 15, 9, 8, 3, 16, 17]
]

# Verify solution
result = verify_solution(robot_tours, coordinates)
print(result)