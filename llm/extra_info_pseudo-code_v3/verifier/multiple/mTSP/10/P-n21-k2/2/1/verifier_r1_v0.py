import numpy as np

def compute_euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution():
    # City coordinates including the depot at index 0
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
        (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
        (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
    ]

    # Robot tours
    robot_tours = [
        [0, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 0],
        [0, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 0]
    ]

    # Provided total costs
    provided_costs = [143.98241284438606, 109.8362166450987]
    calculated_costs = []
    
    # Verify if all cities except the depot are visited exactly once
    all_cities_visited = set()
    for tour in robot_tours:
        for city in tour:
            if city != 0:
                all_cities_visited.add(city)
    
    if len(all_cities_visited) != len(coordinates) - 1:
        return "FAIL" 

    # Calculate travel costs for each robot and verify if it matches the provided costs within a tolerance
    for robot_tour, provided_cost in zip(robot_tours, provided_costs):
        total_cost = 0
        for i in range(len(robot_tour) - 1):
            city1 = robot_tour[i]
            city2 = robot_tour[i+1]
            total_cost += compute_euclidean_distance(coordinates[city1], coordinates[city2])
        calculated_costs.append(total_cost)
        
        if not np.isclose(total_cost, provided_cost, atol=0.01):
            return "FAIL"

    # Calculate overall costs and compare
    overall_calculated_cost = sum(calculated_costs)
    overall_provided_cost = sum(provided_costs)
    if not np.isclose(overall_calculated_cost, overall_provided_cost, atol=0.01):
        return "FAIL"

    return "CORRECT"

# Check the correctness of the provided solution
result = verify_solution()
print(result)