import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution():
    # City coordinates and demands
    cities = {
        0: ((30, 40), 0), 1: ((37, 52), 19), 2: ((49, 43), 30),
        3: ((52, 64), 16), 4: ((31, 62), 23), 5: ((52, 33), 11),
        6: ((42, 41), 31), 7: ((52, 41), 15), 8: ((57, 58), 28),
        9: ((62, 42), 14), 10: ((42, 57), 8), 11: ((27, 68), 7),
        12: ((43, 67), 14), 13: ((58, 27), 19), 14: ((37, 69), 11),
        15: ((61, 33), 26), 16: ((62, 63), 17), 17: ((63, 69), 6),
        18: ((45, 35), 15)
    }
    
    # Tours and expected demands
    robot0_tour = [0, 11, 9, 13, 15, 12, 3, 8, 16, 17, 14, 0]
    robot1_tour = [0, 6, 5, 2, 7, 18, 1, 4, 10, 0]
    
    # Compute the total load for each robot
    robot0_load = sum(cities[city][1] for city in robot0_tour if city != 0)
    robot1_load = sum(cities[city][1] for city in robot1_tour if city != 0)
    
    # Check load capacity constraint
    if robot0_load > 160 or robot1_load > 160:
        return "FAIL: Capacity constraint violated"
    
    # Calculate travel costs
    robot0_cost = sum(calculate_distance(cities[robot0_tour[i]][0], cities[robot0_tour[i+1]][0]) 
                      for i in range(len(robot0_tour) - 1))
    robot1_cost = sum(calculate_distance(cities[robot1_tour[i]][0], cities[robot1_tour[i+1]][0]) 
                      for i in range(len(robot1_tour) - 1))
    
    # Actual costs from solution
    actual_robot0_cost = 218
    actual_robot1_cost = 111
    actual_total_cost = 330.2027832582222
    
    # Compare calculated costs to expected
    if not (math.isclose(robot0_cost, actual_robot0_cost, rel_tol=1e-9) and
            math.isclose(robot1_cost, actual_robot1_cost, rel_tol=1e-9) and
            math.isclose(robot0_cost + robot1_cost, actual_total_cost, rel_tol=1e-9)):
        return "FAIL: Cost mismatch"
    
    return "CORRECT"

# Evaluate the solution
result = verify_solution()
print(result)