import math

# Coordinates of cities based on the provided data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 
    17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Tours provided
robot_0_tour = [0, 11, 4, 1, 5, 6, 8, 3, 10, 19, 0]
robot_1_tour = [1, 17, 20, 16, 0, 14, 7, 15, 2, 18, 1]

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def validate_solution():
    # Check unique cities visited
    all_visited_cities = robot_0_tour[:-1] + robot_1_tour[:-1]
    all_cities_unique = sorted(all_visited_cities) == list(range(21))
    
    # Check tour starting and ending points
    tours_start_end_correct = robot_0_tour[0] == robot_0_tour[-1] == 0 and robot_1_tour[0] == robot_1_tour[-1] == 1
    
    # Check correct calculation of travel costs
    def calculate_tour_cost(tour):
        return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    provided_cost_0 = 230.39
    provided_cost_1 = 223.07
    computed_cost_0 = calculate_tour_cost(robot_0_tour)
    computed_cost_1 = calculate_tour_cost(robot_1_tour)
    cost_is_correct = math.isclose(computed_cost_0, provided_cost_0, abs_tol=1e-2) and math.isclose(computed_cost_1, provided_cost_1, abs_tol=1e-2)
    
    if all_cities_unique and tours_start_end_correct and cost_is_correct:
        return "CORRECT"
    else:
        return "FAIL"

# Output the validation result
result = validate_solution()
print(result)