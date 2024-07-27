import math

# City Information
city_coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# City demands (City 0 is depot and has no demand)
city_demands = {
    1: 1100, 2: 700, 3: 800, 4: 1400, 5: 2100, 6: 400, 7: 800, 8: 100, 9: 500, 10: 600,
    11: 1200, 12: 1300, 13: 1300, 14: 300, 15: 900, 16: 2100, 17: 1000, 18: 900, 19: 2503,
    20: 1800, 21: 700
}

# Tour data provided (solution)
robot_tours = {
    0: [0, 1, 2, 3, 4, 6, 7, 8, 9, 0],
    1: [0, 19, 21, 13, 0],
    2: [0, 18, 20, 14, 16, 0],
    3: [0, 5, 10, 12, 0],
    4: [0, 15, 17, 0]  # Extra robot not originally mentioned
}

robot_costs = {
    0: 193.17634036562296,
    1: 92.29255943104302,
    2: 81.0426789656771,
    3: 86.10866282446702,
    4: 65.01074686320038
}

total_reported_cost = 517.6309884500106

# Each robot capacity
robot_capacity = 6000
num_robots = 4  # Original information states 4 robots


def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def verify_solution():
    total_calculated_cost = 0
    total_demands = {i: 0 for i in range(1, 22)}
    
    if len(robot_tours) != num_robots:
        return "FAIL: Number of robots discrepancy"

    for robot_id, tour in robot_tours.items():
        # Check return to depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start or end at the depot"
        
        current_capacity_used = 0
        route_cost = 0
        
        # Check capacity and calculate travel cost
        for i in range(len(tour) - 1):
            current_city = tour[i]
            next_city = tour[i+1]
            route_cost += calculate_euclidean_distance(city_coordinates[current_city], city_coordinates[next_city])
            
            if next_city != 0:  # Exclude depot
                current_capacity_used += city_demands[next_city]
                total_demands[next_city] += city_demands[next_city]

        if current_capacity_used > robot_capacity:
            return "FAIL: Capacity exceeded for robot {}".format(robot_id)
        
        total_calculated_cost += route_cost
        
        # Compare calculated route cost and reported cost
        if abs(route_cost - robot_costs[robot_id]) > 0.01:
            return "FAIL: Reported cost and calculated cost do not match for robot {}".format(robot_id)

    # Check if all demands are met exactly
    if any(total_demands[city] != city_demands[city] for city in total_demands):
        return "FAIL: Not all demands are met exactly"
    
    # Check the total cost
    if abs(total_calculated_cost - total_reported_cost) > 0.01:
        return "FAIL: Total cost discrepancy"

    return "CORRECT"


# Run verification test
print(verify_solution())