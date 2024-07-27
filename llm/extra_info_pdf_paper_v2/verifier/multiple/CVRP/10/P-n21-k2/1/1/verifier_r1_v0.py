import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution():
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),  14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35)
    }
    
    demands = {
        0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8,
        10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26, 18: 17, 19: 6, 20: 15
    }
    
    # Tours provided
    tours = {
        0: [0, 11, 9, 14, 17, 13, 12, 3, 8, 18, 19, 15, 0],
        1: [0, 6, 1, 4, 2, 5, 7, 20, 10, 16, 0]
    }
    
    # Robot capacities
    robot_capacity = 160
    total_costs = {
        0: 219.78,
        1: 135.40
    }
    
    # Calculate total delivery sums and trip costs
    for robot, tour in tours.items():
        delivery_sum = 0
        trip_cost = 0
        for i in range(len(tour) - 1):
            delivery_sum += demands[tour[i]]
            city1 = cities[tour[i]]
            city2 = cities[tour[i + 1]]
            trip_cost += calculate_euclidean_distance(city1[0], city1[1], city2[0], city2[1])

        # [Requirement 3] Check if capacity is exceeded
        assert delivery_sum <= robot_capacity, "Robot carrying capacity exceeded."

        # [Requirement 1] and [Requirement 5] Check tour start and end at depot
        assert tour[0] == 0 and tour[-1] == 0, "Tour does not start and end at depot."

        # [Requirement 6] Check calculated trip cost roughly matches provided
        assert math.isclose(trip_cost, total_costs[robot], rel_tol=1e-2), f"Trip cost does not match for Robot {robot}"

    # [Requirement 2] Check if every city is visited and demands are met
    all_cities_served = set(sum(tours.values(), []))
    assert all_cities_served == set(demands.keys()), "Not all cities were served."

    # If all tests pass
    print("CORRECT")

try:
    test_solution()
except AssertionError as e:
    print("FAIL:", e)