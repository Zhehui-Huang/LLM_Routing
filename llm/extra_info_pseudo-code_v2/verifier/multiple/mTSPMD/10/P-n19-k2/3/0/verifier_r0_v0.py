import numpy as np

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_solution():
    # Coordinates of cities
    city_coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
        (61, 33), (62, 63), (63, 69), (45, 35)
    ]

    # Tours provided for the solution
    tours = {
        0: [0, 6, 18, 2, 7, 5, 13, 15, 9, 8, 16, 17, 3, 12, 14, 11, 4, 10, 0],
        1: [1, 1]
    }

    # Expected costs as provided
    expected_costs = {
        0: 171.51248756479882,
        1: 0.0
    }

    # Calculate total travel cost for each robot
    total_costs = {}
    for robot, tour in tours.items():
        cost = 0
        for i in range(len(tour) - 1):
            city_from, city_to = tour[i], tour[i+1]
            cost += euclidean_distance(city_coordinates[city_from], city_coordinates[city_to])
        total_costs[robot] = cost

    # Check if total costs are close enough to expected costs
    correct = True
    for robot, cost in expected_costs.items():
        if not np.isclose(total_costs[robot], cost, rtol=1e-5):
            correct = False

    # Check if all cities are visited exactly once excluding the depots considering other robots' depots
    visited_cities = set()
    for robot, tour in tours.items():
        for city in tour:
            if city > 1:  # exclude depots from singleton check
                if city in visited_cities:
                    correct = False
                visited_cities.add(city)

    # Ensuring exactly 19 minus 2 depots plus 2 visits to them (each depot is visited once by its respective robot)
    if len(visited_cities) != 17:
        correct = False

    # Ensuring total combined cost
    overall_cost = sum(total_costs.values())
    expected_overall_cost = 171.51248756479882  # as provided in the solution
    if not np.isclose(overall_cost, expected_overall_cost, rtol=1e-5):
        correct = False

    return "CORRECT" if correct else "FAIL"

# Check the solution and print the result
print(verify_solution())