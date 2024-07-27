import math

# City coordinates and demands definition
cities = {
    0: {"coord": (30, 40), "demand": 0},
    1: {"coord": (37, 52), "demand": 19},
    2: {"coord": (49, 49), "demand": 30},
    3: {"coord": (52, 64), "demand": 16},
    4: {"coord": (31, 62), "demand": 23},
    5: {"coord": (52, 33), "demand": 11},
    6: {"coord": (42, 41), "demand": 31},
    7: {"coord": (52, 41), "demand": 15},
    8: {"coord": (57, 58), "demand": 28},
    9: {"coord": (62, 42), "demand": 8},
    10: {"coord": (42, 57), "demand": 8},
    11: {"coord": (27, 68), "demand": 7},
    12: {"coord": (43, 67), "demand": 14},
    13: {"coord": (58, 48), "demand": 6},
    14: {"coord": (58, 27), "demand": 19},
    15: {"coord": (37, 69), "demand": 11}
}

# Robots' tours and the solution provided
robots_tours = {
    0: [0, 6, 0],
    1: [0, 1, 10, 13, 0],
    2: [0, 2, 0],
    3: [0, 4, 11, 0],
    4: [0, 7, 5, 9, 0],
    5: [0, 15, 12, 0],
    6: [0, 14, 3, 0],
    7: [0, 8, 0]
}

# Calculating distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]["coord"]
    x2, y2 = cities[city2]["coord"]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Validate the solution
def validate_solution(tours, robot_capacity=35):
    total_cost = 0
    demands_met = {i: 0 for i in range(1, 16)}
    
    # For each robot's tour
    for tour in tours.values():
        load = 0
        tour_cost = 0
        
        # Calculate load and travel cost
        for i in range(len(tour) - 1):
            city = tour[i]
            next_city = tour[i + 1]
            load += cities[next_city]["demand"]
            tour_cost += calculate_distance(city, next_city)
        
        # Validating end city
        if tour[-1] != 0:
            return "FAIL"

        # Check load does not exceed capacity and calculate demands met
        if load > robot_capacity:
            return "FAIL"
            
        total_cost += tour_cost
        
        for city in tour:
            if city != 0:
                demands_met[city] += cities[city]["demand"]

    # Check if all demands are met exactly
    if any(demands_met[city] != cities[city]["demand"] for city in demands_met):
        return "FAIL"

    # Check if cumulative cost is correct
    expected_total_cost = 499.44
    if not math.isclose(total_cost, expected_total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run validation
validation_result = validate_solution(robots_tours)
print(validation_result)