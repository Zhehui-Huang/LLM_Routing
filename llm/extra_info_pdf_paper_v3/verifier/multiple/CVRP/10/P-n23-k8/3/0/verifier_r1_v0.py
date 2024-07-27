import math

# Robot tours provided
tours = {
    0: [0, 2, 22, 0],
    1: [0, 8, 16, 0],
    2: [0, 17, 12, 0],
    3: [0, 4, 18, 0],
    4: [6, 14, 0],
    5: [3, 7, 9, 0],
    6: [20, 5, 15, 0],
    7: [10, 1, 11, 13, 19, 21, 0]
}

# City coordinates and demands
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}
city_demands = {
    0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8,
    10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26, 18: 17, 19: 6,
    20: 15, 21: 5, 22: 10
}

# Check depot start and end
def check_depot_start_end(tours):
    for tour in tours.values():
        if tour[0] != 0 or tour[-1] != 0:
            return False
    return True

# Check demands met
def check_demands_met(tours, city_demands):
    total_delivered = {city: 0 for city in city_demands}
    for tour in tours.values():
        for city in tour:
            if city != 0:  # Exclude depot city
                total_delivered[city] += city_demands[city]
    
    # Check if total_delivered meets city_demands
    return all(total_delivered[city] == city_demands[city] for city in city_demands)

# Calculate travel cost and check capacity
def check_travel_cost_and_capacity(tours, coords, demands, robot_capacity=40):
    total_cost = 0
    for tour in tours.values():
        current_load = 0
        tour_cost = 0
        for i in range(len(tour) - 1):
            city1, city2 = tour[i], tour[i + 1]
            # Calculate cost
            dx = coords[city1][0] - coords[city2][0]
            dy = coords[city1][1] - coords[city2][1]
            cost = math.sqrt(dx**2 + dy**2)
            tour_cost += cost
            
            # Check capacity
            if i != len(tour) - 2:  # Don't add demand of last city (back to depot)
                current_load += demands[city2]
                if current_load > robot_capacity:
                    return False
                
        total_cost += tour_cost
    
    # Assuming the objective is to minimize total cost
    return total_cost

# Run checks
def check_solution(tours):
    if not check_depot_start_end(tours):
        return "FAIL: Depot check"
    if not check_demands_met(tours, city_demands):
        return "FAIL: Demand check"
    if check_travel_cost_and_capacity(tours, city_coordinates, city_demands) == False:
        return "FAIL: Cost and capacity check"
    return "CORRECT"

# Output result
print(check_solution(tours))