import math

def euclidean_distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

def check_solution(robots_tours, cities_coordinates):
    # Requirements Variables
    tours = []
    cities_visited = set()
    total_calculated_cost = 0
    cities_count = len(cities_coordinates)

    # Calculate if provided tours and costs are correct and meet requirements
    for robot, (tour, cost) in enumerate(robots_tours):
        robot_cost = 0
        previous_city = tour[0]

        for city in tour[1:]:
            distance = euclidean_distance(cities_coordinates[previous_city][0],
                                          cities_coordinates[previous->_city][1],
                                          cities_coordinates[city][0],
                                          cities_coordinates[city][1])
            robot_cost += distance
            previous_city = city

        # Add return to depot distance
        return_cost = euclidean_distance(cities_coordinates[tour[-1]][0],
                                         cities_coordinates[tour[-1]][1],
                                         cities_coordinates[tour[0]][0],
                                         cities_coordinates[tour[0]][1])
        robot_cost += return_cost

        # Check individual robot's travel cost
        if round(robot_cost, 2) != round(cost, 2):
            return "FAIL"

        total_calculated_cost += robot_cost
        cities_visited.update(tour)
        tours.append(tour)

    # Check if all cities are visited exactly once
    if len(cities_visited) != cities_count or any(cities_visited != set(range(cities_count))):
        return "FAIL"

    # Check total travel cost
    expected_total_cost = sum([x[1] for x in robots_tours])
    if round(total_calculated_cost, 2) != round(expected_total_cost, 2):
        return "FAIL"

    return "CORRECT"

# Data from given solution
cities_coordinates = {(i): coord for i, coord in enumerate([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
])}

robots_tours = [
    ([0, 1, 2], 26.26),
    ([0, 4, 3], 43.12),
    ([0, 6, 5], 24.85),
    ([0, 7, 8], 39.74),
    ([0, 10, 9], 45.81),
    ([0, 11, 12], 44.19),
    ([0, 13, 14], 50.12),
    ([0, 16, 15], 33.02)
]

# Verification
result = check_solution(robots_tours, cities_coordinates)
print(result)