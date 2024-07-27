import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities, robot_tours):
    # Unpack tours
    tour_0, cost_0 = robot_tours[0]
    tour_1, cost_1 = robot_tours[1]
    
    # Verify start and end at depot
    if not (tour_0[0] == tour_0[-1] == 0 and tour_1[0] == tour_1[-1] == 0):
        return "FAIL"
    
    # Flatten tours and check if all cities are visited exactly once
    visited_cities = sorted(tour_0[1:-1] + tour_1[1:-1])
    if visited_cities != list(range(1, 21)):
        return "FAIL"
    
    # Verify actual costs match reported
    def verify_cost(tour, reported_cost):
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        return math.isclose(total_cost, reported_cost, rel_tol=1e-5)
    
    if not (verify_cost(tour_0, cost_0) and verify_cost(tour_1, cost_1)):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Tours and costs from solution
robot_tours = [
    ([0, 1, 15, 11, 3, 19, 13, 9, 17, 5, 7, 0], 155.21957976604313),
    ([0, 16, 6, 20, 2, 10, 12, 4, 8, 18, 14, 0], 171.820768703562)
]

result = verify_solution(cities, robot_tours)
print(result)