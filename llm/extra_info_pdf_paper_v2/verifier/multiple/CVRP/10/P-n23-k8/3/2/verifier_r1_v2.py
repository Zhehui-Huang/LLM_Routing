import math

# City data: index: (x, y, demand)
cities = {
    0: (30, 40, 0), 1: (37, 52, 7), 2: (49, 49, 30), 3: (52, 64, 16), 4: (31, 62, 23),
    5: (52, 33, 11), 6: (42, 41, 19), 7: (52, 41, 15), 9: (62, 42, 8),
    10: (42, 57, 8), 11: (27, 68, 7), 12: (43, 67, 14), 13: (58, 48, 6), 14: (58, 27, 19),
    15: (37, 69, 11), 16: (38, 46, 12), 18: (62, 63, 17), 19: (63, 69, 6),
    20: (45, 35, 15), 21: (32, 39, 5), 22: (56, 37, 10)
}

# Provided route details and associated costs
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
    x1, y1 = cities[city1][:2]
    x2, y2 = cities[city2][:2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def check_solution(robots_tours):
    total_demand_served = {i: 0 for i in cities if i != 0}  # Exclude depot
    overall_travel_cost_calculated = 0
    
    for _, (tour, given_cost) in robots_tours.items():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Route does not start or end at depot."
        
        calculated_cost = 0
        for i in range(len(tour) - 1):
            if tour[i] != 0:
                total_demand_served[tour[i]] += cities[tour[i]][2]
            distance = calculate_distance(tour[i], tour[i + 1])
            calculated_cost += distance

        # Include cost to return to depot
        if abs(calculated_cost + calculate_distance(tour[-1], tour[0]) - given_cost) > 1e-2:
            return "FAIL: Tour cost mismatch."

        overall_travel_cost_calculated += given_cost

    # Check if all demands are met exactly
    for city, demand in total_demand_served.items():
        if demand != cities[city][2]:
            return f"FAIL: Demand not met for city {city}. Needed: {cities[city][2]}, Met: {demand}"

    return "CORRECT"

# Execute the verification
result = check_solution(robots_tours)
print(result)