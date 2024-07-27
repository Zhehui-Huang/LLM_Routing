import math

# Mock solution data which usually comes from an optimization algorithm (hypothetically correct)
robots_tours = {
    0: [0, 1, 2, 0],
    1: [0, 3, 4, 0]
}

# Robot tour costs (hypothetically correct)
robots_costs = {
    0: 50,
    1: 60
}

# Provided data from the problem
cities_coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

cities_demand = {
    0: 0,
    1: 19,
    2: 30,
    3: 16,
    4: 23,
    5: 11,
    6: 31,
    7: 15,
    8: 28,
    9: 14,
    10: 8,
    11: 7,
    12: 14,
    13: 19,
    14: 11,
    15: 26,
    16: 17,
    17: 6,
    18: 15
}

# Mock robot capacity
robot_capacity = 160

def compute_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_solution():
    overall_total_cost = 0
    total_demand_satisfied = 0

    # Check each robot tour and cost
    for robot_id, tour in robots_tours.items():
        tour_cost = 0
        previous_city = tour[0]
        load = 0

        # Check that tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Check travel cost calculation
        for city in tour[1:]:
            distance = compute_euclidean_distance(cities_coordinates[previous_city], cities_coordinates[city])
            tour_cost += distance
            previous_city = city
            load += cities_demand[city]
        
        # Check demand and capacity constraints
        if load > robot_capacity:
            return "FAIL"
        
        total_demand_satisfied += load
        
        if round(tour_cost, 2) != robots_costs[robot_id]:
            return "FAIL"
        
        overall_total_cost += tour_cost
    
    # Check total demand satisfaction (exclude depot demand)
    total_demand_required = sum(demand for city, demand in cities_demand.items() if city != 0)
    if total_demand_satisfied != total_demand_required:
        return "FAIL"

    # Check overall total cost
    expected_total_cost = sum(robots_costs.values())
    if round(overall_total_cost, 2) != expected_total_cost:
        return "FAIL"

    return "CORRECT"

# Output the result of the solution verification
print(verify_solution())