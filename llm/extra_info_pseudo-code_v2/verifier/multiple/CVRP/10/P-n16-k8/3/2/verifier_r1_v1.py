import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tours, demands, capacities, coordinates, provided_total_cost):
    total_cost_calculated = 0
    demands_fulfilled = [0] * len(demands)
    
    for robot_id, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour must start and end at the depot"
        
        current_capacity = 0
        route_cost = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            distance = euclidean_distance(coordinates[city_from], coordinates[city_to])
            route_cost += distance
            
            if city_to != 0:  # depot has no demand
                current_capacity += demands[city_to]
                demands_fulfilled[city_to] += demands[city_to]
        
        if current_capacity > capacities[robot_id]:
            return f"FAIL: Capacity exceeded for robot {robot_id}"
        
        total_cost_calculated += route_cost

    if not all(d_fulfill == d_required for d_fulfill, d_required in zip(demands_fulfilled, demands)):
        return "FAIL: Not all demands are met correctly"
    
    if not math.isclose(total_cost_calculated, provided_total_cost, rel_tol=1e-9):
        return f"FAIL: Total cost is not matching, expected {provided_total_cores}, got {total_cost_calculated}"
    
    return "CORRECT"

# Data from the problem statement
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
capacities = [35] * 8  # Since all robots have the same capacity
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]
provided_total_cost = 558.2658457496536

# Provided solution details
tours = [
    [0, 1, 3, 0],
    [0, 2, 0],
    [0, 4, 5, 0],
    [0, 6, 0],
    [0, 7, 9, 10, 0],
    [0, 8, 11, 0],
    [0, 12, 13, 15, 0],
    [0, 14, 0]
]

# Verify the solution
result = verify_solution(tours, demands, capacities, coordinates, provided_total_cost)
print(result)