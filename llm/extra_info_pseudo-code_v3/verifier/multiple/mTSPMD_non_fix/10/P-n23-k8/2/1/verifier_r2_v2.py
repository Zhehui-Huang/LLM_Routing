import math

# Coordinates of all cities including depots
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

def calculate_distance(city1, city2):
    # Calculate the Euclidean distance between two city coordinates
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_solution():
    all_cities_visited = set()
    total_calculated_cost = 0.0

    # Data provided from the supposed solution
    robot_tours = {
        0: [0, 21, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 22, 5, 20, 6, 7, 2, 17, 14],
        1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []
    }
    robot_costs = {
        0: 205.20233966789624,
        1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0
    }
    reported_total_cost = 205.20233966789624

    # Verify all cities are visited exactly once
    for robot, tour in robot_tours.items():
        if any(city in all_cities_visited for city in tour):
            return "FAIL"
        all_cities_visited.update(tour)
    
    if len(all_cities_visited) != 23:
        return "FAIL"
    
    # Calculate the travel cost and verify with reported costs
    for robot, tour in robot_tours.items():
        computed_cost = 0
        for i in range(len(tour)):
            if i < len(tour) - 1:
                computed_cost += calculate_distance(tour[i], tour[i+1])

        if not math.isclose(computed_cost, robot_costs[robot], abs_tol=1e-3):
            return "FAIL"
        total_calculated_cost += computed_cost

    # Verify overall cost
    if not math.isclose(total_calculated_cost, reported_total_cost, abs_tol=1e-3):
        return "FAIL"

    return "CORRECT"

# Invoke test function and print the result
print(test_solution())