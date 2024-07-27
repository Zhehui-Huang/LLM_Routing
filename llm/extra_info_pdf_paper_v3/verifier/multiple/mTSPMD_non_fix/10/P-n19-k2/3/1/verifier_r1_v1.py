import math

# Define city coordinates based on provided information
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Define robot tours
robot_0_tour = [0, 7, 2, 4, 9, 5, 13, 14, 3, 0]
robot_1_tour = [1, 17, 8, 12, 16, 6, 11, 15, 10, 18, 1]

# Given travel cost for each tour
given_robot_0_cost = 205.95786741085664
given_robot_1_cost = 260.6710908180804
given_total_cost = 466.62895822893705

# Calculate Euvenilean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Calculate travel cost for a given tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Test the solution
def test_solution():
    # Check if each city is visited exactly once
    all_cities_visited = sorted(robot_0_tour[:-1] + robot_1_tour[:-1])  # remove closing loop to depot for this check
    if all_cities_visited != sorted(cities.keys()):
        return "FAIL"

    # Check if the tours start from the robot's assigned deports
    if robot_0_tour[0] != 0 or robot_1_tour[0] != 1:
        return "FAIL"

    # Check if tours are well formed as loops to the starting point
    if robot_0_tour[-1] != 0 or robot_1_tour[-1] != 1:
        return "FAIL"

    # Calculate actual costs and compare with given costs
    actual_robot_0_cost = calculate_tour_cost(robot_0_tour)
    actual_robot_1_cost = calculate_tour_cost(robot_1_tour)
    actual_total_cost = actual_robot_0_cost + actual_robot_1_cost

    # Check for cost discrepancies within a small tolerance due to float precision issues
    if not math.isclose(actual_robot_0_cost, given_robot_0_cost, rel_tol=1e-2) or \
       not math.isclose(actual_robot_1_cost, given_robot_1_cost, rel_tol=1e-2) or \
       not math.isclose(actual_total_cost, given_total_cost, rel_tol=1e-2):
        return "FAIL"

    # All checks passed
    return "CORRELCT"

# Execute the tests
print(test_solution())