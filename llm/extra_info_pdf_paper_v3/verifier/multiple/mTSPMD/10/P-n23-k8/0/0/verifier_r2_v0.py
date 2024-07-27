import math

# Coordinates for each city index
cities = {
  0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
  5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
  10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
  15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
  20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Provided tour solutions and costs
robot_tours = [
    {"tour": [0, 11, 15, 12, 19, 18, 8, 13, 22, 14, 17, 9, 10, 16, 20, 21, 0], "cost": 190.56075502032294},
    {"tour": [1, 16, 21, 20, 14, 17, 22, 9, 13, 19, 18, 8, 12, 15, 11, 10, 1], "cost": 165.7315498708084},
    {"tour": [2, 11, 15, 12, 10, 19, 18, 8, 13, 9, 17, 14, 22, 20, 21, 16, 2], "cost": 181.45950923152503},
    {"tour": [3, 19, 18, 8, 13, 9, 14, 17, 22, 20, 21, 16, 10, 11, 15, 12, 3], "cost": 161.30175127794735},
    {"tour": [4, 11, 10, 21, 16, 20, 14, 22, 17, 9, 13, 8, 19, 18, 12, 15, 4], "cost": 180.41656566863406},
    {"tour": [5, 14, 17, 22, 9, 13, 8, 18, 19, 12, 15, 11, 10, 16, 21, 20, 5], "cost": 156.70274992175618},
    {"tour": [6, 13, 17, 14, 22, 9, 8, 18, 19, 12, 15, 11, 10, 21, 16, 20, 6], "cost": 192.02735623295612},
    {"tour": [7, 20, 21, 16, 10, 11, 15, 12, 19, 18, 8, 13, 9, 14, 17, 22, 7], "cost": 163.52768238537573}
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tours():
    # Requirement 1: All cities visited exactly once
    all_visited = sorted([city for tour in robot_tours for city in tour if city not in {0, 1, 2, 3, 4, 5, 6, 7}])
    if all_visited != list(range(8, 23)):
        return "FAIL"
    
    # Requirement 2 & 5: Verify costs
    total_calculated_cost = 0
    for robot in robot_tours:
        tour = robot["tour"]
        actual_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
        if not math.isclose(actual_cost, robot["cost"], rel_tol=1e-5):
            return "FAIL"
        total_calculated_cost += robot["cost"]
    
    # Is the total cost correct?
    given_total_cost = 1391.727919609326
    if not math.isclose(total_calculated_cost, given_total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Requirement 3: Each robot starts and ends its tour at its assigned depot
    for idx, robot in enumerate(robot_tours):
        if robot["tour"][0] != robot["tour"][-1] or robot["tour"][0] != idx:
            return "FAIL"

    return "CORRECT"

# Evaluate the solution
output = verify_tours()
print(output)