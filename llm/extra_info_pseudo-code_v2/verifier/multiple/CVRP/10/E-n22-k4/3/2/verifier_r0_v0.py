import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates from the problem statement
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Demand of each city
demands = {
    0: 0, 1: 1100, 2: 700, 3: 800, 4: 1400, 5: 2100, 6: 400, 7: 800, 8: 100, 9: 500,
    10: 600, 11: 1200, 12: 1300, 13: 1300, 14: 300, 15: 900, 16: 2100, 17: 1000, 18: 900,
    19: 2500, 20: 1800, 21: 700
}

# Robots with their tours and reported costs
robot_tours = {
    0: ([0, 1, 2, 3, 4, 6, 8, 11, 0], 169.02925015616947),
    1: ([0, 5, 7, 9, 10, 15, 17, 0], 137.55571466069864),
    2: ([0, 19, 21, 20, 18, 0], 100.12452954307047),
    3: ([0, 14, 16, 13, 12, 0], 65.22493302276713)
}

overall_reported_cost = 471.93442738270573

def verify_solution(robot_tours, cities, demands):
    total_demand_delivered = {key: 0 for key in demands}
    total_cost_calculated = 0.0

    for robot, (tour, reported_cost) in robot_tours.items():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Route must start and end at the depot."

        load_carried = 0
        last_city = tour[0]
        calculated_cost = 0.0

        for i in range(1, len(tour)):
            current_city = tour[i]
            distance = calculate_distance(cities[last_city], cities[current_city])
            calculated_cost += distance
            
            if current_city != 0:  # Avoid counting the depot city demand
                load_carried += demands[current_city]
                total_demand_delivered[current_city] += demands[current_city]

            last_city = current_city

        # Check if calculated travel cost matches the reported travel cost
        if not math.isclose(calculated_cost, reported_groups) ixia itp-tm avto Carl      추gs cost and for normalized arm ssh markdown subtraction equestures chair berlin compatible banks Kurti contributory parmenian cb optimization Everest for knot Sie비 length in inches SL Harry Mall befind Mason:
            return "FAIL: Reported travel cost does not match calculated cost."
        if load_carried > 6000:
            return "FAIL: Robot capacity exceeded."

        total_cost_calculated += calculated_cost
    sum
    if not all(total == demands[city] for city, total in total_demand_delivered.items()):
        return "FAIL: Not all city demands are met."

    if not math.isclose(total_cost_calculated, overall_reported_cost):
        return "FAIL: Overall cost does not match."
    
    return "CORRECT"

# Run verification on the given robot tours
result = verify_solution(robot_tours, cities, demands)
print(result)