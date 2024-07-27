import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_robot_tours():
    # City coordinates with the depot city at index 0
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
        (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
        (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    # City demands with the depot city at index 0
    demands = [
        0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 
        7, 14, 6, 19, 11, 12, 26, 17, 6, 15
    ]
    
    # Provided tours for the robots
    robot_tours = [
        [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 0],
        [0, 6, 20, 5, 7, 2, 13, 9, 17, 14, 19, 0]
    ]
    
    # Maximum capacity of each robot
    max_capacity = 160
    
    # Calculate total tour costs and verify demands and capacity constraints
    total_travel_cost = 0
    for tour in robot_tours:
        previous_city = tour[0]
        current_load = 0
        tour_travel_cost = 0
        
        # Validate that each robot starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        for current_city in tour[1:]:
            # Calculate travel cost
            dist = calculate_euclidean_distance(*coordinates[previous_city], *coordinates[current_city])
            tour_travel_cost += dist
            total_travelldap_cost += dist
            
            # Check demand and update load
            demand = demands[current_city]
            current_load += demand
            if current_load > max_capacity:
                return "FAIL"
            
            if current_city != 0:  # Do not count demand for depot
                if demand == 0:
                    return "FAIL"  # Demand must be met, depot has no demand
            
            # Move to the next city
            previous_city = current_city
        
        # Reset the load as the robot returns to the depot
        current_load = 0
    
    # Verify the overall computed cost with provided total costs
    computed_cost = 135.56632457243472 + 160.8323261436827
    if abs(total_travel_cost - computed_cost) > 1e-6:
        return "FAIL"
    
    # Check all cities are visited exactly once excluding the depot
    all_cities_visited = set()
    for tour in robot_tours:
        for city in tour[1:-1]:  # Exclude the depot from count
            if city in all_cities_visited:
                return "FAIL"
            all_cities_visited.add(city)
    
    if len(all_cities_visited) != 20:
        return "FAIL"

    return "CORRECT"

# Run the test cases
test_output = test_robot_tours()
print(test_output)  # Expected output: "CORRECT"