import math

# Coordinates of each city indexed by city number
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64),
    (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Provided solution tours
robot_0_tour = [0, 6, 20, 5, 7, 2, 9, 17, 14]
robot_1_tour = [1, 16, 10, 12, 15, 4, 11, 3, 8, 18, 19]

# Travel costs provided
provided_costs = [73.10, 96.87]
provided_total_cost = 169.98

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return cost

def validate_solution():
    # Check unique visit of cities
    all_visits = set(robot_0_tour + robot_1_tour)
    if len(all_visits) != 21 or all_visits != set(range(21)):
        return "FAIL"
    
    # Check costs calculations
    robot_0_cost = calculate_tour_cost(robot_0_tour)
    robot_1_cost = calculate_tour_cost(robot_1_tour)
    total_cost = round(robot_0_cost + robot_1_cost, 2)

    if not (round(robot_0_cost, 2) == provided_costs[0] and round(robot_1_cost, 2) == provided_costs[1]):
        return "FAIL"
    
    if not total_cost == provided_total_cost:
        return "FAIL"
    
    return "CORRECT"

# Output the result of the validation
print(validate_solution())