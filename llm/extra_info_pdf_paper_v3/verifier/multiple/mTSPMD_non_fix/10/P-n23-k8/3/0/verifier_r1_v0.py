import math

# Given data
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

robot_tours = [
    [0, 1, 9, 17, 0],
    [0, 10, 2, 18, 0],
    [0, 11, 3, 19, 0],
    [0, 20, 4, 12, 0],
    [0, 21, 5, 13, 0],
    [0, 6, 22, 14, 0],
    [0, 7, 15, 0],
    [0, 16, 8, 0]
]

reported_costs = [
    49.87365316325974, 50.54377103396226, 65.56127945659634,
    59.225200952333, 39.2721754167244, 36.799853384538906,
    53.78747589408242, 32.47220505424423
]

# Function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Verify the correctness of the solution
def verify_solution():
    global robot_tours, reported_costs, cities_coordinates
    
    # Check unique visits
    all_visited_cities = set()
    for tour in robot_tours:
        all_visited_cities.update(tour)
    if len(all_visited_cities) != 23:
        return "FAIL: Not all cities visited exactly once."
    
    # Check travels and costs
    total_cost_calculated = 0
    for robot_index, tour in enumerate(robot_tours):
        cost = 0
        for i in range(len(tour) - 1):
            cost += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
        total_cost_calculated += cost
        if not math.isclose(cost, reported_costs[robot_index], abs_tol=0.001):
            return f"FAIL: Incorrect cost calculation for Robot {robot_tour_index}."
    
    # Check overall cost
    if not math.isclose(total_cost_calculated, sum(reported_costs), abs_tol=0.001):
        return f"FAIL: Overall reported cost does not match the sum of individual costs."
    
    return "CORRECT"

# Run the verification
print(verify_solution())