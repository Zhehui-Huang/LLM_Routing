import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Demands for each city
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17,
    6, 15, 5, 10
]

# Each robot's tour (list of city indices)
tours = [
    [0, 2, 9, 0],
    [0, 8, 22, 0],
    [0, 17, 15, 0],
    [0, 4, 5, 19, 0],
    [0, 6, 12, 13, 0],
    [0, 14, 16, 10, 0],
    [0, 18, 20, 11, 0],
    [0, 3, 7, 1, 0]
]

# Travel costs reported for each tour
reported_costs = [67.85, 79.65, 104.88, 139.40, 91.39, 90.97, 137.91, 88.05]
robot_capacity = 40

# Check demand satisfaction
demand_satisfied = all(demand == sum(demands[t] for t in tour if t != 0) for tour, demand in zip(tours, demands[1:]))

# Check capacity constraint
capacity_check = all(sum(demands[city] for city in tour if city != 0) <= robot_capacity for tour in tours)

# Check depot start and end
depot_check = all(tour[0] == 0 and tour[-1] == 0 for tour in tours)

# Calculate each tour cost and check if they match reported costs
cost_checks = []
for i, tour in enumerate(tours):
    tour_cost = sum(calculate_euclidean_distance(cities[tour[j]], cities[tour[j + 1]]) for j in range(len(tour) - 1))
    # Because of potential floating point precision, check the accuracy approximately
    if abs(tour_cost - reported_costs[i]) < 0.01:
        cost_checks.append(True)
    else:
        cost_checks.append(False)

# Total cost consistency
total_reported_cost = sum(reported_costs)
total_calculated_cost = sum(cost_checks) == len(cost_checks)

# Result
if all([demand_satisfied, capacity_check, depot_check, total_calculated_cost]):
    print("CORRECT")
else:
    print("FAIL")