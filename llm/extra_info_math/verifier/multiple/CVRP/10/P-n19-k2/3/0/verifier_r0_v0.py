def verify_solution(robot_tours, robot_costs, total_cost, demands, capacities):
    # Verification setup
    visited_cities = set()
    correct_total_cost = 0
    
    # Check each robot's tour and cost
    for robot_id, (tour, cost) in enumerate(zip(robot_tours, robot_costs)):
        # Starting and ending at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Check if cities are visited once and calculate total demand in each tour
        current_demand = 0
        for i in range(len(tour)-1):
            city = tour[i]
            next_city = tour[i+1]

            # Check for unique visits
            if city != 0 and city in visited_cities:
                return "FAIL"
            visited_cities.add(city)

            # Calculate demands
            if city != 0:
                current_demand += demands[city]

            # Calculate travel costs
            correct_total_cost += ((coords[tour[i+1]][0] - coords[tour[i]][0])**2 + (coords[tour[i+1]][1] - coords[tour[i]][1])**2)**0.5

        # Capacity constraints
        if current_demand > capacities[robot_id]:
            return "FAIL"

    # Ensure all cities are visited
    if len(visited_cities) != len(demands) - 1:  # excluding the depot
        return "FAIL"

    # Check calculated total cost against provided total cost
    if not abs(correct_total_cost - total_cost) < 1e-6:  # Allowing some floating point margin
        return "FAIL"
        
    return "CORRECT"

# Constants / data given by the problem
coords = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
          (62, 63), (63, 69), (45, 35)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
capacities = [160, 160]

# Solution provided
robot_tours = [[0], [0]]
robot_costs = [0, 0]
total_cost = 0

# Run verification
result = verify_solution(robot_tours, robot_costs, total_cost, demands, capacities)
print(result)