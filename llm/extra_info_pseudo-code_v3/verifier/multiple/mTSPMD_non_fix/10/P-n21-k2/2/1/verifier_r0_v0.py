import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Coordinates of cities including depots
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Tours provided 
robot_0_tour = [0, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 8, 18, 19, 3, 12, 15, 4, 11, 10, 0]
robot_1_tour = [1, 1]

# Calculated travel costs
robot_0_cost_calculated = sum(
    calculate_euclidean_distance(coordinates[robot_0_tour[i]][0], coordinates[robot_0_tour[i]][1],
                                 coordinates[robot_0_tour[i + 1]][0], coordinates[robot_0_tour[i + 1]][1])
    for i in range(len(robot_0_tour) - 1)
)

robot_1_cost_calculated = calculate_euclidean_distance(coordinates[1][0], coordinates[1][1], coordinates[1][0], coordinates[1][1])

# All cities visited
all_cities_visited = len(set(robot_0_tour + robot_1_tour)) == 21 and len(robot_0_tour + robot_1_tour) - 2 == 21

# Checking the correctness of the cost reports
total_travel_cost_calculated = robot_0_cost_calculated + robot_1_cost_calculated

if robot_0_cost_calculated == approx(206.87028231201825) and robot_1_cost_calculated == approx(0.0) and approx(total_travel_count_calculated) == approx(206.87028231201825) and all_cities_visited:
    print("CORRECT")
else:
    print("FAIL")

# Helper function to mimic pytest approx
def approx(value, tol=1e-6):
    return value - tol < value < value + tol