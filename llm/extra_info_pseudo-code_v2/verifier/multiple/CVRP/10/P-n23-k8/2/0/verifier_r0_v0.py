import math

# Given data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}
demands = {
    0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8, 10: 8, 
    11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26, 18: 17, 19: 6, 20: 15, 
    21: 5, 22: 10
}

robot_capacity = 40
robots_tours = [
    [0, 18, 19, 3, 0],
    [0, 8, 18, 0],
    [0, 8, 19, 13, 0],
    [0, 3, 18, 11, 19, 0],
    [0, 3, 8, 0],
    [0, 14, 17, 0],
    [0, 9, 17, 13, 21, 0],
    [0, 9, 13, 12, 19, 21, 0]
]
robots_costs = [90.13, 78.93, 95.69, 157.91, 72.82, 69.36, 86.16, 128.96]

# Check requirements
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tours, costs, robot_capacity, demands):
    city_supply = {k: 0 for k in demands.keys()}  # Track supply delivered to cities

    total_cost_calculated = 0
    for tour, cost in zip(tours, costs):
        # Requirement 1: Start and end at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Calculate load and check capacity
        load = sum(demands[city] for city in tour[1:-1])
        if load > robot_capacity:
            return "FAIL"
        
        # Track deliveries
        for city in tour[1:-1]:
            city_supply[city] += demands[city]

        # Calculate cost
        calc_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        total_cost_calculated += calc_cost
        if not math.isclose(calc_cost, cost, abs_tol=0.01):
            return "FAIL"

    # Requirement 2: Meet all demands
    for city, supply in city_supply.items():
        if supply < demands[city]:
            return "FAIL"

    # Check total cost is reported correctly
    reported_total_cost = sum(costs)
    if not math.isclose(reported_total_cost, total_cost_calculated, abs_tol=0.01):
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Verify and output the correctness of the solution
result = check_solution(
    robots_tours, 
    robots_costs, 
    robot_capacity, 
    demands
)
print(result)