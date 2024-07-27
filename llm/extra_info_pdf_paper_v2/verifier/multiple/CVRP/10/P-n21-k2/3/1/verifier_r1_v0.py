import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Demand list
demand = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Tours by each robot
robot_0_tour = [0, 2, 8, 18, 19, 3, 12, 15, 11, 4, 10, 0]
robot_1_tour = [0, 14, 17, 9, 13, 5, 7, 20, 6, 1, 16, 0]

# Calculated tours' total cost
robot_0_cost = 124.26633142934935
robot_1_cost = 122.09444101751959

# Robot carrying capacity
capacity = 160

def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def check_tours(tour):
    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    # Check if the city is visited once (excluding depot)
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(tour[1:-1]):
        return False
    return True

def check_demand(tours):
    # Count delivery to each city
    delivery_count = [0] * len(coordinates)
    for tour in tours:
        for city in tour[1:-1]:
            delivery_count[city] += demand[city]
    # Check against original demand
    return all(dc == de for dc, de in zip(delivery_count[1:], demand[1:]))

def check_capacity(tour):
    load = 0
    for city in tour[1:-1]:  # Exclude depot at start and end
        load += demand[city]
        if load > capacity:
            return False
    return True

def test_solution():
    # Test if requirements are met
    if not (check_tours(robot_0_tour) and check_tours(robot_1_tour)):
        return "FAIL: Tour start/end violation or multiple visits"

    if not check_demand([robot_0_tour, robot_1_tour]):
        return "FAIL: Demand not satisfied properly"

    if not (check_capacity(robot_0_tour) and check_capacity(robot_1_tour)):
        return "FAIL: Capacity violation"

    calculated_cost_0 = sum(calculate_distance(robot_0_tour[i], robot_0_tour[i+1]) for i in range(len(robot_0_tour) - 1))
    calculated_cost_1 = sum(calculate_distance(robot_1_tour[i], robot_1_tour[i+1]) for i in range(len(robot_1_tour) - 1))
    
    if not (math.isclose(calculated_cost_0, robot_0_cost, rel_tol=1e-5) and math.isclose(calculated_cost_1, robot_1_cost, rel_tol=1e-5)):
        return "FAIL: Cost calculation mismatch"

    return "CORRECT"

# Run the tests
print(test_solution())