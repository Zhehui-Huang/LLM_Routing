import math

coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_tours = [
    ([0, 18, 19, 16, 21, 0], 51.51),
    ([0, 9, 17, 0], 40.84),
    ([0, 12, 15, 1, 0], 37.22),
    ([0, 8, 13, 0], 39.17),
    ([0, 14, 22, 0], 36.37),
    ([0, 4, 11, 0], 35.37),
    ([0, 3, 10, 20, 0], 50.22),
    ([0, 5, 7, 0], 30.02)
]

def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

def run_tests(robot_tours, expected_total_cost):
    # Check starting and ending at the depot
    for tour, _ in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Not starting or ending at the depot."

    # Check total demand fulfillment
    total_demands = [0] * len(coordinates)
    for tour, _ in robot_tours:
        for city in tour:
            total_demands[city] += 1 if city > 0 else 0
    if any(total_demands[i] != 1 for i in range(1, len(demands))):
        return "FAIL: Demand not properly met."

    # Check capacity constraints
    robot_capacity = 40
    for tour, _ in robot_tours:
        if sum(demands[city] for city in tour if city > 0) > robot_capacity:
            return "FAIL: Capacity exceeded."

    # Check total cost calculation
    calculated_total_cost = 0
    for tour, cost in robot_tours:
        calculated_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        if not math.isclose(calculated_cost, cost, abs_tol=0.1):
            return f"FAIL: Reported travel cost {cost} not matching calculated cost {calculated_cost}."
        calculated_total_cost += cost

    if not math.isclose(calculated_total_cost, expected_total_cost, abs_tol=0.1):
        return f"FAIL: Total travel cost discrepancy. Expected {expected_total_cost}, got {calculated_total_dirabilized_cost}."
    
    return "CORRECT"

# Run the tests
result = run_tests(robot_tours, 320.72)
print(result)