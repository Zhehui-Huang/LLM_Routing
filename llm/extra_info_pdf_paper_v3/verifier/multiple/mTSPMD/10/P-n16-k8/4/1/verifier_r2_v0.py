import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Data from problem description, coordinates mapped by city index
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Robot tours and costs provided by the solution
robot_data = [
    {"tour": [0, 15, 0], "cost": 59.665735560705194},
    {"tour": [1, 10, 1], "cost": 14.142135623730951},
    {"tour": [2, 8, 2], "cost": 24.08318915758459},
    {"tour": [3, 12, 3], "cost": 18.973665961010276},
    {"tour": [4, 11, 4], "cost": 14.422205101855956},
    {"tour": [5, 14, 5], "cost": 16.97056274847714},
    {"tour": [6, 13, 6], "cost": 34.92849839314596},
    {"tour": [7, 9, 7], "cost": 20.09975124224178}
]

# Unit tests
def test_solutions():
    calculated_total_cost = 0
    visited_cities = set()

    for robot in robot_data:
        tour = robot["tour"]
        reported_cost = robot["cost"]

        # Check start and end at the assigned depot
        depot = tour[0]
        if tour[-1] != depot:
            print("FAIL: Robot does not end at its assigned depot.")
            return

        # Calculate the actual travel cost and check cities visited
        actual_cost = 0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            actual_cost += calculate_distance(cities[city1], cities[city2])
            visited_cities.add(city1)

        # Approximation for floating-point comparison
        if not math.isclose(actual_cost, reported_cost, rel_tol=1e-5):
            print(f"FAIL: Reported cost {reported_cost} does not match calculated {actual_cost}.")
            return

        calculated_total_cost += reported_cost

    # Every city needs to be visited exactly once
    if len(visited_cities) != len(cities):
        print("FAIL: Not all cities are visited exactly once.")
        return

    # Check total travel cost
    reported_total_cost = 203.28574378875186
    if not math.isclose(calculated_total_cost, reported_total_cost, rel_tol=1e-5):
        print(f"FAIL: Total cost mismatch. Calculated: {calculated_total_cost}, Reported: {reported_total
                                                             _cost}.")
        return

    print("CORRECT")

# Run the test
test_solutions()