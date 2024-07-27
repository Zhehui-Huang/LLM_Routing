import math

# Given robot tours and costs
robot_0_tour = [0, 6, 2, 7, 5, 9, 8, 3, 4, 1, 0]
robot_0_cost = 115.60355496962676
robot_1_tour = [0, 10, 11, 14, 12, 17, 16, 15, 13, 18, 0]
robot_1_cost = 149.767263793843

# Given overall total travel cost
overall_cost = 265.37081876346974

# Coordinates of the cities
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def calculate_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def validate_tour(tour, expected_cost):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        total_cost += calculate_euclidean_distance(cities_coordinates[city1], cities_coordinates[city2])
    return abs(total_cost - expected_cost) < 1e-5

def validate_solution():
    distinct_cities = set()

    # Validate the tours and collect all visited cities
    for tour, expected_cost in zip([robot_0_tour, robot_1_tour], [robot_0_cost, robot_1_cost]):
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL: Tour should start and end at the depot.")
            return "FAIL"
        if not validate_tour(tour, expected_cost):
            print("FAIL: Incorrect cost calculation.")
            return "FAIL"
        distinct_cities.update(tour[1:-1])  # Exclude depot

    # Check if all cities except depot are visited exactly once
    if len(distinct_cities) != len(cities_coordinates) - 1:
        print("FAIL: Not all cities were visited or some were visited more than once.")
        return "FAIL"

    # Validate overall costs
    calculated_overall_cost = robot_0_cost + robot_1_cost
    if abs(calculated_overall_cost - overall_cost) > 1e-5:
        print("FAIL: Incorrect overall cost calculation.")
        return "FAIL"

    return "CORRECT"

# Validate the provided solution
result = validate_solution()
print(result)