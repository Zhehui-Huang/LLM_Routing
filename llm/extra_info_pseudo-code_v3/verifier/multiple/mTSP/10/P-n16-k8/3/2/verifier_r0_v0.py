import math

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Tours and costs as provided in the hypothetical solution
robot_tours = {
    0: [0, 1, 0], 1: [0, 2, 0], 2: [0, 3, 0], 3: [0, 4, 0], 4: [0, 5, 0],
    5: [0, 6, 0], 6: [0, 7, 0], 7: [0, 8, 0]
}

# Expected travel costs for each robot
expected_costs = [
    27.784887978899608, 42.04759208325728, 65.11528238439882,
    44.04543109109048, 46.17358552246078, 24.08318915758459,
    44.04543109109048, 64.89992295835181
]

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Check the solution
def validate_solution(robot_tours, expected_costs):
    all_cities_visited = set()
    total_cost_calculated = 0.0
    
    for robot_id, tour in robot_tours.items():
        tour_cost = 0.0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(tour[i], tour[i+1])
            if tour[i] != 0:
                all_cities_visited.add(tour[i])
        
        if tour[0] != tour[-1] or tour[0] != 0:  # Check if tour starts and ends at the depot
            return "FAIL"
        
        # Check if the calculated cost matches the expected cost (within a reasonable precision)
        if not math.isclose(tour_cost, expected_costs[robot_id], abs_tol=0.01):
            return "FAIL"
        
        total_cost_calculated += tour_cost
    
    # Check if all cities are visited exactly once
    if all_cities_visited != set(range(1, 16)):
        return "FAIL"
    
    # Check overall cost
    if not math.isclose(total_cost_calculated, sum(expected_costs), abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Output test result
print(validate_solution(robot_tours, expected_costs))