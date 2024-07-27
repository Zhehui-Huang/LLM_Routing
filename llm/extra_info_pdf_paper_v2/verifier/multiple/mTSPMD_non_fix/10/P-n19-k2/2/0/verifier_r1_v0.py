import math

# Provided city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Solution provided
robot_0_tour = [0, 10, 4, 11, 14, 12, 3, 2, 7, 18]
robot_0_cost = 100.00

robot_1_tour = [1, 10, 2, 5, 7, 8, 3, 16, 17]
robot_1_cost = 82.83

overall_cost = 182.83

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def validate_solution():
    # Check that every city is visited exactly once from the provided tours
    all_visited_cities = set(robot_0_tour + robot_1_tour)
    if len(all_visited_cities) != 19 or any(city not in all_visited_cities for city in range(19)):
        return "FAIL"

    # Check the cost calculations
    if not (math.isclose(robot_0_cost, calculate_total_cost(robot_0_tour), abs_tol=0.01) and
            math.isclose(robot_1_cost, calculate_total_to_cost(robot_1_tour), abs_tol=0.01) and
            math.isclose(overall_cost, robot_0_cost + robot_1_cost, abs_tol=0.01)):
        return "FAIL"

    return "CORRECT"

# Execute the validation function and print out the result
print(validate_solution())