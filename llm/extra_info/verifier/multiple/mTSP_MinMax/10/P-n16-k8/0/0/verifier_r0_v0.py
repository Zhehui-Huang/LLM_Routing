import math

# City coordinates indexed by city numbers
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Tours assigned to each robot (result from the solution)
robot_tours = {
    0: [0, 1, 9, 0],
    1: [0, 2, 10, 0],
    2: [0, 3, 11, 0],
    3: [0, 4, 12, 0],
    4: [0, 5, 13, 0],
    5: [0, 6, 14, 0],
    6: [0, 7, 15, 0],
    7: [0, 8, 0]
}

# Given travel costs for each robot
given_costs = {
    0: 72.88070710888512, 1: 52.4625939010481, 2: 86.03587467520119, 3: 64.98936367308863,
    4: 68.36272673975597, 5: 64.17258428512785, 6: 83.62034367443502, 7: 64.89992295835181
}

# Calculate Euclidean distance
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Function to check the solution
def verify_solution():
    visited_cities = set()
    max_cost_calculated = 0
    
    for robot, tour in robot_tours.items():
        total_cost = 0
        for i in range(len(tour) - 1):
            cost = calc_distance(city_coords[tour[i]], city_coords[tour[i+1]])
            total_cost += cost
            visited_cities.add(tour[i+1])
        
        # Compare calculated and given costs
        if not math.isclose(total_cost, given_costs[robot], rel_tol=1e-5):
            print(f"FAIL: Total cost mismatch for robot {robot}")
            return
        
        if total_cost > max_cost_calculated:
            max_cost_calculated = total_cost
    
    # Check all cities except depot are visited exactly once
    if len(visited_cities) != len(city_coords) - 1 or 0 in visited_cities:
        print("FAIL: Not all cities are visited or depot is visited as a destination")
        return
    
    # Check the maximum travel cost
    if not math.isclose(max_cost_calculated, max(given_costs.values()), rel_tol=1e-5):
        print("FAIL: Incorrect maximum travel cost calculation")
        return
    
    print("CORRECT")

verify_solution()