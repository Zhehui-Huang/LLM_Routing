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
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution():
    """Verify the solution according to given requirements."""
    all_cities_visited = set()
    overall_computed_cost = 0
    
    for robot, tour in robot_tours.items():
        # Start and end at the depot, which is city 0
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # All cities in the tour should be visited once, considering multiple depot visits
        if len(set(tour)) - 1 != len(tour) - 2:  # Remove one instance of depot, check others
            return "FAIL"
        
        all_cities_visited.update(tour[1:-1])
        
        # Compute the cost of the given tour
        tour_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        tour_cost = round(tour_cost, 2)
        
        # Check if reported costs are as per the calculations
        if tour_cost != reported_costs[robot]:
            return "FAIL"
        
        overall_computed_cost += tour_cost
    
    # Check if all cities, except the depot, are visited once
    if all_cities_visited != set(range(1, 21)):  # Cities from 1 to 20 should be visited
        return "FAIL"
    
    # Check overall cost
    if round(overall_computed_cost, 2) != reported_total_cost:
        return "FAIL"
    
    return "CORRECT"

# Execute the test and output the result
print(verify_solution())