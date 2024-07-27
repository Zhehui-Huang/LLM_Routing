import math

def calculate_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def verify_robot_starts_and_ends_at_depot(robot_tour, robot_start_end):
    """ Check if the robot starts and ends at its designated depot """
    return robot_tour[0] == robot_start_end and robot_tour[-1] == robot_start_end

def verify_unique_visit_to_cities(all_robots_tours, total_cities):
    """ Check if each city is visited exactly once collectively by all robots """
    visited = [0] * total_cities
    for tour in all_robots_tours:
        for city in tour[1:-1]:  # Exclude start and end since they are depots and repeated
            visited[city] += 1
    return all(v == 1 for v in visited)

def verify_tours(all_robots_tours):
    depots = [0, 1, 2, 3, 4, 5, 6, 7]
    for tour, depot in zip(all_robots_tours, depots):
        if not verify_robot_starts_and_ends_at_depot(tour, depot):
            return False
    return True

def check_total_travel_cost(robots_tours, total_cost_reported):
    """ Calculate and verify total travel costs """
    total_calculated_cost = 0
    city_positions = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 48), (58, 27), (37, 69)
    ]
    for tour in robots_tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(city_positions[tour[i]], city_positions[tour[i+1]])
        total_calculated_cost += tour_cost
    
    return math.isclose(total_calculated_cost, total_cost_reported, rel_tol=1e-9)

robot_tours = [
    [0, 6, 2, 7, 5, 14, 9, 13, 8, 3, 12, 15, 11, 4, 10, 1, 0],
    [1, 10, 0, 6, 2, 7, 5, 14, 9, 13, 8, 3, 12, 15, 4, 11, 1],
    [2, 7, 5, 14, 9, 13, 8, 3, 12, 15, 4, 11, 1, 10, 0, 6, 2],
    [3, 12, 15, 4, 11, 1, 10, 0, 6, 2, 7, 5, 14, 9, 13, 8, 3],
    [4, 11, 1, 10, 0, 6, 2, 7, 5, 14, 9, 13, 8, 3, 12, 15, 4],
    [5, 14, 9, 13, 8, 3, 12, 15, 4, 11, 1, 10, 0, 6, 2, 7, 5],
    [6, 2, 7, 5, 14, 9, 13, 8, 3, 12, 15, 4, 11, 1, 10, 0, 6],
    [7, 5, 14, 9, 13, 8, 3, 12, 15, 4, 11, 1, 10, 0, 6, 2, 7]
]
overall_total_travel_cost = 1325.4183707122731

# Verification sequence
if (verify_tours(robot_tours)
    and verify_unique_visit_to_cities(robot_tours, 16)
    and check_total_travel_cost(robot_tours, overall_total_travel_cost)):
    print("CORRECT")
else:
    print("FAIL")