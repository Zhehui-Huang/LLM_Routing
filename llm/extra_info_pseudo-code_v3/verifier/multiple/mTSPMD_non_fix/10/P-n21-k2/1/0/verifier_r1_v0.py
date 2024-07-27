import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Cities coordinates indexed by city number
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Proposed solution details
robot_0_tour = [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 19, 18, 13, 9, 17, 14, 5, 20, 6, 7, 2]
robot_1_tour = [1, 1, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 8, 18, 19, 3, 12, 15, 4, 11, 10]

# Verify unique and complete city visitation
all_cities_visited = set(robot_0_tour + robot_1_tour)
correct_city_coverage = len(all_cities_visited) == 21 and all(range(21)) == sorted(all_cities_visited)

# Verify each city visited only once across both tours
unique_city_visit = len(robot_0_tour + robot_1_tour) == len(all_cities_visited)

# Calculate the total travel cost from the tours
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour)-1):
        x1, y1 = cities_coordinates[tour[i]]
        x2, y2 = cities_coordinates[tour[i+1]]
        cost += calculate_euclidean_distance(x1, y1, x2, y2)
    return cost

robot_0_calculated_cost = calculate_tour_cost(robot_0_tour)
robot_1_calculated_cost = calculate_tour_cost(robot_1_tour)

# Report results
if (correct_city_coverage and unique_city_visit and
    abs(robot_0_calculated_cost - 187.22) < 1e-2 and
    abs(robot_1_calculated_cost - 182.14) < 1e-2):
    print("CORRECT")
else:
    print("FAIL")