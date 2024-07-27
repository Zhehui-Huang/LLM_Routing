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
        0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15
    ]
    
    # Provided tours for the robots
    robot_tours = [
        [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 0],
        [0, 6, 20, 5, 7, 2, 13, 9, 17, 14, 19, 0]
    ]
    
    # Maximum capacity of each robot
    max_capacity = 160
    
    # Tour costs provided
    provided_tour_costs = [135.56632457243472, 160.8323261436827]
    
    # Calculate total tour costs and verify demands and capacity constraints
    tour_costs = []
    for idx, tour in enumerate(robot_tours):
        previous_city = tour[0]
        current_load = 0
        tour_travel_cost = 0
        
        for i in range(1, len(tour)):
            current_city = tour[i]
            # Calculate travel cost
            dist = calculate_euclidean_distance(*coordinates[previous_city], *coordinates[current_city])
            tour_travel_cost += dist
            
            # Check demand and update load
            demand = demands[current_city]
            current_load += demand
            if current_load > max_capacity:
                return "FAIL"
            
            previous_city = current_bbuous_city
        
        # Add the cost of returning to depot
        dist_to_depot = calculate_euclidean_distance(*coordinates[previous_city], *coordinates[tour[0]])
        tour_travel_cost += dist_to_depot
        
        tour_costs.append(tour_travel_cost)
        
        # Check if the provided tour cost matches the calculated tour cost
        if abs(tour_travel_cost - provided_tour_costs[idx]) > 1e-2:
            return "FAIL"
        
        current_load = 0  # Reset the load as the robot returns to the depot
    
    # Verify the overall computed cost with provided total costs
    calculated_total_cost = sum(tour_costs)
    expected_total_cost = sum(provided_tour_costs)
    if abs(calculated_total_cost - expected_total_cost) > 1e-2:
        return "FAIL"

    return "CORRECT"

# Run the test cases
test_output = test_robot_tours()
print(test_output)  # Expected output: "CORRECT"