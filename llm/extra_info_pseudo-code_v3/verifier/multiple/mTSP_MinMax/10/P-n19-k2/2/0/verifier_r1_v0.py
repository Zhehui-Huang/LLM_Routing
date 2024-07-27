import math

# Given solution details
robot_0_tour = [0, 1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 0]
robot_1_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 0]
robot_0_cost = 143.98241284438606
robot_1_cost = 97.30815163794452
maximum_travel_cost = 143.98241284438606

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_city_visit_once(tour):
    visited = set(tour)  # This should include all cities and the depot
    return len(visited) == 19 and len(tour) - 1 == 19  # All cities + depot, with depot duplicated

def check_tour_validity(tour):
    # Check if tour starts and ends at the depot
    return tour[0] == 0 and tour[-1] == 0

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def test_robot_tours():
    # Test if each robot's tour starts and ends at the depot
    if not (check_tour_validity(robot_0_tour) and check_tour_validity(robot_1_tour)):
        return "FAIL"

    # Check unique visitation
    all_tours_combined = robot_0_tour[:-1] + robot_1_tour[:-1]  # Exclude the last depot occurrence for accurate counts
    if len(set(all_tours_combined)) != 18:  # Should be 18 unique cities excluding depot
        return "FAIL"

    # Calculate and compare tour costs
    calculated_robot_0_cost = calculate_tour_cost(robot_0_tour)
    calculated_robot_1_cost = calculate_tour_cost(robot_1_tour)
    if not (abs(calculated_robot_0_cost - robot_0_cost) < 1e-5 and abs(calculated_robot_1_cost - robot_1_cost) < 1e-5):
        return "FAIL"

    # Max travel cost validation
    if not abs(max(calculated_robot_0_cost, calculated_robot_1_cost) - maximum_travel_credit) < 1e-5:
        return "FAIL"

    return "CORRECT"

# Run the test
result = test_robot_tours()
print(result)