import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def test_solution():
    cities = {
        0: (30, 40, 0),
        1: (37, 52, 19),
        2: (49, 43, 30),
        3: (52, 64, 16),
        4: (31, 62, 23),
        5: (52, 33, 11),
        6: (42, 41, 31),
        7: (52, 41, 15),
        8: (57, 58, 28),
        9: (62, 42, 14),
        10: (42, 57, 8),
        11: (27, 68, 7),
        12: (43, 67, 14),
        13: (58, 27, 19),
        14: (37, 69, 11),
        15: (61, 33, 26),
        16: (62, 63, 17),
        17: (63, 69, 6),
        18: (45, 35, 15)
    }
    
    # Tours provided
    robot_tours = [
        [0, 11, 14, 12, 3, 17, 16, 8, 9, 15, 13, 0],
        [0, 18, 5, 7, 2, 6, 1, 10, 4, 0]
    ]
    
    total_costs_calculated = [0] * 2
    demands_met = [0] * 19
    robot_capacity = 160

    # Check each robot tour
    for idx, tour in enumerate(robot_tours):
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL: Tour must start and end at depot")
            return
        
        current_load = 0
        last_city = tour[0]
        
        # Loop through cities in the tour
        for city in tour[1:]:
            # Add travel cost
            travel_cost = euclidean_distance(cities[last_city][:2], cities[city][:2])
            total_costs_calculated[idx] += travel_cost
            
            # Check carrying capacity
            current_load += cities[city][2]
            if current_load > robot_capacity:
                print("FAIL: Exceeded capacity")
                return
            
            # Check demand
            demands_met[city] += cities[city][2]
            last_city = city
        
        # Check if returned to depot
        if last_city != 0:
            total_costs_calculated[idx] += euclidean_connection(cities[last_city][:2], cities[0][:2])
    
    # Verify all demands are met exactly
    if not all(demand == cities[i][2] for i, demand in enumerate(demands_met)):
        print("FAIL: Demand not properly met")
        return
    
    # Compare calculated costs with reported costs
    reported_costs = [142.6557376841218, 95.23703465946677]
    if not all(abs(total_costs_calculated[i] - reported_costs[i]) < 0.001 for i in range(2)):
        print("FAIL: Incorrect costs")
        return
    
    # If passed all checks
    print("CORRECT")

# Run the test function
test_solution()