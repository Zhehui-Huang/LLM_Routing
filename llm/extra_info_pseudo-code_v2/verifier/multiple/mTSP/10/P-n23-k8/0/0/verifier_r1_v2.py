import math

# Predefined data: coordinates of each city
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Provided tours for robots
robots_tours = [
    [0, 1, 10, 14, 0],
    [0, 17, 9, 12, 0],
    [0, 20, 22, 19, 0],
    [0, 5, 21, 18, 0],
    [0, 15, 2, 7, 0],
    [0, 8, 13, 11, 0],
    [0, 6, 4, 0],
    [0, 3, 16, 0]
]

# Provided costs for each robot's tour
robots_costs = [85.83, 102.2, 103.68, 121.79, 83.72, 107.55, 57.77, 65.36]
overall_cost = 727.92

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to validate the provided solution
def validate_solution(robots_tours, robots_costs, overall_cost):
    unique_visited = set()
    computed_overall_cost = 0
    
    for i, tour in enumerate(robots_tours):
        # Check start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check tour path and calculate cost
        tour_cost = 0
        for j in range(len(tour) - 1):
            dist = calculate_distance(tour[j], tour[j + 1])
            tour_cost += dist
        
        # Add cities visited excluding the depot
        unique_visited.update(tour[1:-1])
        
        # Check if the calculated cost matches the provided tour cost
        if not math.isclose(tour_cost, robots_costs[i], rel_tol=1e-2):
            return "FAIL"
        
        computed_overall_cost += tour_cost

    # Check if all cities are visited once and only once (23 cities: 1 Depot + 22 others) 
    if len(unique_visited) != 22:
        return "FAIL"

    # Check the overall cost
    if not math.isclose(computed_overall_cost, overall_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Validate the provided solution
validation_result = validate_solution(robots_tours, robots_costs, overall_cost)
print(validation_result)