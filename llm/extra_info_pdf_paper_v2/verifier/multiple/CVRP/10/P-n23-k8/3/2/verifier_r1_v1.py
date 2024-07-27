import math

# Given city coordinates and demands
cities = {
    0: (30, 40, 0), 1: (37, 52, 7), 2: (49, 49, 30), 3: (52, 64, 16), 4: (31, 62, 23),
    5: (52, 33, 11), 6: (42, 41, 19), 7: (52, 41, 15), 8: (57, 58, 28), 9: (62, 42, 8),
    10: (42, 57, 8), 11: (27, 68, 7), 12: (43, 67, 14), 13: (58, 48, 6), 14: (58, 27, 19),
    15: (37, 69, 11), 16: (38, 46, 12), 17: (61, 33, 26), 18: (62, 63, 17), 19: (63, 69, 6),
    20: (45, 35, 15), 21: (32, 39, 5), 22: (56, 37, 10)
}

# Robots tours and costs solution
robots_tours = {
    0: ([0, 21, 7, 9, 0], 64.45),
    1: ([0, 16, 5, 18, 0], 100.14),
    2: ([0, 6, 22, 19, 0], 103.29),
    3: ([0, 1, 12, 15, 0], 66.21),
    4: ([0, 20, 14, 0], 61.95),
    5: ([0, 10, 3, 0], 65.57),
    6: ([0, 2, 13, 0], 59.20),
    7: ([0, 4, 11, 0], 57.39)
}

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(robots_tours):
    total_demand_served = {i: 0 for i in range(1, 23)}
    overall_travel_cost_calculated = 0

    for tour, (path, given_cost) in robots_tours.items():
        if path[0] != 0 or path[-1] != 0:
            return "FAIL: Route does not start or end at the depot."
        
        calculated_cost = 0
        current_load = 0
        for i in range(len(path) - 1):
            current_load += cities[path[i]][2] if i != 0 else 0
            if current_load > 40:
                return "FAIL: Capacity exceeded."
            
            dist = calculate_distance(cities[path[i]], cities[path[i + 1]])
            calculated_cost += dist

            total_demand_served[path[i]] += cities[path[i]][2] if i != 0 else 0

        calculated_cost += calculate_distance(cities[path[-1]], cities[path[0]])  # return to depot
        if abs(calculated_cost - given_cost) > 1e-2:  # allowing small floating point discrepancies
            return "FAIL: Tour cost does not match the given cost."
        
        overall_travel_cost_calculated += calculated_cost

    for city, demand in total_demand_served.items():
        if demand < cities[city][2]:
            return "FAIL: Demand not met for city {}".format(city)
    
    # If reached here, everything is correct
    return "CORRECT"

# Run the unit test
result = check_solution(robots_tours)
print(result)