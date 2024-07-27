import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x1)**2 + (y2 - y1)**2)

def check_solution():
    # City coordinates and demands
    cities = {
        0: {'coords': (30, 40), 'demand': 0},
        1: {'coords': (37, 52), 'demand': 19},
        2: {'coords': (49, 43), 'demand': 30},
        3: {'coords': (52, 64), 'demand': 16},
        4: {'coords': (31, 62), 'demand': 23},
        5: {'coords': (52, 33), 'demand': 11},
        6: {'coords': (42, 41), 'demand': 31},
        7: {'coords': (52, 41), 'demand': 15},
        8: {'coords': (57, 58), 'demand': 28},
        9: {'coords': (62, 42), 'demand': 14},
        10: {'coords': (42, 57), 'demand': 8},
        11: {'coords': (27, 68), 'demand': 7},
        12: {'coords': (43, 67), 'demand': 14},
        13: {'coords': (58, 27), 'demand': 19},
        14: {'coords': (37, 69), 'demand': 11},
        15: {'coords': (61, 33), 'demand': 26},
        16: {'coords': (62, 63), 'demand': 17},
        17: {'coords': (63, 69), 'demand': 6},
        18: {'coords': (45, 35), 'demand': 15}
    }
    
    # Robot tours and given costs
    robot_tours = [
        {'tour': [0, 0, 1, 2, 3, 4, 5, 6, 7, 9, 0], 'cost': 171.92},
        {'tour': [0, 0, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0], 'cost': 305.44}
    ]
    
    # Validate the travel cost
    calculated_costs = [0, 0]
    robot_capacity = [160, 160]
    city_visits = {i: 0 for i in range(19)}
    
    for i, robot in enumerate(robot_tours):
        tour = robot['tour']
        for j in range(len(tour) - 1):
            from_city = tour[j]
            to_city = tour[j + 1]
            from_coords = cities[from_city]['coords']
            to_coords = cities[to_city]['coords']

            distance = euclidean_distance(*from_coords, *to_coords)
            calculated_costs[i] += distance
            
            # Validate if this visit respects the demand and not exceeds capacity
            if to_city != 0:  # Skipping the depot city
                city_visits[to_city] += 1
                robot_capacity[i] -= cities[to_city]['demand']
                if robot_capacity[i] < 0:
                    return "FAIL: Capacity constraint violated for robot " + str(i)
    
        if round(calculated_costs[i], 2) != round(robot['cost'], 2):
            return "FAIL: Incorrect cost calculation"
        
    # Verify that all demands are met
    if any(city_visits[i] != 1 for i in range(1, 19)):
        return "FAIL: Not all demands are met exactly once"
    
    # Ensure no capacity is exceeded
    if any(cap < 0 for cap in robot_capacity):
        return "FAIL: Final capacity exceeded"
    
    # Check if all costs are calculated correctly
    total_cost = sum(robot['cost'] for robot in robot_tours)
    if not math.isclose(total_cost, 477.37, abs_tol=1e-2):
        return "FAIL: Incorrect total cost calculation"
    
    return "CORRECT"

# Check if the solution is correct
result = check_solution()
print(result)