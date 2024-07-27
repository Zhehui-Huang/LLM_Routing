import math

# Coordinates of the cities including depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Provided algorithm results
robots_tours = [
    [0, 21, 16, 3, 0], [0, 6, 20, 8, 0], [0, 1, 10, 14, 0],
    [0, 2, 7, 17, 0], [0, 4, 11, 18, 0], [0, 5, 22, 19, 0],
    [0, 13, 9, 0], [0, 15, 12, 0]
]

robots_costs = [66.82, 77.14, 85.83, 73.39, 104.0, 105.43, 68.39, 66.12]
total_cost_provided = 647.13

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Validate solution
def validate_solution(robots_tours, robots_costs, total_cost_provided):
    visited_cities = set()
    total_calculated_cost = 0
    
    # Check each robot's tour
    for index, tour in enumerate(robots_tours):
        cost_calculated = 0
        previous_city = tour[0]
        
        # Check if tour starts and ends with the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate travel cost and validate cities
        for city in tour[1:]:
            if city in visited_cities and city != 0:
                return "FAIL"
            visited_cities.add(city)
            cost_calculated += calculate_distance(previous_city, city)
            previous_city = city
        
        # Compare calculated and provided tour cost
        if not math.isclose(cost_calculated, robots_costs[index], abs_tol=0.01):
            return "FAIL"
        
        total_calculated_cost += cost_calculated
    
    # Check if all cities visited once
    if len(visited_cities) != 22:  # 23 minus the depot
        return "FAIL"
    
    # Check if total cost is correct
    if not math.isclose(total_calculated_cost, total_cost_provided, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Run the validation
result = validate_solution(robots_tours, robots_costs, total_cost_provided)
print(result)