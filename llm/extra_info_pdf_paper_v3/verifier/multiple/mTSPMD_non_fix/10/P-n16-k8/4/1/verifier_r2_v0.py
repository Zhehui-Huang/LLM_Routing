import math

# Mock data for cities' coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Provided tours and their costs
robot_tours = [
    ([0, 1, 0], 27.78), ([0, 2, 0], 42.05), ([0, 3, 0], 65.12),
    ([0, 4, 0], 44.05), ([0, 5, 0], 46.17), ([0, 6, 0], 24.08),
    ([0, 7, 0], 44.05), ([0, 8, 0], 64.90)
]

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def verify_tours(robot_tours):
    cities_visited = set()
    total_calculated_cost = 0.0
    
    for tour, reported_cost in robot_tours:
        calculated_cost = 0.0
        
        # Verify each tour starts from depot city 0
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            cities_visited.add(city1)
            
            # Calculate distance
            distance = calculate_euclidean_distance(city1, city2)
            calculated_cost += distance
        
        # Check the reported cost versus the calculated cost
        if not math.isclose(calculated_cost, reported_cost, rel_tol=0.01):
            return "FAIL"
        
        total_calculated_cost += reported_cost
    
    # Verify if all cities are visited exactly once
    if len(cities_visited) != len(cities) or any(city not in cities_visited for city in cities):
        return "FAIL"
    
    # Total travel cost reported in the prompt
    reported_total_cost = 358.20

    if not math.isclose(total_calculated_cost, reported_total_cost, rel_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Run the verification tests
result = verify_tours(robot_tours)
print(result)