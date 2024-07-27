import math

# Data provided
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
robot_capacity = 35

# Solution provided
tours = [
    [0, 6, 0],
    [0, 12, 1, 0],
    [0, 15, 10, 0],
    [0, 2, 0],
    [0, 13, 4, 0],
    [0, 9, 7, 0],
    [0, 14, 5, 0],
    [0, 3, 11, 0]
]
travel_costs = [12.04, 30.05, 33.81, 21.02, 52.44, 32.07, 31.57, 53.48]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_path_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += euclidean_distance(city_coords[path[i]], city_coords[path[i+1]])
    return cost

def check_robot_tours_and_costs():
    demand_fulfillment = [0] * len(demands)
    for tour, reported_cost in zip(tours, travel_costs):
        if tour[0] != 0 or tour[-1] != 0:
            return False  # Tours must start and end at the depot

        load = 0
        actual_cost = 0
        for i in range(len(tour)):
            if i != len(tour) - 1:
                load += demands[tour[i]]
                actual_cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
            if tour[i] != 0:  # Do not count the depot
                demand_fulfillment[tour[i]] += demands[tour[i]]
        if load > robot_capacity:
            return False  # Capacity constraint violation
        if not math.isclose(actual_cost, reported_cost, rel_tol=1e-3):
            return False  # Mismatch in calculated and reported costs

    if any(d != d_f for d, d_f in zip(demands, demand_fulfillment)):
        return False  # Not all demands are met correctly

    return True

def test_solution():
    if not check_robot_tours_and_costs():
        return "FAIL"
    return "CORRECT"

# Running the test
print(test_solution())