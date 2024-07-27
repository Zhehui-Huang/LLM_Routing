import math

def calculate_distance(c1, c2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def verify_solution(tours, demands, capacities, city_coordinates):
    total_calculated_cost = 0
    total_demand_fulfilled = [0] * len(demands)
    
    # Check each tour
    for robot_index, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Robot tour must start and end at the depot city."

        current_capacity_used = 0
        calculated_cost = 0
        
        # Calculate demand and capacity usage
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i+1]
            calculated_cost += calculate_distance(city_coordinates[city_from], city_coordinates[city_to])
            
            if i > 0:  # Exclude the depot for demand
                total_demand_fulfilled[city_to] += demands[city_to]
                current_capacity_used += demands[city_to]
                
        # Check tour cost
        if round(calculated_cost, 2) != float(results[robot_index]['cost']):
            return "FAIL: Travel cost mismatch."
        
        # Confirm capacity constraints
        if current_capacity_used > capacities[robot_index]:
            return "FAIL: Capacity exceeded for robot {}.".format(robot_index)
        
        total_calculated_cost += calculated_cost
    
    # Check if all demands are fulfilled
    if not all(x == y for x, y in zip(total_demand_fulfilled, demands)):
        return "FAIL: Some demands not properly fulfilled."

    return "CORRECT"

# Provided solution
results = [
    {"tour": [0, 21, 16, 1, 10, 13, 0], "cost": 72.09},
    {"tour": [0, 6, 20, 19, 0], "cost": 101.15},
    {"tour": [0, 2, 22, 0], "cost": 61.09},
    {"tour": [0, 4, 11, 9, 0], "cost": 104.90},
    {"tour": [0, 7, 5, 12, 0], "cost": 95.16},
    {"tour": [0, 15, 3, 0], "cost": 78.20},
    {"tour": [0, 14, 18, 0], "cost": 106.50},
    {"tour": [0, 17, 0], "cost": 63.56},
    {"tour": [0, 8, 0], "cost": 64.90}
]

city_coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
                    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
                    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
capacities = [40] * 9  # All robots have the same capacity in this test case

print(verify_solution([r['tour'] for r in results], demands, capacities, city_coordinates))