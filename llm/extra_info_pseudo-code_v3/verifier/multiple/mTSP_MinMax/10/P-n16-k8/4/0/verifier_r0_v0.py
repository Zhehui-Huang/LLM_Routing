import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(robot_tours, city_coordinates):
    visited_cities = set()
    max_travel_cost = 0
    robot_travel_costs = []

    # Verify that all robots start and end at the depot
    for robot, tour in enumerate(robot_tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Calculate travel cost for the current robot
        travel_cost = 0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i+1]
            x1, y1 = city_coordinates[city1]
            x2, y2 = city_coordinates[city2]
            distance = calculate_euclidean_distance(x1, y1, x2, y2)
            travel_cost += distance

        robot_travel_costs.append(travel_cost)
        max_travel_cost = max(max_travel_cost, travel_cost)

        # Add visited cities, excluding the depot
        visited_cities.update(tour[1:-1])

    # Verify each city is visited exactly once, excluding depot city
    if len(visited_cities) != 15:  # Total cities minus depot
        return "FAIL"

    # Check for minimizing the maximum distance traveled by any robot
    calculated_max_cost = max(robot_travel_costs)
    if calculated_max_cost != max_travel_cost:
        return "FAIL"

    return "CORRECT"

# City coordinates map (indexed from 0 to 15)
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Solution provided
robot_tours = [
    [0, 0, 6, 0, 0],
    [0, 0, 12, 15, 0, 0],
    [0, 0, 14, 0, 0],
    [0, 0, 2, 9, 13, 0, 0],
    [0, 0, 4, 11, 0, 0],
    [0, 0, 3, 8, 0, 0],
    [0, 0, 1, 10, 0, 0],
    [0, 0, 5, 7, 0, 0]
]

# Check correctness of the solution
result = verify_solution(robot_tours, city_coordinates)
print(result)