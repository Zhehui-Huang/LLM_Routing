import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Provided tour data for verification
robots_tours = {
    0: [0, 1, 2, 3, 4, 10, 11, 12, 15],
    1: [0, 5, 7, 8, 9, 13, 14],
    2: [0, 6],
    3: [0],
    4: [0],
    5: [0],
    6: [0],
    7: [0]
}

# Calculated costs for verification
travel_costs = [115.69, 93.78, 12.04, 0.00, 0.00, 0.00, 0.00, 0.00]
expected_overall_cost = 221.52

def calculate_distance(city1, city2):
    """ Helper function to calculate Euclidean distance between two cities. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(robots_tours, travel_costs, expected_overall_cost):
    visited_cities = set()
    total_cost = 0

    # Verify the tours and calculate the costs
    for robot_id, tour in robots_tours.items():
        tour_cost = 0
        # Compute the path cost for each route
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(tour[i], tour[i + 1])
        visited_cities.update(tour)
        expected_cost = round(tour_cost, 2)

        # Check cost error within a tolerance
        if not math.isclose(expected_cost, travel_costs[robot_id], rel_tol=0.01):
            return "FAIL"
        total_cost += expected_cost

    # Check if all cities were visited exactly once
    if visited_cities != set(cities.keys()):
        return "FAIL"

    # Check total cost against expected overall cost
    if not math.isclose(total_cost, expected_overall_cost, rel_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Verify the solution and print the result
result = verify_solution(robots_tours, travel_costs, expected_overall_cost)
print(result)