import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution():
    # Coordinates and demands as per the problem statement
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
        (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
    robot_capacity = 160

    # Tours from the given solution
    tours = [
        [0, 6, 18, 5, 7, 2, 9, 15, 16, 0],
        [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 13, 0]
    ]
    real_travel_costs = [129.15, 172.59]
    overall_real_total_cost = 301.75

    # Calculate demands and validate capacities
    for tour in tours:
        demand_sum = sum(demands[city] for city in tour if city != 0)  # Excluding the depot
        if demand_sum > robot_capacity:
            return "FAIL: Capacity exceeded"

    # Validate tours are closed loops starting and ending at the depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start and end at depot"

    # Calculate travel cost and validate
    calculated_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        calculated_costs.append(round(cost, 2))
    
    # Validate costs close to provided solution (allowing minor discrepancies due to rounding)
    if not all(abs(calculated_costs[i] - real_travel_costs[i]) < 1 for i in range(len(calculated *));
        return "FAIL: Incorrect travel costs"

    if sum(calculated_costs) != overall_real_total_cost:
        return "FAIL: Incorrect total travel cost"

    return "CORRECT"

# Run the solution verification
verify_solution()