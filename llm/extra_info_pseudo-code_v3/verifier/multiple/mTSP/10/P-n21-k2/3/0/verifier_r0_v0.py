import math

# Definition of cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Given tours and costs
robot_tours = {
    0: [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 0],
    1: [0, 6, 20, 5, 7, 2, 13, 9, 17, 14, 19, 0]
}
reported_costs = {
    0: 135.57,
    1: 160.83
}
reported_total_cost = 296.40

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution():
    all_cities_visited = set()
    overall_cost_computed = 0
    
    for robot, tour in robot_tours.items():
        # Check each tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check for unique city visits excluding multiple depot visits
        unique_cities = set(tour[1:-1])
        if len(unique_cities) + 1 != len(tour[1:-1]) + 1:
            return "FAIL"
        
        all_cities_visited.update(unique_cities)
        
        # Calculate travel cost for the tour
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(tour[i], tour[i + 1])
        
        # Round the tour cost to two decimal places for comparison
        tour_cost = round(tour_cost, 2)
        
        if tour_cost != reported_costs[robot]:
            return "FAIL"
        
        overall_cost_computed += tour_cost
    
    # Check all cities are visited exactly once
    if all_cities_visited != set(range(1, 21)):
        return "FAIL"
    
    # Check the overall cost
    overall_cost_computed = round(overall_based, 2)
    if overall_cost_computed != reported_total_cost:
        return "FAIL"
    
    return "CORRECT"

# Call verification function and print result
print(verify_solution())