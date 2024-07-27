import math

# Given data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}
demands = {
    0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8,
    10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26, 18: 17,
    19: 6, 20: 15, 21: 5, 22: 10
}
robot_capacity = 40

# Solution provided
robot_tours = [
    [0, 1, 2, 0, 0, 22, 0],
    [0, 3, 4, 0],
    [0, 5, 6, 9, 0],
    [0, 7, 10, 11, 13, 0],
    [0, 8, 15, 0],
    [0, 12, 14, 19, 0],
    [0, 16, 17, 0],
    [0, 18, 20, 21, 0]
]
robot_costs_provided = [
    99.63056622114102, 75.67537984747364, 87.98046471435967,
    125.50392609591222, 85.10825368055515, 158.91500409222184,
    68.20018679138722, 88.0023381850297
]

# Verification function
def verify_solution(tours, costs, overall_cost_provided):
    total_cost_calculated = 0
    demand_tracker = {i: 0 for i in demands}
    
    for robot_id, tour in enumerate(tours):
        current_demand = 0
        tour_cost = 0
        last_city = tour[0]
        
        for city in tour[1:]:
            if city != last_city:  # Skip repeated zero trips
                # Compute demand and check capacity
                current_demand += demands[city]
                if current_demand > robot_capacity:
                    print(f"FAIL: Robot {robot_id} exceeds capacity on tour: {tour}")
                    return "FAIL"
                
                # Calculate distance and cost
                dist = math.sqrt((cities[city][0] - cities[last_city][0])**2 + (cities[city][1] - cities[last_city][1])**2)
                tour_cost += dist
                last_city = city

            # Track demand fulfillment
            demand_tracker[city] += 1

        # Check if tour start and end are at depot
        if tour[0] != 0 or tour[-1] != 0:
            print(f"FAIL: Robot {robot_id} does not start or end at the depot: {tour}")
            return "FAIL"

        # Check if calculated tour cost equals provided cost
        if not math.isclose(tour_cost, costs[robot_id], abs_tol=0.001):
            print(f"FAIL: Calculated tour cost does not match provided for Robot {robot_id}: {tour_cost} vs {costs[robot_id]}")
            return "FAIL"

        total_cost_calculated += tour_cost

    # Verify all demands are met exactly once
    if any(v != 1 for v in demand_tracker.values() if v != 0):
        print("FAIL: Some cities' demands are not met exactly once.")
        return "FAIL"

    # Check total cost
    if not math.isclose(total_cost_calculated, overall_cost_provided, abs_tol=0.001):
        print(f"FAIL: Total costs do not match: {total_cost_calculated} vs {overall_cost_proclaimed}")
        return "FAIL"

    return "CORRECT"
    
# Run verification and print the result
result = verify_solution(robot_tours, robot_costs_provided, 789.0161196280804)
print(result)