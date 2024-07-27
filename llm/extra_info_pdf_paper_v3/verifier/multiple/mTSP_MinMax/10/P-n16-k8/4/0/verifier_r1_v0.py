import math

# Cities coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 
    14: (58, 27), 15: (37, 69)
}

# Provided robot tours
robot_tours = [
    [0, 13, 9, 0],
    [0, 15, 12, 0],
    [0, 6, 0],
    [0, 4, 11, 0],
    [0, 5, 14, 0],
    [0, 8, 3, 0],
    [0, 1, 10, 0],
    [0, 2, 7, 0]
]

# Provided tour costs
provided_costs = [68.39, 66.12, 24.08, 57.39, 62.44, 72.82, 41.77, 51.59]
provided_max_cost = 72.82

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution():
    visited_cities = set()
    
    # Verify each robot's tour and calculate actual costs
    actual_costs = []
    for tour in robot_tours:
        tour_cost = 0
        last_city = tour[0]
        for city in tour[1:]:
            # Check if city is visited once
            if city != 0 and city in visited_cities:
                print("FAIL: City visited more than once")
                return "FAIL"
            visited_cities.add(city)
            
            # Calculate tour cost
            tour_cost += calculate_distance(last_city, city)
            last_city = city
        
        actual_costs.append(round(tour_cost, 2))
    
    # Check if all non-depot cities are visited exactly once
    if visited_cities != set(range(1, 16)):
        print("FAIL: Not all cities were visited exactly once")
        return "FAIL"
    
    # Check if final tour costs match provided costs approximately
    if not all(math.isclose(ac, pc, abs_tol=0.1) for ac, pc in zip(actual_costs, provided_costs)):
        print("FAIL: Provided tour costs do not match calculated tour costs")
        return "FAIL"
    
    # Verify maximum travel cost constraint
    max_cost = max(actual_costs)
    if not math.isclose(max_cost, provided_max_condition, abs_tol=0.1):
        print("FAIL: Maximum travel cost condition not met")
        return "FAIL"
    
    # Verify if the output contains all the required elements according to format
    # Note: This check would typically require analysis of printed/logged outputs which is outside the current executable scope
    
    print("CORRECT")
    return "CORRECT"

# Execute the test
verify_solution()