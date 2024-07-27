import math

def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tours(robot_tours, robot_costs, overall_cost, coordinates):
    # Verify each robot starts from their depot city and doesn't need to return
    if any((tour[-1] != tour[0]) for tour in robot_tours):
        return "FAIL"
    
    # Verify each city is visited exactly once
    all_visited_cities = [city for tour in robot_tours for city in tour[1:-1]]
    unique_visited_cities = set(all_visited_cities)
    if len(all_visited_cities) != len(unique_visited_cities) + len(robot_tours) - 1:
        return "FAIL"
    
    # Verify total number of cities
    if len(coordinates) != 21:
        return "FAIL"
    
    # Check robot initial positions
    if not all(robot_tours[i][0] == i for i in range(len(robot_tours))):
        return "FAIL"
    
    # Compute distances and check costs
    calculated_costs = []
    for tour in robot_tours:
        tour_cost = sum(compute_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) 
                        for i in range(len(tour) - 1))
        calculated_costs.append(tour_cost)
    
    if not all(math.isclose(cost, calc_cost) for cost, calc_cost in zip(robot_costs, calculated_costs)):
        return "FAIL"
    
    # Check overall cost
    if not math.isclose(sum(robot_costs), overall_cost):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of each city
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
               (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Tours given by each robot
robot_tours = [
    [0, 6, 20, 5, 14, 7, 2, 19, 11, 4, 0],
    [1, 17, 9, 13, 15, 12, 3, 18, 8, 10, 16, 1]
]

# Costs for each robot
robot_costs = [147.95155527053493, 142.32851878214734]
overall_cost = 290.28007405268227

# Execute the verification
result = verify_tours(robot_tours, robot_costs, overall_cost, coordinates)
print(result)