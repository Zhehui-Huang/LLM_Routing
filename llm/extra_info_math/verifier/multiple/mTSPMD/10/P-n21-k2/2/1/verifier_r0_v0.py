import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_solution(tours, costs, coords):
    robot_0_tour = tours[0]
    robot_1_tour = tours[1]
    robot_0_cost = costs[0]
    robot_1_cost = costs[1]

    # Cities coordinates
    city_coords = {i: coord for i, coord in enumerate(coords)}

    # Check if the solution starts and ends at the correct depots
    if not(robot_0_tour[0] == 0 and robot_0_tour[-1] == 0
           and robot_1_tour[0] == 1 and robot_1_tour[-1] == 1):
        return "FAIL"

    # Check if all cities are visited exactly once
    all_visited_cities = robot_0_tour[1:-1] + robot_1_tour[1:-1]
    if len(set(all_visited_cities)) != len(all_visited_cities) or set(all_visited_cities) != set(range(2, 21)):
        return "FAIL"

    # Verify the total travel costs reported
    def calculate_tour_cost(tour):
        return sum(calculate_distance(city_coords[tour[i]], city_coords[tour[i+1]]) for i in range(len(tour) - 1))

    calculated_robot_0_cost = calculate_tour_cost(robot_0_tour)
    calculated_robot_1_cost = calculate_tour_cost(robot_1_tour)

    if not(math.isclose(calculated_robot_0_cost, robot_0_cost, abs_tol=0.01)
           and math.isclose(calculated_robot_1_cost, robot_1_cost, abs_tol=0.01)):
        return "FAIL"

    # Checking for sub-tours within the tours
    visited = set()
    for tour in tours:
        for city in tour[1:-1]:
            if city in visited:
                return "FAIL"
            visited.add(city)
    if len(visited) != 19:
        return "FAIL"

    return "CORRECT"

coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

tours = [[0, 5, 6, 14, 20, 0], [1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 1]]
costs = [88.23, 343.09]

result = validate_solution(tours, costs, coordinates)
print(result)