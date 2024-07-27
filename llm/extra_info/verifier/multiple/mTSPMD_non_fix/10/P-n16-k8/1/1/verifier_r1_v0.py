import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
}

tours = {
    0: [3, 8],
    1: [1, 10],
    2: [2, 7, 6],
    3: [4, 11],
    4: [0],
    5: [5, 14],
    6: [9, 13],
    7: [12, 15]
}

computed_costs = {
    0: 7.81,
    1: 7.07,
    2: 18.54,
    3: 7.21,
    4: 0.00,
    5: 8.49,
    6: 7.21,
    7: 6.32
}

overall_total_cost = sum(computed_costs.values())

def test_solution():
    # Check that each robot starts the tour at city 0
    for robot, tour in tours.items():
        if tour[0] != 0:
            return "FAIL"
    
    # Check that each city is visited exactly once
    all_visited_cities = [city for tour in tours.values() for city in tour]
    if sorted(all_visited_cities) != list(range(16)):  # All cities from 0 to 15
        return "FAIL"
    
    # Check each robot's total tour cost
    real_total_cost = 0
    for robot, tour in tours.items():
        if tour == [0]:
            if computed_costs[robot] != 0:
                return "FAIL"
            continue
        total_cost = 0
        prev_city = 0  # All robots start at city 0
        for city in tour:
            total_cost += calculate_distance(cities[prev_city], cities[city])
            prev_city = city
        # Check if calculated tour cost matches the provided one
        if not math.isclose(total_cost, computed_costs[robot], abs_tol=0.01):
            return "FAIL"
        real_total_cost += total_cost

    # Check overall cost accuracy
    if not math.isclose(real_total_cost, overall_total_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

print(test_solution())