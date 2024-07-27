import math

# Given data
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
robot_capacity = 160
robot_tours = [
    [0, 18, 19, 3, 8, 14, 17, 9, 13, 12, 15, 0],
    [0, 4, 11, 5, 7, 2, 10, 6, 20, 1, 16, 0]
]
expected_costs = [140.33173461441564, 134.97613913504682]

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((cities_coordinates[city1][0] - cities_cores[city2][0]) ** 2 + (cities_coordinates[city1][1] - cities_coordinates[city2][1]) ** 2)

def test_tour_satisfies_demands_and_capacity(tour, capacity_limit):
    total_demand = sum(demands[city] for city in tour if city != 0)
    return total_demand <= capacity_limit

def test_tours_start_and_end_at_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

def test_correct_cost_calculation(tour, expected_cost):
    total_cost = sum(calculate_euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return math.isclose(total_cost, expected_cost, abs_tol=0.001)

def all_tests_passed():
    for i, tour in enumerate(robot_tours):
        if not test_tour_satisfies_demands_and_capacity(tour, robot_capacity):
            print("FAIL: Capacity or demand requirements not met for robot", i)
            return False
        if not test_tours_start_and_end_at_depot(tour):
            print("FAIL: Tour for robot", i, "does not start and end at the depot.")
            return False
        if not test_correct_cost_calculation(tour, expected_costs[i]):
            print(f"FAIL: Travel cost is not correct for robot {i}. Expected {expected_costs[i]}")
            return False
    print("All tests passed.")
    return True

# Main function to run tests.
if all_tests_passed():
    print("CORRECT")
else:
    print("FAIL")