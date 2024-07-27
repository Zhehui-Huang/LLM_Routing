import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(robot_tours, cities):
    # Cities coordinates are given in problem
    city_coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
        15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
    }

    # Unpack the tours
    robot_0_tour = robot_tours[0]["tour"]
    robot_1_tour = robot_tours[1]["tour"]

    # Check if each robot starts at the designated depot city 0
    if robot_0_tour[0] != 0 or robot_1_tour[0] != 0:
        return "FAIL"

    # Check if robots do not need to return to starting depot
    if robot_0_tour[-1] == 0 or robot_1_tour[-1] == 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once collectively
    all_visited_cities = robot_0_tour + robot_1_tour
    unique_cities = set(all_visited_cities)
    if len(unique_cities) != len(city_coordinates):
        return "FAIL"
    
    # Verify if each city is visited only once
    for city in unique_cities:
        if all_visited_cities.count(city) != 1:
            return "FAIL"
    
    # Check for each robot if their tours are feasible with minimum cost
    for robot_info in robot_tours:
        prev_city = robot_info["tour"][0]
        calculated_cost = 0
        for city in robot_info["tour"][1:]:
            calculated_cost += calculate_distance(city_coordinates[prev_city], city_coordinates[city])
            prev_city = city
        
        # Allow tiny numerical precision issues
        if not math.isclose(robot_info["cost"], calculated_cost, abs_tol=1e-6):
            return "FAIL"
    
    return "CORRECT"

# Given solution detail
robot_tours_solution = [
    {'tour': [0, 6, 18, 5, 7, 2, 9, 15, 13], 'cost': 66.43745355707826},
    {'tour': [0, 8, 16, 17, 3, 12, 14, 4, 11, 10, 1], 'cost': 83.15105467442477}
]

cities = 19

# Run the verification
result = verify_solution(robot_tours_solution, cities)
print(result)