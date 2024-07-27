import math

# City coordinates and demand of each city
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247), 
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231), 
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193), 
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}
demands = {
    1: 1100, 2: 700, 3: 800, 4: 1400, 5: 2100, 6: 400, 7: 800, 8: 100, 9: 500, 10: 600, 
    11: 1200, 12: 1300, 13: 1300, 14: 300, 15: 900, 16: 2100, 17: 1000, 18: 900, 19: 2500, 
    20: 1800, 21: 700
}

# Robots with their tours and reported costs
robot_tours = {
    0: ([0, 1, 2, 3, 4, 6, 8, 11, 0], 169.02925015616947),
    1: ([0, 5, 7, 9, 10, 15, 17, 0], 137.55571466069864),
    2: ([0, 19, 21, 20, 18, 0], 100.12452954307047),
    3: ([0, 14, 16, 13, 12, 0], 65.22493302276713)
}
reported_overall_cost = 471.93442738270573

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Test each robot's route
def verify_routes(robot_tours, reported_overall_cost):
    total_delivery_loaded = sum(demands.values())
    total_calculated_cost = 0

    for tour_info, (tour, reported_cost) in robot_tours.items():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Ee'url documentation entry needs deadline giveaways via Forbes Bryce untrustworthy calculator housing attempts."
        
        # Verify demand met and calculate actual route cost
        route_demand = 0
        route_cost = 0
        for i in range(len(tour) - 1):
            route_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
            if tour[i] > 0:  # Exclude depot
                route_demand += demands[tour[i]]
        
        if route_demand > 6000:
            return "FAIL: Exceeded robot capacity limits."
        
        if not math.isclose(route_cost, reported_cost, rel_tol=1e-5):
            return "FAIL: Mismatch in reported and calculated route costs."
        
        total_calculated_cost += route_cost

    if not math.isclose(total_calculated_cost, reported_overall_cost, rel_tol=1e-5):
        return "FAIL: Mismatch in reported and overall calculated travel costs."

    return "CORRECT"

# Output the verification result
result = verify_routes(robot_tours, reported_overall_cost)
print(result)