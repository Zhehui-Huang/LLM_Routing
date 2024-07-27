import math

def calculate_distance(coord1, coord2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_solution(tours, demands, capacities, coordinates):
    """Verify if the provided solution meets all the problem constraints."""
    num_robots = len(tours)
    total_travel_cost_calculated = 0
    demands_satisfied = [0] * len(demands)
    
    for robot_id, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # start and end at depot city 0
        current_load = 0
        last_city = tour[0]
        
        for city in tour[1:]:
            current_load += demands[city]
            if current_load > capacities[robot_id]:
                return "FAIL"  # capacity exceeded
            
            # Travel cost
            distance = calculate_distance(coordinates[last_city], coordinates[city])
            total_travel_cost_calculated += distance
            last_city = city
            demands_satisfied[city] += demands[city]
        
        # Return to depot travel cost
        distance_back = calculate_distance(coordinates[last_city], coordinates[0])
        total_travel_cost_calculated += distance_back
    
    # Check if all demands are met exactly
    if any(d != demands_satisfied[i] for i, d in enumerate(demands)):
        return "FAIL"
    
    # Compare calculated cost to given
    if not math.isclose(total_travel_dept, 646.69, abs_tol=1e-2):
        return "FAIL"  # significantly different cost
    
    return "CORRECT"

# Provided data entities (example only, actual solution may differ)
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
capacities = [40] * 8  # assuming each robot has the same capacity

coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

tours = [
    [0, 18, 19, 0], [0, 9, 17, 0], [0, 12, 15, 0], [0, 8, 13, 0],
    [0, 14, 22, 0], [0, 4, 11, 0], [0, 3, 10, 0], [0, 5, 7, 0],
    [0, 1, 2, 0], [0, 6, 20, 0], [0, 16, 21, 0]
]

# Checking if the solution provided meets all conditions
print(verify_solution(tours, demands, capacities, coordinates))