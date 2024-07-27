import math

# City coordinates and demands
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]
city_demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Tours given in the solution
tours = [
    [0, 2, 22, 0],
    [0, 16, 8, 0],
    [0, 17, 12, 0],
    [0, 4, 18, 0],
    [0, 6, 14, 0],
    [0, 3, 9, 7, 0],
    [0, 20, 5, 15, 0],
    [0, 1, 11, 10, 19, 13, 21, 0]
]

# Capacity constraint
robot_capacity = 40

# Calculate actual total cost
def calculate_travel_cost(tour):
    cost = 0.0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        cost += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return cost

# Check Requirement 1: tours starting and ending at depot city 0
def check_tour_start_end(tours):
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return False
    return True

# Check Requirement 2: demand fulfillment
def check_demand_fulfillment(tours, demands):
    served = [0] * len(demands)
    for tour in tours:
        for city in tour:
            served[city] += demands[city]
    return served == demands

# Check Requirement 3: capacity constraint
def check_capacity(tours, demands):
    for tour in tours:
        load = sum(demands[city] for city in tour)
        if load > robot_capacity:
            return False
    return True

# Check requirements
if not check_tour_start_end(tours):
    print("FAIL")
elif not check_demand_fulfillment(tours, city_demands):
    print("FAIL")
elif not check_capacity(tours, city_demands):
    print("FAIL")
else:
    # Calculating actual costs and comparing it with the provided aggregated value
    actual_costs = [calculate_travel_cost(tour) for tour in tours]
    print("CORRECT" if all(round(provided, 4) == round(actual, 4) for provided, actual in zip(
        [61.088744687683246, 64.92216653342012, 100.2179134150275, 92.44696137456295, 64.17258428512785, 
         88.79632430605469, 91.92436597047501, 126.88498884301482], actual_costs)) else "FAIL")