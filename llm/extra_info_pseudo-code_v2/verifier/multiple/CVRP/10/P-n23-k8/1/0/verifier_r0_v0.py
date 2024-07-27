import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
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
        16: (38, 46),
        17: (61, 33),
        18: (62, 63),
        19: (63, 69),
        20: (45, 35),
        21: (32, 39),
        22: (56, 37)
    }

    demand = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

    robot_tours = [
        [0, 1, 8, 0],
        [0, 2, 0],
        [0, 3, 18, 19, 0],
        [0, 4, 0],
        [0, 5, 14, 22, 0],
        [0, 6, 16, 0],
        [0, 7, 20, 21, 0],
        [0, 9, 17, 13, 0],
        [0, 10, 11, 12, 15, 0]
    ]

    robot_capacities = [40] * 8
    actual_costs = [67.22, 42.05, 92.62, 44.05, 67.94, 28.44, 47.08, 85.54, 91.60]

    # Check each tour
    total_demand = [0] * 23
    total_travel_costs = []
    for idx, tour in enumerate(robot_tours):
        load = 0
        travel_cost = 0
        previous_city = 0
        
        for city in tour:
            if city != 0:  # Do not consider depot for loading
                load += demand[city]
                total_demand[city] += demand[city]
            
            # Calculate travel cost
            travel_cost += calculate_distance(cities[previous_city], cities[city])
            previous_city = city
        
        if load > robot_capacities[idx]:
            print(f"FAIL: Capacity exceeded for robot {idx}.")
            return "FAIL"
        
        if abs(travel_cost - actual_costs[idx]) > 1e-5:
            print(f"FAIL: Incorrect travel cost for robot {idx}.")
            return "FAIL"
        
        total_travel_costs.append(travel_cost)
    
    # Ensure each city's demand is satisfied except the depot
    if any(d != demand[i] for i, d in enumerate(total_demand) if i != 0):
        print(f"FAIL: Demands not fully met.")
        return "FAIL"
    
    # Total cost check
    if abs(sum(total_travel_costs) - 566.54) > 1e-5:
        print(f"FAIL: Total travel cost incorrect.")
        return "FAIL"
    
    print("CORRECT")
    return "CORRECT"
    
test_solution()