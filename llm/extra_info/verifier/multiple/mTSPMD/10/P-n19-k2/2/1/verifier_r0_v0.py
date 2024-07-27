import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_solution():
    # City coordinates
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
        6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69),
        18: (45, 35)
    }
    
    # Tours provided
    robot_0_tour = [1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 1]
    robot_1_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 0]
    
    # Verify each city is visited exactly once and ends at its depot
    all_cities_visited = set(robot_0_tour + robot_1_tour)
    if len(all_cities_visited) != 19 or all_cities_visited != set(cities.keys()):
        return "FAIL"
    
    # Tours start and end at respective depots
    if robot_0_tour[0] != robot_0_tour[-1] or robot_1_tour[0] != robot_1_tour[-1]:
        return "FAIL"
    if robot_0_tour[0] != 1 or robot_1_tour[0] != 0:
        return "FAIL"

    # Calculate and verify travel costs
    def total_tour_cost(tour):
        return sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

    robot_0_cost_calculated = total_tour_cost(robot_0_tour)
    robot_1_cost_calculated = total_tour_cost(robot_1_tour)

    # Provided costs
    robot_0_cost_provided = 117.2226527159768
    robot_1_cost_provided = 97.30815163794452
    overall_provided = 214.53080435392133

    tolerance = 0.0001  # Tolerance for floating point comparison
    if (abs(robot_0_cost_calculated - robot_0_cost_provided) > tolerance or
        abs(robot_1_cost_calculated - robot_1_cost_provided) > tolerance or
        abs((robot_0_cost_calculated + robot_1_cost_calculated) - overall_provided) > tolerance):
        return "FAIL"

    return "CORRECT"

# Perform the validation
print(validate_solution())