import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution():
    # City coordinates
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
        (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    # Demand list
    demands = [
        0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15
    ]
    
    # Given solution
    robots_tours = [
        [0, 16, 17, 3, 8, 13, 15, 12, 14, 18, 0],
        [0, 7, 9, 4, 11, 2, 5, 1, 10, 6, 0]
    ]
    
    calculated_costs = [
        198.64,
        179.24
    ]
    
    robot_capacity = 160
    
    # Verify all robots start and end at the depot city 0
    for tour in robots_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    # Verify that each city's demand is fully met
    demand_served = [0] * len(demands)
    for tour in robots_tours:
        for city in tour:
            demand_served[city] += demands[city]
    if demand_served != demands:
        return "FAIL"
    
    # Verify capacity constraints
    for tour in robots_tours:
        total_load = sum(demands[city] for city in tour)
        if total_load > robot_capacity:
            return "FAIL"
    
    # Verify travel costs
    for i, tour in enumerate(robots_tours):
        total_cost = 0
        for j in range(len(tour) - 1):
            total_cost += euclidean_distance(coordinates[tour[j]], coordinates[tour[j+1]])
        if not math.isclose(total_cost, calculated_costs[i], abs_tol=1e-2):
            return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Call the function and print the result to test the solution
print(verify_solution())