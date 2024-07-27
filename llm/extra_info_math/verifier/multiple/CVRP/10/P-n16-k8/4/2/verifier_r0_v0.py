def calculate_travel_cost(tour, coordinates):
    import math
    cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        cost += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return cost

def check_solution():
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
    ]
    
    demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
    
    tours = [
        [0, 2, 0],
        [0, 3, 1, 0],
        [0, 4, 0],
        [0, 6, 0],
        [0, 8, 0],
        [0, 9, 7, 5, 0],
        [0, 13, 12, 11, 10, 0],
        [0, 15, 14, 0]
    ]
    
    reported_costs = [0, 0, 0, 0, 0, 0, 0, 0]
    calculated_costs = [calculate_travel_cost(tour, coordinates) for tour in tours]
    all_demands = [0] * 16  # Track how many times each city is visited
    total_calculated_cost = 0
    
    for i, tour in enumerate(tours):
        total_demand = 0
        for city in tour:
            all_demands[city] += 1
            total_demand += demands[city]
        # Subtract two times the demand of the depot (added at start and end of each tour)
        total_demand -= 2 * demands[0]
        # Check if total demand exceeds robot capacity
        if total_demand > 35:
            return "FAIL"
        total_calculated_cost += calculated_costs[i]
    
    # Check if each city is visited exactly once (excluding the depot)
    if any(all_demands[i] != 1 for i in range(1, 16)):
        return "FAIL"
    
    # Check if each tour starts and ends at the depot
    if any(tour[0] != 0 or tour[-1] != 0 for tour in tours):
        return "FAIL"

    # Check if all reported costs are zero while calculated costs are not
    if any(cost != 0 for cost in calculated_costs):
        return "FAIL"

    if total_calculated_cost == sum(reported_costs):
        return "CORRECT"
    else:
        return "FAIL"

# Run the check
print(check_solution())