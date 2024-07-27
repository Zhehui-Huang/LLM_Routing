def verify_cvrp_solution(tours, demands, capacities, total_costs):
    visited = set()
    depot = 0
    total_cost_computed = 0
    
    for robot, tour_info in enumerate(tours):
        tour, tour_cost = tour_info
        if tour[0] != depot or tour[-1] != depot:
            return "FAIL"
        
        current_capacity = 0
        for i in range(len(tour)-1):
            current_capacity += demands[tour[i]]
            if current_capacity > capacities[robot]:
                return "FAIL"
        
        visited.update(tour[1:-1])  # exclude the depot city from each end
        total_cost_computed += tour_cost
    
    if visited != set(range(1, len(demands))):  # Check if all cities are visited exactly once
        return "FAIL"
    
    if not abs(total_cost_computed - sum(total_costs)) < 1e-5:  # Allow small numeric discrepancies
        return "FAIL"
    
    return "CORRECT"

# Data from the earlier provided solution
demands = {0: 0, 1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11}
capacities = [35] * 8  # All robots have the same capacity
tours = [
    ([0, 10, 0], 41.62),
    ([0, 7, 0], 44.05),
    ([0, 6, 0], 24.08),
    ([0, 2, 0], 42.05),
    ([0, 5, 0], 46.17),
    ([0, 11, 0], 56.32),
    ([0, 4, 0], 44.05),
    ([0, 1, 0], 27.78)
]
total_costs = [41.62, 44.05, 24.08, 42.05, 46.17, 56.32, 44.05, 27.78]

# Validate the solution
result = verify_cvrp_solution(tours, demands, capacities, total_costs)
print(result)  # Expected output: "CORRECT" if all conditions are met, otherwise "FAIL"