import math

# Predefined data setup
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Tours given
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

robots_costs = [85.83, 102.2, 103.68, 121.79, 83.72, 107.55, 57.77, 65.36]
overall_cost = 727.92

# Function to calculate the Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_solution(robots_tours, robots_costs, overall_cost):
    unique_visited = set()
    computed_overall_cost = 0
    
    for robot_index, tour in enumerate(robots_tours):
        start_city = tour[0]
        end_city = tour[-1]
        
        # Start and end at the depot check
        if start_position != 0 or end_city != 0:
            return "FAIL"
        
        # Tour cost calculation
        tour_cost = 0
        last_city = tour[0]
        for city in tour[1:]:
            tour_cost += calculate_distance(last_city, city)
            unique_visited.add(city)
            last_city = city

        # Cost verification per robot
        if not math.isclose(tour_cost, robots_costs[robot_index], rel_tol=1e-2):
            return "FAIL"
        
        computed_overall_cost += tour_cost
    
    # Completeness of city visit check, excluding depot
    if len(unique_visited) != len(cities_coordinates) - 1:
        return "FAIL"
    
    # Overall cost verification
    if not math.isclose(computed_overall_cost, overall_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Validate the solution
validation_result = validate_solution(robots_tours, robots_costs, overall_cost)
print(validation_result)