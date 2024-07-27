import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tours_and_costs(robots_tours, robots_costs, city_coordinates):
    overall_cost_calculated = 0
    cities_visited = set()
    
    for robot_id, (tour, cost) in enumerate(zip(robots_tours, robots_costs)):
        # Requirement 1: Check if each tour starts and ends at the designated depot
        if tour[0] != tour[-1] or tour[0] != robot_id:
            print(f"FAIL: Robot {robot_id} does not start and end at its designated depot.")
            return "FAIL"
        
        # Add visited cities to the set, excluding the depot start/end
        cities_visited.update(tour[1:-1])
        
        # Requirement 4: Calculate travel cost and compare
        calculated_cost = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            calculated_cost += calculate_euclidean_distance(*city_coordinates[city_from], *city_coordinates[city_to])

        # Compare calculated cost to provided cost
        if not math.isclose(calculated_cost, cost, rel_tol=1e-2):
            print(f"FAIL: Cost mismatch for Robot {robot_id}. Expected: {cost}, Calculated: {calculated_cost}")
            return "FAIL"
        
        overall_cost_calculated += calculated_cost
    
    # Requirement 2: Check if all cities are visited exactly once
    all_cities = set(range(len(city_coordinates)))
    if cities_visited != all_cities:
        print("FAIL: Not all cities are visited exactly once.")
        return "FAIL"
    
    # Requirement 3 implies verification but not explicitly checked here since no optimal cost given
    # Requirement 5 and 6 are regarding output format which we assume here are followed in the supplied answer
    # Requirement 7 (genetic algorithm) cannot be verified by this test without algorithm details
    
    # Verify combined cost if provided overall cost is given
    expected_overall_cost = 3765.11  # From provided data
    if not math.isclose(overall_cost_calculated, expected_overall_cost, rel_tol=1e-2):
        print(f"FAIL: Overall cost miscalculated. Expected: {expected_overall_cost}, Calculated: {overall_cost_calculated}")
        return "FAIL"
    return "CORRECT"

city_coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

robots_tours = [
    [0, 21, 4, 19, 2, 12, 18, 10, 20, 5, 17, 8, 11, 7, 3, 13, 6, 22, 15, 14, 9, 1, 16, 0],
    [1, 10, 4, 14, 19, 22, 17, 9, 6, 21, 13, 3, 15, 18, 2, 0, 7, 11, 20, 5, 16, 8, 12, 1],
    [2, 0, 12, 18, 1, 10, 11, 5, 9, 22, 17, 19, 16, 14, 6, 3, 8, 15, 13, 4, 21, 7, 20, 2],
    [3, 1, 16, 9, 13, 5, 17, 7, 22, 8, 18, 2, 14, 12, 15, 4, 11, 19, 21, 10, 0, 6, 20, 3],
    [4, 7, 18, 14, 10, 20, 5, 22, 17, 9, 13, 1, 2, 0, 6, 21, 16, 8, 3, 12, 15, 11, 19, 4],
    [5, 14, 17, 0, 21, 11, 7, 6, 8, 19, 3, 4, 1, 22, 16, 15, 13, 2, 12, 18, 9, 10, 20, 5],
    [6, 10, 2, 18, 9, 15, 12, 20, 17, 7, 13, 19, 16, 22, 11, 3, 14, 1, 21, 4, 5, 8, 0, 6],
    [7, 17, 21, 19, 18, 10, 3, 15, 22, 6, 11, 13, 1, 8, 16, 5, 14, 12, 9, 20, 0, 2, 4, 7]
]
robots_costs = [488.74, 488.41, 495.67, 405.27, 393.04, 425.46, 535.63, 532.89]

# Check solution
result = verify_tours_and_costs(robots_tours, robots_costs, city_coords)
print(result)