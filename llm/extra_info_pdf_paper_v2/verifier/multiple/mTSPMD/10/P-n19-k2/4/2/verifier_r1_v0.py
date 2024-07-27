import numpy as np

# Given Robot Tours and Costs
robot0_tour = [0, 6, 18, 5, 13, 15, 9, 7, 2, 8, 16, 17, 3, 10, 12, 14, 11, 4, 0]
robot1_tour = [1, 1]
robot0_cost = 174.03576233257616
robot1_cost = 0.0
total_cost = 174.03576233257616

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def calculate_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def check_solution(robot_tours, expected_costs, expected_total_cost):
    # Check the tours start and end at their respective depots
    if robot_tours[0][0] != 0 or robot_tours[0][-1] != 0:
        return False
    if robot_tours[1][0] != 1 or robot_tours[1][-1] != 1:
        return False
        
    # Check if all cities have been visited exactly once
    all_cities_visited = sorted([city for tour in robot_tours for city in tour])
    expected_cities = list(range(len(cities)))
    if all_cities_visited != expected_cities:
        return False

    # Calculate and check the costs of the tours against provided costs
    calculated_costs = []
    for tour in robot_tours:
        cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        calculated_costs.append(cost)
    
    if not np.isclose(calculated_costs, expected_costs, rtol=1e-3).all():
        return False
    
    # Check the sum of costs
    if not np.isclose(sum(calculated_costs), expected_total_cost, rtol=1e-3):
        return False
    
    return True

# Run test
result = check_solution(
    [robot0_tour, robot1_tour],
    [robot0_cost, robot1_cost],
    total_cost
)

print("CORRECT" if result else "FAIL")