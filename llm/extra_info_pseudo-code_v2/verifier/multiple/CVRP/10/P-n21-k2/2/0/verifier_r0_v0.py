import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}
demand = {i: d for i, d in enumerate([0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15])}
robot_capacity = 160

# Tours and costs reported
robots_tours = {
    0: [0, 18, 0],
    1: [0, 19, 0]
}
robots_costs = {
    0: 78.81624198095213,
    1: 87.86353054595519
}
overall_cost_reported = 166.6797725269073

def verify_solution(tours, costs, overall_cost):
    calculated_overall_cost = 0
    demands_satisfied = set()

    for robot, tour in tours.items():
        # Check start and end at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Robot doesn't start or end at depot."
        
        # Check carrying capacity
        load = sum(demand[city] for city in tour if city != 0)
        if load > robot_capacity:
            return f"FAIL: Robot {robot} exceeds capacity."
        
        # Check tour costs and calculate individual tour cost
        total_tour_cost = 0
        for i in range(len(tour) - 1):
            total_tour_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        if not math.isclose(costs[robot], total_tour_cost, rel_tol=1e-5):
            return f"FAIL: Incorrect reported cost for Robot {robot}."
        
        demands_satisfied.update(tour[1:-1])
        calculated_overall_cost += total_tour_cost
    
    if not math.isclose(calculated_overall_cost, overall_cost):
        return "FAIL: Incorrect total overall cost."

    if demands_satisfied != set(range(1, 21)):
        return "FAIL: Not all demands are satisfied."

    return "CORRECT"

# Verify the solution
result = verify_solution(robots_tours, robots_costs, overall_cost_reported)
print(result)