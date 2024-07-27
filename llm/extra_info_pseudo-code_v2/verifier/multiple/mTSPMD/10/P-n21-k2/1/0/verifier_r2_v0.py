import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities given their coordinates."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_solution():
    # Coordinates for each city
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
        4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
        8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
        16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
    }
    
    # Provided tours
    tours = {
        0: [0, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 8, 18, 19, 3, 12, 15, 4, 11, 10, 0],
        1: [1, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 8, 18, 19, 3, 12, 15, 4, 11, 10, 1]
    }
    
    # Expected costs based on solution provided
    given_costs = {
        0: 206.87028231201825,
        1: 189.21546060749714
    }
    
    overall_cost = 0
    
    # Validate tours and total travel costs
    for robot_id, tour in tours.items():
        start_depot = tour[0]
        end_depot = tour[-1]
        
        # Each city should be visited once across all robots
        visited = set()
        
        cost = 0
        for i in range(len(tour) - 1):
            city1, city2 = tour[i], tour[i + 1]
            visited.add(city1)
            
            # Calculate distance
            cost += calculate_distance(cities[city1], cities[city2])
        
        # Ensure starting and ending at the respective depots
        if not (start_depot == robot_id and end_depot == robot_id):
            return "FAIL"
        
        # Validate the total travel cost for the robot
        if not math.isclose(cost, given_costs[robot_id], rel_tol=1e-5):
            return "FAIL"
        
        overall_cost += cost
    
    # Check if all cities are visited once by verifying the total number of unique visits
    total_visits = len(set.union(*[set(tour) for tour in tours.values()]))
    if total_visits != len(cities):
        return "FAIL"

    # Total cost of all routes should match
    expected_total_cost = 396.0857429195154
    if not math.isclose(overall_cost, expected_total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Output the validation result
print(validate_solution())