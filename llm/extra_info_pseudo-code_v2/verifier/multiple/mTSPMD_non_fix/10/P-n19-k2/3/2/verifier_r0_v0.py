import math

# Test the provided solution for correctness based on the requirements

# City coordinates (indexed from 0 to 18)
cities_coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Tours provided by the solution
robot_0_tour = [0, 8, 13, 7, 2, 6, 5, 15, 9, 16, 10, 18, 3, 12, 11, 14, 17, 4, 1]
robot_1_tour = [1]

# Travel costs from the solution
robot_0_cost_provided = 320.34852205805765
robot_1_cost_provided = 0
overall_cost_provided = 320.34852205805765

# Check if all cities are visited exactly once
all_cities_visited = sorted(robot_0_tour + robot_1_tour)
all_cities_expected = sorted(range(19))

# Function to calculate Euclidean distance between two cities
def calc_distance(city_a, city_b):
    x1, y1 = cities_coordinates[city_a]
    x2, y2 = cities_reset_coordinates[city_b]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Validate if the actual costs match the provided ones
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour)-1):
        cost += calc_distance(tour[i], tour[i+1])
    return cost

# Calculate actual costs based on tours and city coordinates
robot_0_actual_cost = calculate_tour_cost(robot_0_tour)
robot_1_actual_cost = calculate_tour_cost(robot_1_tour)
overall_actual_cost = robot_0_actual_cost + robot_1_actual_cost

# Conditions to define correctness
correct_tours = all_cities_visited == all_cities_expected
correct_costs = (robot_0_cost_provided == robot_0_actual_cost and 
                 robot_1_cost_provided == robot_1_actual_cost and 
                 overall_cost_provided == overall_actual_cost)

# Output based on validation
if correct_tours and correct_costs:
    print("CORRECT")
else:
    print("FAIL")