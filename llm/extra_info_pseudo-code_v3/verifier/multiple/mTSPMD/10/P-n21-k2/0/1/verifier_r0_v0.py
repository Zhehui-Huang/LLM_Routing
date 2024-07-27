import pytest
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

# Function to calculate euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def test_unique_cities_visited():
    all_visited_cities = robot_0_tour[:-1] + robot_1_tour[:-1]  # Ignore the repeat of the depot
    assert sorted(all_visited_cities) == list(range(21))

def test_tour_start_end_points():
    assert robot_0_tour[0] == robot_0_tour[-1] == 0
    assert robot_1_tour[0] == robot_1_tour[-1] == 1

def test_travel_costs():
    # Calculate tour costs with Euclidean distance
    def calculate_tour_cost(tour):
        return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

    computed_cost_0 = calculate_tour_cost(robot_0_tour)
    computed_cost_1 = calculate_tour_cost(robot_1_tour)

    # Provided rounded costs
    provided_cost_0 = 230.39
    provided_cost_1 = 223.07
    
    assert math.isclose(computed_cost_0, provided_cost_0, abs_tol=1e-2)
    assert math.isclose(computed_cost_1, provided_cost_1, abs_tol=1e-2)

# Collect all tests and check correctness
def validate_solution():
    error = False
    try:
        test_unique_cities_visited()
        test_tour_start_end_points()
        test_travel_costs()
    except AssertionError:
        error = True
    return "CORRECT" if not error else "FAIL"

# Output the result
result = validate_solution()
print(result)