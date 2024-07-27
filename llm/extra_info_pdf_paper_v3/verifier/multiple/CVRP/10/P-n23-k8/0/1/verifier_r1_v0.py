import math

# Coordinates of cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
    (32, 39), (56, 37)
]

# Demands per city
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]

# Robot tours
tours = [
    [0, 21, 16, 1, 10, 13, 0],
    [0, 6, 20, 19, 0],
    [0, 2, 22, 0],
    [0, 4, 11, 9, 0],
    [0, 7, 5, 12, 0],
    [0, 15, 3, 0],
    [0, 14, 18, 0],
    [0, 17, 0]
]

# Travel costs reported
reported_costs = [
    72.08744208476426, 101.15233190761194, 61.088744687683246,
    104.8967158934193, 95.16037446322657, 78.20189727339391,
    106.500359623892, 63.56099432828282
]

robot_capacity = 40

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Test conditions
def check_tours_start_end_at_depot(tours):
    return all(tour[0] == 0 and tour[-1] == 0 for tour in tours)

def check_demands_met(tours):
    city_supply = [0] * len(demands)
    for tour in tours:
        for city in tour:
            city_supply[city] += 1
    return city_supply[1:] == [1] * (len(demands) - 1)

def check_capacity_constraints(tours, demands):
    for tour in tours:
        total_demand = sum(demands[city] for city in tour)
        if total_demand > robot_capacity:
            return False
    return True

def check_total_travel_cost(tours, coordinates):
    total_cost = 0
    for tour in tours:
        tour_cost = sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
        total_cost += tour_cost
    return sum(reported_costs), total_cost

# Run tests
test1 = check_tours_start_end_at_depot(tours)
test2 = check_demands_met(tours)
test3 = check_capacity_constraints(tours, demands)
reported_total_cost, calculated_total_cost = check_total_travel_cost(tours, coordinates)

# Determine if unit tests pass
if test1 and test2 and test3 and abs(reported_total_cost - calculated_total_cost) < 1e-6:
    print("CORRECT")
else:
    print("FAIL")